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
		$nome_completo = $nome_diretorio . "/" . $arquivo;
  	if ( is_dir( $nome_completo ) ) {
			if ( $arquivo != "." && $arquivo != ".."  ) {
				chmod( $nome_completo, $permissao_diretorio );
				alterar_permissao( $nome_completo, $expressao_regular, $permissao_arquivo, $permissao_diretorio );
			}
		} else {
			if ( ereg( $expressao_regular, $arquivo ) ) {
				chmod( $nome_completo, $permissao_arquivo );
			}
 		}
	}
}

if ( !is_dir( REPOSITORIO ) ) {
	mkdir( REPOSITORIO );
}

if ( !is_file( BASE_DADOS ) ) {
	touch( BASE_DADOS );
}

alterar_permissao( ".", "^[a-zA-Z]", 0440, 0755 );
alterar_permissao( REPOSITORIO, "^tr", 0440, 0755 );
chmod( BASE_DADOS, 0755 );

?>
