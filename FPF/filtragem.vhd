library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.pack_tipos.all;

entity filtragem is
    port (
		tam             : in  std_logic_vector(4 downto 0);
        entrada_refs    : in  array_64;
        saida_filtrada  : out array_64
    );
end filtragem;

-- TABELA do tam:
-- "00001" = 4
-- "00011" = 8
-- "00111" = 16
-- "01111" = 32
-- "11111" = 64

architecture Behavioral of filtragem is

    component filtro is
        port (
            A      : in  unsigned(7 downto 0);  
            B      : in  unsigned(7 downto 0);
            C      : in  unsigned(7 downto 0);  
            Saida  : out unsigned(7 downto 0)
        );
    end component;

    signal saidas_filtro_1: array_64;

begin
	gen_filtros : for i in 0 to 126 generate
		filtro_inst : filtro
			port map (
				A     => entrada_refs(i-1),
				B     => entrada_refs(i),
				C     => entrada_refs(i+1),
				Saida => saidas_filtro_1(i)
			);
	end generate;

	with tam select
		saida_filtrada(7) <= entrada_refs(7) when "00001", 
		                     saidas_filtro_1(7) when others;
	
	with tam select
		saida_filtrada(15) <= entrada_refs(15) when "00011", -- não filtra o elemento 15 (amostra da ponta) quando tam for 8
		                      saidas_filtro_1(15) when others;  -- nos demais casos, filtra
	with tam select
		saida_filtrada(31) <= entrada_refs(31) when "00111",
		                      saidas_filtro_1(31) when others;
	
	with tam select
		saida_filtrada(63) <= entrada_refs(63) when "01111",
		                      saidas_filtro_1(63) when others;
	
	saida_filtrada(127) <= entrada_refs(127);

	saida_filtrada(-1)  <= entrada_refs(-1);

	saida_filtrada(0 to 6)    <= saidas_filtro_1(0 to 6);
    saida_filtrada(0 to 14) <= saidas_filtro_1(0 to 14);
    saida_filtrada(16 to 30) <= saidas_filtro_1(16 to 30);
    saida_filtrada(32 to 62) <= saidas_filtro_1(32 to 62);
    saida_filtrada(64 to 126) <= saidas_filtro_1(64 to 126);

end Behavioral;
