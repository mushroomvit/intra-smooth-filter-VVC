library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity filtro is
    Port (
        A      : in  unsigned(7 downto 0);  
        B      : in  unsigned(7 downto 0);
        C      : in  unsigned(7 downto 0);  
        Saida  : out unsigned(7 downto 0)   
    );
end filtro;

architecture Behavioral of filtro is
    signal sumAC    : unsigned(8 downto 0); 
    signal MultB    : unsigned(8 downto 0);
    signal ACMultB  : unsigned(9 downto 0); 
    signal allSum   : unsigned(9 downto 0); 
begin
    sumAC <= RESIZE(A, 9) + RESIZE(C, 9);

    MultB <=  B & '0';

    ACMultB <= resize(sumAC, 10) + resize(MultB, 10);

    allSum <= ACMultB + 2;
	
    Saida <= RESIZE(SHIFT_RIGHT(allSum, 2), 8);
	
end Behavioral;

