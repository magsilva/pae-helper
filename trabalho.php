<?php

require_once( "exercicio.php" );

/**
* Um trabalho contém todas as informações a seu respeito além de meios de calcular as notas
* com base nas correções feitas no trabalho do aluno.
*/
class Trabalho {
	var
		$id,		// Identificador único de cada trabalho.
		$data_entrega,	// Data limite de entrega, sempre no formato ano-mês-ano hora:minuto.
		$diretorio_base,// Diretório contendo os trabalhos que os alunos entregaram.
		$nome,		// Nome do trabalho.
		$descricao,	// Breve descrição do trabalho.
		$enunciado,	// Texto detalhado sobre o trabalho.
		$exercicios;	// Os exercícios associados ao trabalho, utilizados posteriormente
				// para fazer o cálculo das notas.
		
	/**
	* Método utilizado para fazer a análise do arquivo com os dados a respeito do trabalho.
	*/
	function elemento_inicial( $parser, $nome, $atributo ) {
		$this->ultima_tag = $nome;
		switch( $nome ) {
			case "trabalho":
				$this->id = $atributo[ "id" ];
				$this->data_entrega = $atributo[ "data" ];
				$this->diretorio_base = REPOSITORIO . "/" . $atributo[ "id" ];
				break;
			case "nome":
				break;
			case "descricao":
				break;
			case "enunciado":
				break;
			case "exercicio":
				$this->ultimo_exercicio = $atributo[ "id" ];
				$this->adicionar_exercicio( $atributo[ "id" ], intval( $atributo[ "valor" ] ) );
				break;
			case "criterio":
				$exercicio =& $this->exercicios[ $this->ultimo_exercicio ];
				$exercicio->adicionar_criterio( $atributo[ "id" ], intval( $atributo[ "peso" ] ), $atributo[ "descricao" ] );
				break;
		}
	}

	/**
	* Método sem função útil, apenas existe por requisito do parser XML do PHP.
	*/
	function elemento_final( $parser, $nome ) {
	}

	/**
	* Analisa os dados contidos dentre de uma tag XML (não os atributos junto com uma
	* tag, sim os seus CDATA.
	*/
	function dados_elemento( $xmlparser, $dado ) {
		switch ( $this->ultima_tag ) {
			case "nome":
				if ( is_null( $this->nome) ) {
					$this->nome = $dado;
				}
				break;
			case "descricao":
				if ( is_null( $this->descricao) ) {
					$this->descricao = $dado;
				}
				break;
			case "enunciado":
				if ( is_null( $this->enunciado) ) {
					$this->enunciado = $dado;
				}
				break;
		}
	}

	/**
	* Construtor de um trabalho. Como parâmetro recebe o nome do arquivo com o documento XML
	* contendo os dados do trabalho. O caminho para este arquivo não deve ser fornecido, sempre
	* deve estar dentro do diretório REPOSITÓRIO definido em config.php.
	*/
	function Trabalho( $arquivo ) {
		$xml_parser = xml_parser_create();
		xml_set_object( $xml_parser, $this );
		xml_set_element_handler( $xml_parser, "elemento_inicial", "elemento_final" );
		xml_set_character_data_handler( $xml_parser, "dados_elemento" );
		xml_parser_set_option( $xml_parser,XML_OPTION_CASE_FOLDING, false );
		
		$fp = fopen( $arquivo, "r" );
		while ( $data = fread( $fp, 4096 ) ) {
			if ( !( xml_parse( $xml_parser, $data, feof( $fp ) ) ) ) {
				echo xml_error_string( xml_get_error_code( $xml_parser ) ) . " at line number " . xml_get_current_line_number( $xml_parser ) . ".";
			}
		}
		xml_parser_free( $xml_parser );
	}

	/**
	* Calcula a nota do trabalho.
	*/
	function calcular_nota( $criterios_trabalho_corrigido ) {
		$nota = 0;

		reset( $this->exercicios );
		while ( $exercicio = current( $this->exercicios ) ) {
			$nota += $exercicio->calcular_nota( $criterios_trabalho_corrigido );
			next( $this->exercicios );
		}
		return $nota;
	}

	function converter_para_csv() {
		$csv = $this->id;
		$csv .= "," . $this->data_entrega;
		$csv .= "," . $this->diretorio_base;
		$csv .= "," . $this->nome;
		$csv .= "," . $this->descricao;
		$csv .= "," . $this->enunciado;

		$csv .= "\n";
		reset( $this->exercicios );
		while ( $exercicio =& current( $this->exercicios ) ) {
			$csv .= "\t" . $exercicio->converter_para_csv() . "\n";
			next( $this->exercicios );
		}

		return $csv;
	}

	function adicionar_exercicio( $id, $valor ) {
		$this->exercicios[ $id ] =& new Exercicio( $id, $valor );
	}

	function remover_exercicio( $id, $valor ) {
		unset( $this->exercicios[ $id ] );
	}

	function &pegar_exercicio( $id ) {
		$exercicio = $this->exercicios[ $id ];
		return $this->exercicios[ $id ];
	}

	function quantidade_exercicios() {
		return sizeof( $this->exercicios );
	}

	function quantidade_criterios() {
		$quantidade = 0;
		reset( $this->exercicios );
		while ( $exercicio = current( $this->exercicios ) ) {
			$quantidade += $exercicio->quantidade_criterios();
			next( $this->exercicios );
		}
		return $quantidade;
	}

	function nota_maxima() {
		$nota = 0;
		reset( $this->exercicios );
		while ( $exercicio = current( $this->exercicios ) ) {
			$nota += $exercicio->valor;
			next( $this->exercicios );
		}
		return $nota;
	}
}
?>
