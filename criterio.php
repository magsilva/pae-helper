<?php

/**
* Cada exerc�cio � avaliado com base em crit�rios bem estabelecidos. Cada crit�rio
* possui um identificador, um peso, uma descri��o e a porcentagem errada dele. Toda
* a corre��o � apontando os erros e, inicialmente, sempre assume-se que est� tudo
* correto.
*/
class Criterio {
	var
		$id_exercicio,		// Identificador do exerc�cio a que este crit�rio pertence (atributo
					// utilizado para facilitar o trabalho com crit�rios corrigidos).
		$id_criterio,		// Identificador �nico, em rela��o ao exerc�cio, do crit�rio.
		$peso,			// Peso do crit�rio.
		$descricao,		// Descri��o do crit�rio (para ajudar o estagi�rio quando o aluno
					// vier perguntar o que est� errado).
		$porcentagem_errada;	// A porcentagem da quest�o que est� incorreta. � um valor inteiro.


	/**
	* Inicializa um crit�rio. Sempre assume-se que um crit�rio est� atendido (correto)
	* (ou seja, o aluno � inocente at� que se prove o contr�rio - atrav�s da corre��o
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
