<?php

require_once( "criterio.php" );

class Exercicio {
	var
		$id,		// Identificar único do exercício.
		$valor,		// Valor do exercício (nota absoluta).
		$criterios;	// Critérios a serem atendidos para obtenção da nota.

	/**
	* O exercício sempre contém um identificador e seu valor. Os critérios serão
	* posteriormente adicionados.
	*/
	function Exercicio( $id, $valor ) {
		$this->id = $id;
		$this->valor = $valor;
		$this->criterios = array();
	}

	/**
	* Calcula a nota que o aluno tirou no exercício com base nos critérios corrigidos
	* obtidos quando na correção do trabalho do aluno. Como sempre, assume-se sempre a nota
	* máxima e, a cada critério corrigido encontrado, diminui-se a nota do aluno, levando-se
	* em conta o peso do critério e a porcentagem errada do critério.
	*/
	function calcular_nota( $criterios_corrigidos ) {
		$nota = $this->valor;

		if ( is_null( $criterios_corrigidos ) ) {
			return 0;
		}

		$soma_pesos_criterios = 0;
		reset( $this->criterios );
		while ( $criterio = current( $this->criterios ) ) {
			$soma_pesos_criterios += $criterio->peso;
                        next( $this->criterios );
                }

		reset( $this->criterios );
		while ( $criterio = &current( $this->criterios ) ) {
			reset( $criterios_corrigidos );
			while ( $criterio_corrigido = &current( $criterios_corrigidos ) ) {
				if ( $criterio_corrigido->id_exercicio == $this->id && $criterio_corrigido->id_criterio == $criterio->id_criterio ) {
					$nota_criterio = $criterio->peso * $this->valor * ( $criterio_corrigido->porcentagem_errada / 100 );

					$nota -= $nota_criterio / $soma_pesos_criterios;
				}
				next( $criterios_corrigidos );
			} 
			next( $this->criterios );
		}
		return $nota;
	}

	/**
	* Adiciona um novo critério ao exercício. Os critérios devem sempre ser adicionados quando
	* na inicialização do sistema (não seria uma boa idéia avaliar alunos, cada qual com critérios
	* distintos.
	*/
	function adicionar_criterio( $id, $peso, $descricao ) {
		$criterio = new Criterio( $this->id, $id, 0, $peso, $descricao );
		$this->criterios[ $id ] =& $criterio;
	}

	/**
	* Exclui um critério do exercício. Normalmente este método nunca seria utilizado.
	*/
	function remover_criterio( $id ) {
		unset( $this->criterio[ $id ] );
	}

	function quantidade_criterios() {
		return sizeof( $this->criterios );
	}

	function clonar_criterios( $valor ) {
		$criterios_clonados = $this->criterios;
		reset( $criterios_clonados );
		while ( $criterio = current( $criterios_clonados ) ) {
			$criterio->porcentagem_errada = 100;
			next( $criterios_clonados );
		}
		return $criterios_clonados;
	}

	/**
	* Converte o exercício para um formato de fácil e rápida visualização. Utilizado principalmente
	* para uma depuração "de pobre".
	*/
	function converter_para_csv() {
		$csv = $this->id;
		$csv .= "," . $this->valor;

		$csv .= "\n";
		reset( $this->criterios );
		while ( $criterio =& current( $this->criterios ) ) {
			$csv .= "\t\t" . $criterio->converter_para_csv() . "\n";
			next( $this->criterios );
		}

		return $csv;
	}
}

?>
