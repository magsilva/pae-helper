<?php

require_once( "aluno.php" );


/**
* Classe que representa a classe real da disciplina, com seus respectivos alunos.
*/
class Classe {
	var $alunos,
		$nome_arquivo;

	/**
	* Cria uma instância da classe, usando o arquivo dado como argumento
	* para base de dados.
	*/
	function Classe( $nome_arquivo ) {
		$this->alunos = array();
		$this->nome_arquivo = $nome_arquivo;
		$this->carregar();
	}

	/**
	* Adiciona um aluno na classe.
	*
	* Se o aluno já existir, retorna 0. Caso contrário, retorna a senha gerada.
	*/ 
	function &adicionar_aluno( $numero_usp, $nome, $email, $senha_limpa ) {
		if ( is_null( $this->alunos[ $numero_usp ] ) ) {
			$senha = $senha_limpa;
			$aluno =& new Aluno( $numero_usp, $nome, $email, $senha );
			$this->alunos[ $numero_usp ] = $aluno;
			return $aluno;
		}
		return NULL;
	}

	/**
	* Remove o aluno da classe.
	*/
	function remover_aluno( $numero_usp ) {
		if ( ! is_null( $this->alunos[ $numero_usp ] ) ) {
			unset( $this->alunos[ $numero_usp ] );
		}
		return TRUE;
	}

	/**
	* Retorna um aluno da classe.
	*/
	function &pegar_aluno( $numero_usp, $senha ) {
		if ( is_null( $this->alunos[ $numero_usp ] ) ) {
			return NULL;
		}

		$aluno =& $this->alunos[ $numero_usp ];

		if ( $aluno->autenticar( $senha ) ) {
			return $aluno;
		} else {
			return NULL;
		}
	}

	function enviar_nova_senha( $numero_usp ) {
		if ( $this->possui_aluno( $numero_usp ) ) {
			$aluno =& $this->alunos[ $numero_usp ];
			return $aluno->criar_senha();
		}
		return FALSE;
	}

	/**
	  * Retorna os alunos da classe.
	  */
	function &pegar_alunos() {
		return $this->alunos;
	}


	/**
	* Verifica se possui o aluno em questão.
	*/
	function possui_aluno( $numero_usp ) {
		if ( is_null( $this->alunos[ $numero_usp ] ) ) {
			return FALSE;
		}
		return TRUE;
	}


	/**
	* Salva os dados da classe em arquivo.
	*/
	function salvar() {
		$arquivo = fopen( $this->nome_arquivo, "w" );
		if ( !$arquivo ) {
			return FALSE;
		}

		fwrite( $arquivo, $this->converter_para_csv() );

		fclose( $arquivo );

		return TRUE;
	}

	/**
	* Restaura os dados da classe a partir de arquivo.
	*/
	function carregar() {
		if ( ! is_file( $this->nome_arquivo ) ) {
			return FALSE;
		}

		$arquivo = fopen( $this->nome_arquivo, "r" );
		if ( !$arquivo ) {
			return FALSE;
		}

		while ( !feof( $arquivo ) ) {
			$linha = fscanf( $arquivo, "%[^,],%[^,],%[^,],%[^,\n]" );
			list( $numero_usp, $nome, $senha, $email ) = $linha;
			if ( is_numeric( $numero_usp ) ) {
				$aluno =& new Aluno( $numero_usp, $nome, $email, $senha );
	      			$this->alunos[ $numero_usp ] = $aluno;
			}
		}

		fclose( $arquivo );

		return TRUE;
	}

	/**
	* Converte os dados da classe para o formato CSV.
	*/
	function converter_para_csv() {
		$dump = "";
		reset( $this->alunos );
		while ( $aluno = &current( $this->alunos ) ) {
			$dump .= $aluno->converter_para_csv() . "\n";
			next( $this->alunos );
		}
		return $dump;
	}

}

?>
