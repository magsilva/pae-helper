<?php

require( "classe.php" );

$poo012003 = new Classe( "alunos2.txt");
echo $poo012003->converter_para_csv();
$poo012003->adicionar_aluno( 0, "Marco Aurélio Graciotto Silva", "magsilva@icmc.usp.br", "teste123" );
$poo012003->adicionar_aluno( 1, "Aurélio Graciotto Silva", "msilva@icmc.usp.br", "teste234" );
$poo012003->adicionar_aluno( 200, "Graciotto Silva", "mags@icmc.usp.br", "teste567" );
$poo012003->adicionar_aluno( 9200, "Silva", "marco@icmc.usp.br", "teste890" );
$poo012003->adicionar_aluno( 99200, "Aurélio Graciotto", "marcoaurelio@icmc.usp.br", "tes123" );
$poo012003->adicionar_aluno( 799200, "Marco Silva", "underline@icmc.usp.br", "tes234" );
echo $poo012003->converter_para_csv();

$teste =& $poo012003->pegar_aluno( 9200, "teste890" );
echo "\n\n\t" . $teste->converter_para_csv() . "\n\n";

echo $poo012003->converter_para_csv();


$poo012003->salvar();


$teste = $poo012003->pegar_aluno( 9200, "teste890" );
$teste->converter_para_csv();

$poo012003->remover_aluno( 1 );
$poo012003->converter_para_csv();
$poo012003->remover_aluno( 0 );
$poo012003->converter_para_csv();
$poo012003->remover_aluno( 799200 );
$poo012003->converter_para_csv();
$poo012003->remover_aluno( 99200 );
$poo012003->converter_para_csv();


?>
