library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use work.pack_tipos.all; 

entity filtragem1x64 is
    port (
		tamLinha       : in  std_logic_vector(4 downto 0);
		tamColuna      : in  std_logic_vector(4 downto 0);
        linha_refs     : in  array_64;
		coluna_refs    : in  array_64;
		sinalSeletor   : in std_logic;
        linha_saidas   : out array_64;
		coluna_saidas  : out array_64
    );
	
end filtragem1x64;

architecture Behavioral of filtragem1x64 is

	component seletorEntradas is
		port (
			tam                 : in  std_logic_vector(4 downto 0);
			entradas            : in  array_64;
			saidas_selecionadas : out array_64
		);
	end component;

    component filtro is
        port (
            A      : in  unsigned(7 downto 0);  
            B      : in  unsigned(7 downto 0);
            C      : in  unsigned(7 downto 0);  
            Saida  : out unsigned(7 downto 0)
        );
    end component;
	
	component filtragem is
		port (
			tam             : in  std_logic_vector(4 downto 0);
			entrada_refs    : in  array_64;
			saida_filtrada  : out array_64
		);
	end component;
	
	component seletorFiltragem is
		port (
			entradas_coluna		: in array_64;
			entradas_linha		: in array_64;
			filtrados_coluna    : in array_64;
			filtrados_linha     : in array_64;
			sinal 				: in std_logic;
			saida_coluna        : out array_64;
			saida_linha         : out array_64
		);
	end component;

    signal saida1: unsigned (7 downto 0);
	signal linhas_selecionadas, linha_filtrada_sig: array_64;
	signal colunas_selecionadas, coluna_filtrada_sig: array_64;
	signal seletor_linha, seletor_coluna: array_64;
	signal seletor_linha_filtrada, seletor_coluna_filtrada: array_64;
	--signal zeros_select: array_64; -- foi para o seletor.vhd

begin
	--zeros_select <= (others => to_unsigned(0, 8)); -- foi para o seletor.vhd
	
	-- Seletor e array de filtros para a linha
	SLinha: seletorEntradas port map(
		tam => tamLinha,
		entradas => linha_refs,
		saidas_selecionadas => linhas_selecionadas
	);
	fLinha: filtragem port map(
		tam => tamLinha,
		entrada_refs => linhas_selecionadas,
		saida_filtrada => linha_filtrada_sig
	);
		
	seletor_linha_filtrada(0 to 127) <= linha_filtrada_sig(0 to 127);

	
	
	-- Seletor e array de filtros para a coluna
	SColuna: seletorEntradas port map(
		tam => tamColuna,
		entradas => coluna_refs,
		saidas_selecionadas => colunas_selecionadas
	);
	
	fColuna: filtragem port map(
		tam => tamColuna,
		entrada_refs => colunas_selecionadas,
		saida_filtrada => coluna_filtrada_sig
	);
	
	seletor_coluna_filtrada(0 to 127) <= coluna_filtrada_sig(0 to 127);
	
	-- Amostra -1,-1
	f1: filtro port map(
		A => coluna_refs(0),
		B => linha_refs(-1),
		C => linha_refs(0),
		Saida => saida1
	);
    seletor_linha_filtrada(-1)	<= saida1;
	seletor_coluna_filtrada(-1)  <= saida1;
	
	SF: seletorFiltragem port map (
		entradas_coluna	=> coluna_refs,
		entradas_linha => linha_refs,
		filtrados_coluna => seletor_coluna_filtrada,
		filtrados_linha => seletor_linha_filtrada,
		sinal => sinalSeletor,
		saida_coluna => seletor_coluna,
		saida_linha => seletor_linha
	);
	
	linha_saidas <= seletor_linha;
	coluna_saidas <= seletor_coluna;
	
	
	
end Behavioral;
