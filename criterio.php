<?php

/**
* Cada exercício é avaliado com base em critérios bem estabelecidos. Cada critério
* possui um identificador, um peso, uma descrição e a porcentagem errada dele. Toda
* a correção é apontando os erros e, inicialmente, sempre assume-se que está tudo
* correto.
*/
class Criterio {
	var
		$id_exercicio,		// Identificador do exercício a que este critério pertence (atributo
					// utilizado para facilitar o trabalho com critérios corrigidos).
		$id_criterio,		// Identificador único, em relação ao exercício, do critério.
		$peso,			// Peso do critério.
		$descricao,		// Descrição do critério (para ajudar o estagiário quando o aluno
					// vier perguntar o que está errado).
		$porcentagem_errada;	// A porcentagem da questão que está incorreta. É um valor inteiro.


	/**
	* Inicializa um critério. Sempre assume-se que um critério está atendido (correto)
	* (ou seja, o aluno é inocente até que se prove o contrário - através da correção
	* do trabalho).
	*/
	function Criterio( $id_exercicio, $id_criterio, $porcentagem_errada, $peso, $descricao ) {
		$this->id_exercicio = $id_exercicio;
		$this->id_criterio= $id_criterio;
		$this->peso = $peso;
		$this->descricao = $descricao;
		$this->porcentagem_errada = $porcentagem_errada;
	}

	/**
	* Debug de pobre. Converte para o formato CSV.
	*/
	function converter_para_csv() {
		$csv = $this->id_exercicio;
		$csv .= "," . $this->id_criterio;
		$csv .= "," . $this->peso;
		$csv .= "," . $this->descricao;
		$csv .= "," . $this->porcentagem_errada;
		return $csv;
	}
}

?>
