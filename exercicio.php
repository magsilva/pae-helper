<?php

require_once( "criterio.php" );

class Exercicio {
	var
		$id,		// Identificar �nico do exerc�cio.
		$valor,		// Valor do exerc�cio (nota absoluta).
		$criterios;	// Crit�rios a serem atendidos para obten��o da nota.

	/**
	* O exerc�cio sempre cont�m um identificador e seu valor. Os crit�rios ser�o
	* posteriormente adicionados.
	*/
	function Exercicio( $id, $valor ) {
		$this->id = $id;
		$this->valor = $valor;
		$this->criterios = array();
	}

	/**
	* Calcula a nota que o aluno tirou no exerc�cio com base nos crit�rios corrigidos
	* obtidos quando na corre��o do trabalho do aluno. Como sempre, assume-se sempre a nota
	* m�xima e, a cada crit�rio corrigido encontrado, diminui-se a nota do aluno, levando-se
	* em conta o peso do crit�rio e a porcentagem errada do crit�rio.
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
	* Adiciona um novo crit�rio ao exerc�cio. Os crit�rios devem sempre ser adicionados quando
	* na inicializa��o do sistema (n�o seria uma boa id�ia avaliar alunos, cada qual com crit�rios
	* distintos.
	*/
	function adicionar_criterio( $id, $peso, $descricao ) {
		$criterio = new Criterio( $this->id, $id, 0, $peso, $descricao );
		$this->criterios[ $id ] =& $criterio;
	}

	/**
	* Exclui um crit�rio do exerc�cio. Normalmente este m�todo nunca seria utilizado.
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
	* Converte o exerc�cio para um formato de f�cil e r�pida visualiza��o. Utilizado principalmente
	* para uma depura��o "de pobre".
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
