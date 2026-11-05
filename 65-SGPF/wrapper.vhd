library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.pack_tipos.all;

entity wrapper is
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
end wrapper;

architecture rtl of wrapper is
    signal ref_ext_reg       : sample_array_ext_t;
    signal filter_enable_reg : std_logic;
    signal ref_comb_out      : sample_array_t;
    signal ref_out_reg       : sample_array_t;
    
    signal load_inputs       : std_logic;
    signal latch_output      : std_logic;
    signal cycle_count_id    : unsigned(7 downto 0); 

    component array_of_filters is
        port (
            W             : in  unsigned(6 downto 0);
            H             : in  unsigned(6 downto 0);
            cycle_count   : in  unsigned(7 downto 0);
            filter_enable : in  std_logic;
            ref_ext_in    : in  sample_array_ext_t;
            ref_out       : out sample_array_t
        );
    end component;

    component ctrl is
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
    end component;

begin
    u_ctrl : ctrl
        port map (
            clk             => clk,
            rst             => rst,
            W               => W,
            H               => H,
            start           => start,
            load_inputs     => load_inputs,
            latch_output    => latch_output,
            done            => done,
            cycle_count_out => cycle_count_id
        );

    -- barreira de entrada
    process (clk)
    begin
        if rising_edge(clk) then
            if rst = '1' then
                ref_ext_reg       <= (others => (others => '0'));
                filter_enable_reg <= '0';
            elsif load_inputs = '1' then
                ref_ext_reg       <= ref_ext_in;
                filter_enable_reg <= filter_enable;
            end if;
        end if;
    end process;

    u_filter_array : array_of_filters
        port map (
            W             => W,
            H             => H,
            cycle_count   => cycle_count_id,
            filter_enable => filter_enable_reg,
            ref_ext_in    => ref_ext_reg,
            ref_out       => ref_comb_out
        );

    -- barreira saída
    process (clk)
    begin
        if rising_edge(clk) then
            if rst = '1' then
                ref_out_reg <= (others => (others => '0'));
            elsif latch_output = '1' then
                ref_out_reg <= ref_comb_out;
            end if;
        end if;
    end process;

    ref_out <= ref_out_reg;
end rtl;