library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.pack_tipos.all;

entity array_of_filters is
    port (
        W             : in  unsigned(6 downto 0);
        H             : in  unsigned(6 downto 0);
        cycle_count   : in  unsigned(7 downto 0);
        filter_enable : in  std_logic;
        ref_ext_in    : in  sample_array_ext_t; 
        ref_out       : out sample_array_t      
    );
end array_of_filters;

architecture rtl of array_of_filters is

    signal total_samples : unsigned(9 downto 0);
    signal processed     : unsigned(13 downto 0);
    signal last_sample   : unsigned(13 downto 0);

    signal lane_active   : std_logic_vector(64 downto 0);
    signal filter_out    : sample_array_t;

    component fltr_unit is
        port (
            A     : in  unsigned(7 downto 0);
            B     : in  unsigned(7 downto 0);
            C     : in  unsigned(7 downto 0);
            outpt : out unsigned(7 downto 0)
        );
    end component;

begin
    -- cálculo do total de amostras: 2W + 2H + 1
    total_samples <= resize(W, 10) + resize(W, 10) + resize(H, 10) + resize(H, 10) + 1;
    
    -- calcula quantidade de amostras já processadas nos ciclos anteriores
    processed   <= resize(cycle_count, 8) & "000000"; 
    -- calcula indice da ultima amostra
    last_sample <= resize(total_samples, 14) - 1;

    gen_lanes : for i in 0 to 64 generate
        signal current_idx      : unsigned(13 downto 0);
        signal op_A, op_B, op_C : unsigned(7 downto 0);
    begin
        current_idx <= processed + to_unsigned(i, 14);

        --  a FU esta "ativa" quando filter_enable = '1' e se o indice da amostra i for menor que o da ultima amostrs
        lane_active(i) <= filter_enable when current_idx < last_sample else '0';

        -- operand isolation: recebe a amostra quando a lane estiver ativa, do contrario recebe 0
        op_A <= ref_ext_in(i-1) when lane_active(i) = '1' else (others => '0');
        op_B <= ref_ext_in(i)   when lane_active(i) = '1' else (others => '0');
        op_C <= ref_ext_in(i+1) when lane_active(i) = '1' else (others => '0');


        -- instancia o filtro com os operando determinados antes
        fltr_i : fltr_unit
            port map (
                A     => op_A,
                B     => op_B,
                C     => op_C,
                outpt => filter_out(i)
            );

        -- com a lane ativa recebe a saida do filtro, do contrario recebe a amostra original
        ref_out(i) <= filter_out(i) when lane_active(i) = '1' else ref_ext_in(i);
    end generate;

end rtl;
