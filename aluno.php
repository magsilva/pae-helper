<?php

require_once( "config.php" );
require_once( "criterio.php" );

/**
* Class que controla todas as opera��es que afetam um aluno.
*
* A senha do aluno � texto limpo. Caso queira utilizar um hash ou alguma t�cnica
* aprimorada para armazen�-la, crie uma nova classe (herdando esta) e sobrescreva
* o m�todo autenticar().
*/
class Aluno {
	var $nome,
			$senha,
			$numero_usp,
			$email,
			$autenticado; // Indica se o usu�rio j� se autenticou.

	/**
	* Cria um novo aluno.
	*/
	function Aluno( $numero_usp, $nome, $email, $senha ) {
		$this->numero_usp = $numero_usp;
		$this->nome = $nome;
		$this->email = $email;
		$this->senha = $senha;
		$this->autenticado = FALSE;
	}

	/**
	* Autentica o aluno (autentica��o simples, compara��o de texto limpo).
	* O processo de autentica��o invalida a autentica��o feita anteriormente
	* automaticamente (por exemplo, se eu j� estiver autenticado e tentar me
	* autenticar novamente, seria como se eu nunca tive me autenticado antes).
	*/
	function autenticar( $senha ) {
		$this->autenticado = FALSE;
		if ( $this->senha == $senha ) {
			$this->autenticado = TRUE;
		}
		return $this->autenticado;
	}

	/**
	* Altera a senha do aluno. Pr�-requisito para efetuar a altera��o � estar autenticado.
	*/
	function alterar_senha( $senha ) {
		if ( $this->autenticado == FALSE ) {
			return false;
		}

		$this->senha = $senha;
		return TRUE;
	}

	function criar_senha() {
		$this->autenticado = FALSE;
		unset( $this->senha );
		$tamanho_senha = 7;
		$caracteres = "abcdefghijklmnopqrstuvwxyz0123456789";
		for ( $i = 0; $i <= $tamanho_senha; $i++ ) {
			$this->senha .= $caracteres[ rand( 0, strlen( $caracteres ) ) ];
     		}

		$mensagem = "$this->nome,\n\nA sua nova senha de POO � $this->senha.";
		mail( $this->email, DISCIPLINA . " - Nova senha", $message, "From: " . MONITOR );
		return $this->senha;
	}

	function alterar_email( $email ) {
		$this->email = $email;
	}

	/**
	* Retorna uma string com os dados essenciais do aluno separados por v�rgulas.
	*/
	function converter_para_csv() {
		return $this->numero_usp . "," . $this->nome . "," . $this->senha . "," . $this->email;
	}

	/**
	* Procura o �ltimo arquivo enviado.
	*/
	function pegar_ultimo_arquivo( $trabalho ) {
		$ultimo_arquivo = -1;

		// Se o diret�rio n�o existe, nenhum arquivo foi gravado.
		$nome_diretorio = $trabalho->diretorio_base . "/" . $this->numero_usp;
		if ( !is_dir( $nome_diretorio ) ) {
			return -1;
		}

		$diretorio = opendir( $nome_diretorio );

		while ( false !== ( $arquivo_destino = readdir( $diretorio ) ) ) {
			if ( is_file( $nome_diretorio . "/". $arquivo_destino ) ) {
				$arquivo_destino = strtok( $arquivo_destino, "." );
				if ( $ultimo_arquivo < intval( $arquivo_destino ) ) {
					$ultimo_arquivo = intval( $arquivo_destino );
				}
			}
		}
		closedir( $diretorio );
		return $ultimo_arquivo;
	}

	/*
	* Realiza a c�pia do arquivo na pasta deste script
	*/
	function gravar_arquivo( $trabalho, $arquivo_origem ) {
		// O aluno deve estar autenticado e o arquivo deve existir.
		if ( !$this->autenticado || !is_file( $arquivo_origem ) ) {
			return FALSE;
		}

		$diretorio = $trabalho->diretorio_base . "/" . $this->numero_usp;

		/*
		* Se o aluno tentou enviar o arquivo diretamente e participava de um grupo,
		* retornar erro. O aluno deve entrar em contato com o professor.
		*/
		if ( file_exists( $diretorio ) && is_link( $diretorio ) ) {
			return FALSE;
		}

		/**
		* Cria o diret�rio do aluno (se n�o existir).
		*/
		if ( !is_dir( $diretorio ) ) {
			if ( !mkdir( $diretorio, 0750 ) ) {
				return FALSE;
			}
		}

		$ultimo_arquivo = $this->pegar_ultimo_arquivo( $trabalho );

		/*
		* Prepara a cria��o do novo arquivo.
		*/
		$ultimo_arquivo++;
		$arquivo_destino = $diretorio . "/" . $ultimo_arquivo;

		/*
		* Finalmente armazena o arquivo enviado no diret�rio definitivo.
		*/
		if ( copy( $arquivo_origem, $arquivo_destino ) ) {
 			chmod( $arquivo_destino, 0440 );
			return TRUE;
		} else {
			return FALSE;
		}
	}

