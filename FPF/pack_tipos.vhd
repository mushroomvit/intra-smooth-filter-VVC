library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

package pack_tipos is
    type array_4 is array (-1 to 7) of unsigned(7 downto 0); 
    type array_64 is array (-1 to 127) of unsigned(7 downto 0); 
end pack_tipos;