library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.pack_tipos.all;

entity seletorFiltragem is
	port(
	entradas_coluna		: in array_64;
	entradas_linha		: in array_64;
	filtrados_coluna    : in array_64;
	filtrados_linha     : in array_64;
	sinal 				: in std_logic;
	saida_coluna        : out array_64;
	saida_linha         : out array_64
	);
end seletorFiltragem;

architecture Behavioral of seletorFiltragem is

begin

with sinal select
		saida_coluna <= filtrados_coluna  when '1', 
						entradas_coluna when others;
with sinal select
		saida_linha <= filtrados_linha  when '1', 
		               entradas_linha when others; 


end Behavioral;