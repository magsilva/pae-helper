<?php

/**
* Configura as permissões de acesso aos arquivos vitais do sistema.
*/
require_once( "config.php" );

/**
* Altera todos os arquivos para somente leitura ao dono e grupo.
* Parâmetros: string, string, inteiro (octal), inteiro (octal).
*/
function alterar_permissao( $nome_diretorio, $expressao_regular, $permissao_arquivo, $permissao_diretorio ) {
	$diretorio = opendir( $nome_diretorio );
  while ( false !== ( $arquivo = readdir( $diretorio ) ) ) {
  	if ( is_dir( $nome_diretorio . "/" . $arquivo ) {
			if ( $arquivo != "." && $arquivo != ".."  ) {
				chmod( $arquivo, $permissao_diretorio );
				alterar_permissao( $arquivo, $expressao_regular, $permissao_arquivo, $permissao_diretorio );
			}
		} else {
			if ( ereg( $expressao_regular, $arquivo ) ) {
				chmod( $arquivo, $permissao_arquivo );
			}
 		}
	}
}

alterar_permissao( ".", "", 0440, 0755 );
alterar_permissao( REPOSITORIO, "", 0440, 0755 );

?>
