library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity ctrl is
    port (
        clk             : in  std_logic;
        rst             : in  std_logic;
        W               : in  unsigned(6 downto 0);
        H               : in  unsigned(6 downto 0);
        start           : in  std_logic;
        load_inputs     : out std_logic;
        latch_output    : out std_logic;
        done            : out std_logic;
        cycle_count_out : out unsigned(7 downto 0) 
    );
end ctrl;

architecture rtl of ctrl is
    signal cycle_count   : unsigned(7 downto 0) := (others => '0');
    signal cycles_needed : unsigned(7 downto 0);
    signal busy          : std_logic := '0';
    signal size          : std_logic_vector(5 downto 0); 
    
    function size_to_bits(x: unsigned(6 downto 0)) return std_logic_vector is
    begin
        case x is
            when "0000100" => return "000";
            when "0001000" => return "001";
            when "0010000" => return "010";
            when "0100000" => return "011";
            when "1000000" => return "100";
            when others    => return "111";
        end case;
    end function;

begin
    cycle_count_out <= cycle_count;
    size <= size_to_bits(W) & size_to_bits(H);

    -- blocos com W=64 ou H=64 precisam de 2 ciclos. restante 1.
    with size select                     
        cycles_needed <= to_unsigned(2,8) when "100100" | "100011" | "100010" | "100001" | "100000" |
                                               "011100" | "010100" | "001100" | "000100", 
                         to_unsigned(0,8) when "111111", 
                         to_unsigned(1,8) when others;

    process (clk)
    begin
        if rising_edge(clk) then
            if rst = '1' then
                busy <= '0';
                cycle_count <= (others => '0');
                load_inputs <= '0';
                latch_output <= '0';
                done <= '0';
            else
                load_inputs <= '0';
                latch_output <= '0';
                done <= '0';
                if (start = '1') and (busy = '0') then
                    load_inputs <= '1'; 
                    
                    if cycles_needed = 0 then
                        latch_output <= '1';
                        done <= '1';
                    else
                        busy <= '1';
                        cycle_count <= (others => '0');
                    end if;

                elsif busy = '1' then
                    load_inputs  <= '1'; 
                    latch_output <= '1';
                    if cycle_count < (cycles_needed - 1) then
                        cycle_count <= cycle_count + 1;
                    else
                        busy <= '0';
                        cycle_count <= (others => '0');
                        done <= '1';
                    end if;
                end if;
            end if;
        end if;
    end process;
end rtl;