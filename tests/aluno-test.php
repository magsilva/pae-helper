<?php

require( "aluno.php" );
require( "config.php" );


$aluno1 = new Aluno( 4799200, "Marco Aurélio Graciotto Silva", "magsilva@icmc.usp.br", "teste123" );
$aluno2 = new Aluno( 4799201, "Marco Aurélio Graciotto Silva", "magsilva@icmc.usp.br", "teste123" );

echo "\n" . $aluno1->pegar_trabalho();
$aluno1->autenticar( "teste123" );
echo $aluno1->converter_para_csv() . "\n";
if ( $aluno1->gravar_arquivo( BASE_DADOS ) ) {
	$aluno1->responsabilizar_por( 25252 );
}
echo "\n" . $aluno1->pegar_trabalho();


echo "\n" . $aluno2->pegar_trabalho();
$aluno2->autenticar( "teste123" );
echo $aluno2->converter_para_csv() . "\n";
if ( $aluno2->gravar_arquivo( BASE_DADOS ) ) {
	$aluno2->responsabilizar_por( 4799200 );
	$aluno2->responsabilizar_por( 25252 );
}
echo "\n" . $aluno2->pegar_trabalho();



echo "\n";
?>
