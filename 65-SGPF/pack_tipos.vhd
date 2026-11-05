library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

package pack_tipos is
    type sample_array_ext_t is array (-1 to 65) of unsigned(7 downto 0);
    type sample_array_t is array (0 to 64) of unsigned(7 downto 0);

    type array_8 is array (-1 to 7) of unsigned(7 downto 0);
    type array_16 is array (-1 to 15) of unsigned(7 downto 0);
    type array_32 is array (-1 to 31) of unsigned(7 downto 0);
    type array_64 is array (-1 to 127) of unsigned(7 downto 0); 
end pack_tipos;