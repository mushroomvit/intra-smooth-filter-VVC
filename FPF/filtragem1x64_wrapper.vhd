library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.pack_tipos.all;

entity filtragem1x64_wrapper is
    port (
        clk           : in  std_logic;
        rst           : in  std_logic;
        tamLinha      : in  std_logic_vector(4 downto 0);
        tamColuna     : in  std_logic_vector(4 downto 0);
        linha_refs    : in  array_64;
        coluna_refs   : in  array_64;
        sinalSeletor  : in  std_logic;
        linha_saidas  : out array_64;
        coluna_saidas : out array_64
    );
end filtragem1x64_wrapper;

architecture rtl of filtragem1x64_wrapper is

    component filtragem1x64 is
        port (
            tamLinha      : in  std_logic_vector(4 downto 0);
            tamColuna     : in  std_logic_vector(4 downto 0);
            linha_refs    : in  array_64;
            coluna_refs   : in  array_64;
            sinalSeletor  : in  std_logic;
            linha_saidas  : out array_64;
            coluna_saidas : out array_64
        );
    end component;

    constant C_ZERO_ARRAY64 : array_64 := (others => (others => '0'));

    signal tamLinha_reg      : std_logic_vector(4 downto 0) := (others => '0');
    signal tamColuna_reg     : std_logic_vector(4 downto 0) := (others => '0');
    signal linha_refs_reg    : array_64 := C_ZERO_ARRAY64;
    signal coluna_refs_reg   : array_64 := C_ZERO_ARRAY64;
    signal sinalSeletor_reg  : std_logic := '0';

    signal linha_saidas_core  : array_64 := C_ZERO_ARRAY64;
    signal coluna_saidas_core : array_64 := C_ZERO_ARRAY64;

    signal linha_saidas_reg  : array_64 := C_ZERO_ARRAY64;
    signal coluna_saidas_reg : array_64 := C_ZERO_ARRAY64;

begin

    u_core: filtragem1x64
        port map (
            tamLinha      => tamLinha_reg,
            tamColuna     => tamColuna_reg,
            linha_refs    => linha_refs_reg,
            coluna_refs   => coluna_refs_reg,
            sinalSeletor  => sinalSeletor_reg,
            linha_saidas  => linha_saidas_core,
            coluna_saidas => coluna_saidas_core
        );

    process(clk)
    begin
        if rising_edge(clk) then
            if rst = '1' then
                tamLinha_reg      <= (others => '0');
                tamColuna_reg     <= (others => '0');
                linha_refs_reg    <= C_ZERO_ARRAY64;
                coluna_refs_reg   <= C_ZERO_ARRAY64;
                sinalSeletor_reg  <= '0';
                linha_saidas_reg  <= C_ZERO_ARRAY64;
                coluna_saidas_reg <= C_ZERO_ARRAY64;
            else
                tamLinha_reg      <= tamLinha;
                tamColuna_reg     <= tamColuna;
                linha_refs_reg    <= linha_refs;
                coluna_refs_reg   <= coluna_refs;
                sinalSeletor_reg  <= sinalSeletor;
                linha_saidas_reg  <= linha_saidas_core;
                coluna_saidas_reg <= coluna_saidas_core;
            end if;
        end if;
    end process;

    linha_saidas  <= linha_saidas_reg;
    coluna_saidas <= coluna_saidas_reg;

end rtl;
