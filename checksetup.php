#!/bin/php

/**
* Configura as permissões de acesso aos arquivos vitais do sistema.
*/

<?php
	require_once( "config.php" )

	// Altera todos os arquivos para somente leitura ao dono e grupo.
	foreach ( $file in . ) {
		chmod( "", 0440 );
	}

	// Coloca permissão de escrita no repositório.
	chmod( REPOSITORIO ,0775 );
	foreach ( $file.xml in REPOSITORIO ) {
		chmod( , 0440 );
	}
	foreach ( $diretorio in REPOSITORIO ) {
		chmod( $diretorio ,0775 );
	}
?>