	/**
	* Retorna o nome do arquivo do �ltimo trabalho entregue.
	*/
	function pegar_trabalho( $trabalho ) {
		$ultimo_arquivo = $this->pegar_ultimo_arquivo( $trabalho );
		if ( $ultimo_arquivo == -1 ) {
			return -1;
		}

		$arquivo = $trabalho->diretorio_base . "/" . $this->numero_usp . "/" . $ultimo_arquivo;
		return $arquivo;
	}

	/**
	* Cria uma liga��o para outro elemento do grupo.
	*/
	function responsabilizar_por( $trabalho, $numero_usp ) {
		if ( is_dir( $trabalho->diretorio_base . "/" . $numero_usp ) ||
			!is_dir( $trabalho->diretorio_base . "/" . $this->numero_usp ) ) {
			return FALSE;
		} else {
			symlink( $this->numero_usp, $trabalho->diretorio_base . "/" . $numero_usp );
			return TRUE;
		}
	}

	/**
	* Calcula e retorna a nota do aluno.
	*/
	function &corrigir_trabalho( $trabalho ) {
		$diretorio = $trabalho->diretorio_base . "/" . $this->numero_usp . "/";
		$criterios = array();

		/**
		* CORRECAO_V0 � utilizado quando � feita uma corre��o em papel, com crit�rios determinados
		* fora do escopo deste programa.
		*
		* Neste modo, o arquivo cont�m apenas a nota que o trabalho recebeu.
		*/
		if ( file_exists( $diretorio . CORRECAO_V0 ) ) {
			$arquivo = fopen( $diretorio . CORRECAO_V0, "r" );
			$linha = fgets( $arquivo);
			$id_exercicio = strval( 1 );
			$id_criterio = strval( 1 );
			$porcentagem_errada = 100 - intval( $linha );
			$criterios[] =& new Criterio( $id_exercicio, $id_criterio, $porcentagem_errada, 0, "" );
			fclose( $arquivo );
			return $criterios;
		}

		/**
		* O formato CORRECAO_V1 consiste em:
		*	"#" "ERRO" ( "TOTAL"|"PARCIAL" ) EXERCICIO DESCRICAO
		* O exercicio est� no formato 'exercicio "." criterio ":"'.
		*
		* Este crit�rio � mantido apenas por compatibilidade, ele � anterior a utiliza��o de crit�rio,
		* isto � apenas uma adapta��o para aproveitar o material anteriormente corrigido.
		*/
		if ( file_exists( $diretorio . CORRECAO_V1 ) ) {
			$porcentagem_errada = 0;
			$valor_exercicio_parcial = 50; // Somente um n�mero qualquer.
			$arquivo = fopen( $diretorio . CORRECAO_V1, "r" );
			while ( !feof( $arquivo ) ) {
				$linha = fgets( $arquivo);
				if ( $linha[ 0 ] == "#" ) {
					$palavras = explode(" ", $linha);
					$token_erro = trim( $palavras[ 1 ] );
					if ( $token_erro == "ERRO" ) {
						$tipo_erro = trim( $palavras[ 2 ] );
						$exercicio_token = trim( $palavras[ 3 ], " :" );
						$exercicio_token_temp = explode( ".", $exercicio_token );
						$id_exercicio = trim( $exercicio_token_temp[ 0 ] );
						$id_criterio = trim( $exercicio_token_temp[ 1 ] );
						$explicacao = trim( $palavras[ 4 ] );
						if ( $tipo_erro == "TOTAL" ) {
							$porcentagem_errada = 100;
						} else {
							$porcentagem_errada = $valor_exercicio_parcial;
						}
						$criterios[] =& new Criterio( $id_exercicio, $id_criterio, $porcentagem_errada, 0, "" );
					}
				}
			}
			fclose( $arquivo );
			return $criterios;
		}

		/**
		* O novo formato para corre��o de programa Python, CORRECAO_V2, � estruturado como:
		* 	"#" "ERRO" EXERCICIO CRITERIO
		* Um crit�rio s� pode ser atendido totalmente neste sistema.
		*/
		if ( file_exists( $diretorio . CORRECAO_V2 ) ) {
			$arquivo = fopen( $diretorio . CORRECAO_V2, "r" );
			while ( !feof( $arquivo ) ) {
				$linha = fgets( $arquivo);
				if ( $linha[ 0 ] == "#" ) {
					$palavras = explode(" ", $linha);
					$token_erro = trim( $palavras[ 1 ] );
					if ( $token_erro == "ERRO" ) {
						$id_exercicio = trim( $palavras[ 2 ] );
						$id_criterio = trim( $palavras[ 3 ] );
						$criterios[] =& new Criterio( $id_exercicio, $id_criterio, 100, 0, "" );
					}
				}
			}
			fclose( $arquivo );
			return $criterios;
		}


		/**
		* O novo formato para corre��o de programa Python, CORRECAO_PYTHON_V3, � estruturado como:
		* 	"#" "ERRO" ( "TOTAL" | "PARCIAL" ) EXERCICIO CRITERIO 
		* Um crit�rio s� pode ser atendido totalmente neste sistema.
		*/
		if ( file_exists( $diretorio . CORRECAO_V3 ) ) {
			$arquivo = fopen( $diretorio . CORRECAO_V3, "r" );
			while ( !feof( $arquivo ) ) {
				$linha = fgets( $arquivo);
				if ( $linha[ 0 ] == "#" ) {
					$palavras = explode(" ", $linha);
					$token_erro = trim( $palavras[ 1 ] );
					if ( $token_erro == "ERRO" ) {
						$id_exercicio = trim( $palavras[ 3 ] );
						$id_criterio = trim( $palavras[ 4 ] );
						$tipo_erro = trim( $palavras[ 2 ] );
						if ( $tipo_erro == "TOTAL" ) {
							$porcentagem_errada = 100;
						} else {
							$porcentagem_errada = 50;
						}
						$criterios[] =& new Criterio( $id_exercicio, $id_criterio, $porcentagem_errada, 0, "" );
					}
				}
			}
			fclose( $arquivo );
			return $criterios;
		}

		/**
		* O novo formato para corre��o de programa Python, CORRECAO_PYTHON_V4, � estruturado como:
		* 	"#" "ERRO" EXERCICIO CRITERIO PORCENTAGEM
		* onde PORCENTAGEM � um valor de 0 a 100.
		* Um crit�rio s� pode ser atendido totalmente neste sistema.
		*/
		if ( file_exists( $diretorio . CORRECAO_V4 ) ) {
			$arquivo = fopen( $diretorio . CORRECAO_V4, "r" );
			while ( !feof( $arquivo ) ) {
				$linha = fgets( $arquivo);
				if ( $linha[ 0 ] == "#" ) {
					$palavras = explode(" ", $linha);
					$token_erro = trim( $palavras[ 1 ] );
					if ( $token_erro == "ERRO" ) {
						$id_exercicio = trim( $palavras[ 2 ] );
						$id_criterio = trim( $palavras[ 3 ] );
						$porcentagem_errada = intval( trim( $palavras[ 4 ] ) );
						$criterios[] =& new Criterio( $id_exercicio, $id_criterio, $porcentagem_errada, 0, "" );
					}
				}
			}
			fclose( $arquivo );
			return $criterios;
		}
	}

	function calcular_nota( $trabalho ) {
		$criterios =& $this->corrigir_trabalho( $trabalho );
		$nota = $trabalho->calcular_nota( $criterios );
		return round( $nota );
	}

	function calcular_nota_arredondada( $trabalho ) {
		$nota = $this->calcular_nota( $trabalho );

		$unidade = intval( $nota % 10 );
		$dezena = intval( $nota - $unidade );
		if ( $unidade < 5 && $unidade > 0 ) {
			$unidade = 5;
		}
		if ( $unidade > 5 ) {
			$dezena += 10;
			$unidade = 0;
		}
		$nota = $dezena + $unidade;
		if ( $nota > 100 ) {
			$nota = 100;
		}
		return $nota;
	}

}

?>
