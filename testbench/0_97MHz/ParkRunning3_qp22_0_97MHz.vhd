library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use std.textio.all;
use work.pack_tipos.all; 

entity ParkRunning3_qp22_0_97MHz is
end ParkRunning3_qp22_0_97MHz;

architecture sim of ParkRunning3_qp22_0_97MHz is

    -- interface com o wrapper
    signal clk           : std_logic := '0';
    signal rst           : std_logic := '1';
    signal W             : unsigned(6 downto 0) := (others => '0');
    signal H             : unsigned(6 downto 0) := (others => '0');
    signal start         : std_logic := '0';
    signal filter_enable : std_logic := '1'; -- analise considerando que o filtro sempre é aplicado
    signal done          : std_logic;
    signal ref_ext_in    : sample_array_ext_t := (others => (others => '0'));
    signal ref_out       : sample_array_t;

    constant CLK_PERIOD : time := 1030928 ps; -- 0.97 MHz

    component wrapper is
        port (
            clk           : in  std_logic;
            rst           : in  std_logic;
            W             : in  unsigned(6 downto 0); 
            H             : in  unsigned(6 downto 0); 
            start         : in  std_logic;            
            filter_enable : in  std_logic;            
            done          : out std_logic;            
            ref_ext_in    : in  sample_array_ext_t;   
            ref_out       : out sample_array_t
        );
    end component;

begin

    u_wrapper : wrapper
        port map (
            clk           => clk,
            rst           => rst,
            W             => W,
            H             => H,
            start         => start,
            filter_enable => filter_enable,
            done          => done,
            ref_ext_in    => ref_ext_in,
            ref_out       => ref_out
        );

    -- geração do clock
    clk_process : process
    begin
        clk <= '0';
        wait for CLK_PERIOD/2;
        clk <= '1';
        wait for CLK_PERIOD/2;
    end process;

    stim_process : process
        file file_in       : text open read_mode is "ParkRunning3_QP22.txt"; 
        variable v_iline   : line;
        variable v_w, v_h  : integer;
        variable v_val     : integer;
        variable v_comma   : character;
        
        -- arrays temporarios pra armazenar linhas lidas antes do mapeamento
        type temp_array_t is array (0 to 127) of integer;
        variable top_row   : temp_array_t;
        variable left_col  : temp_array_t;
        variable corner    : integer;
        variable corner_idx: integer;
        variable char_peek : character;

    begin

        rst <= '1';
        wait for 20 ns;
        rst <= '0';
        wait for 20 ns;

        -- loop de leitura
        while not endfile(file_in) loop
            
            -- le a largura (w) - primeira linha
            readline(file_in, v_iline);
            read(v_iline, v_w);
            W <= to_unsigned(v_w, 7);

            -- le altura (h) segunda linha
            readline(file_in, v_iline);
            read(v_iline, v_h);
            H <= to_unsigned(v_h, 7);

            -- le a linha de referencias - terceira linha
            readline(file_in, v_iline);
            for i in 0 to v_w - 1 loop
                read(v_iline, v_val);
                top_row(i) := v_val;
                if v_iline'length > 0 then
                    read(v_iline, v_comma); 
                end if;
            end loop;

            -- le a coluna de referencias - quarta linha
            readline(file_in, v_iline);
            for i in 0 to v_h - 1 loop
                read(v_iline, v_val);
                left_col(i) := v_val;
                if v_iline'length > 0 then
                    read(v_iline, v_comma); 
                end if;
            end loop;

            -- le a amostra de canto - quinta linhs
            readline(file_in, v_iline);
            read(v_iline, corner);

            -- ignora separação
            if not endfile(file_in) then
                readline(file_in, v_iline);
            end if;

            -- ==========================================
            -- mapeamento para ref_ext_in [-1 to 129]
            -- ==========================================
            -- para que o canto tenha como vizinhos a 1ª amostra da linha e a 1ª da coluna:
            -- ref_ext_in(H-1)     = left_col(0) (Vizinho Esquerdo)
            -- ref_ext_in(H)       = corner      (Canto)
            -- ref_ext_in(H+1)     = top_row(0)  (Vizinho Direito)
            
            ref_ext_in <= (others => (others => '0'));
            
            corner_idx := v_h; 
            
            -- preenche coluna invertida
            for i in 0 to v_h - 1 loop
                ref_ext_in(corner_idx - 1 - i) <= to_unsigned(left_col(i), 8);
            end loop;
            
            -- preenche o canto
            ref_ext_in(corner_idx) <= to_unsigned(corner, 8);
            
            -- preenche linha após o canto
            for i in 0 to v_w - 1 loop
                ref_ext_in(corner_idx + 1 + i) <= to_unsigned(top_row(i), 8);
            end loop;

            wait for CLK_PERIOD; -- sincroniza
            
            -- começa o bloco
            start <= '1';
            wait for CLK_PERIOD;
            start <= '0';

           -- espera done = 1 - terminou de filtrar o bloco
            wait until done = '1';
            wait for CLK_PERIOD * 2;
            
        end loop;

        report "End of simulation - ParkRunning3 QP22 0.97MHz" severity note;
        wait;
    end process;

end sim;
