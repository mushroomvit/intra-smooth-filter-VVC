
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.pack_tipos.all;

entity seletorEntradas is
    port (
		tam                 : in  std_logic_vector(4 downto 0);
		entradas            : in  array_64;
		saidas_selecionadas : out array_64
    );
end seletorEntradas;

architecture Behavioral of seletorEntradas is
	
	signal zeros: array_64;    -- puxei os zeros para ca

begin
	zeros <= (others => to_unsigned(0, 8));
	with tam select
		saidas_selecionadas <= entradas(-1 to 7) & zeros(8 to 127) when "00001", -- tam 4
							   entradas(-1 to 15) & zeros(16 to 127) when "00011", -- tam 8 necessita apenas refs (-1 to 15)
		                       entradas(-1 to 31) & zeros(32 to 127) when "00111", -- tam 16 necessita apenas refs (-1 to 31)
		                       entradas(-1 to 63) & zeros(64 to 127) when "01111", -- tam 32 necessita apenas refs (-1 to 63)
		                       entradas(-1 to 127) when "11111",                   -- tam 64 necessita todas refs
		                       zeros when others; -- tams desconhecidos. também vale para o tam 4 que nunca passa por filtragem.

end Behavioral;