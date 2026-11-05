library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity fltr_unit is

    Port (
        A  : in  unsigned(7 downto 0);  
        B   : in  unsigned(7 downto 0);
        C  : in  unsigned(7 downto 0);  
        outpt       : out unsigned(7 downto 0)   
    );

end fltr_unit;

architecture Behavioral of fltr_unit is
    signal sum_AC : unsigned(7 downto 0);
    signal carry_stage1 : unsigned(0 downto 0);
    signal carry_stage2 : unsigned(0 downto 0);
begin

    carry_stage1(0) <= A(0) AND C(0);
    sum_AC <= resize(A(7 downto 1), 8) + 
              resize(C(7 downto 1), 8) +
              carry_stage1;

    carry_stage2(0) <= sum_AC(0) OR B(0);
    outpt <= resize(sum_AC(7 downto 1), 8) + 
             resize(B(7 downto 1), 8) +
             carry_stage2;

end Behavioral;