<?php
	require( "config.php" );
	require( "trabalho.php" );
	require_once( "checar.php" );
?>

<!DOCTYPE html PUBLIC "-//IETF//DTD XHTML 1.1//EN">

<html>

<head>
	<title>Programação Orientada a Objetos - Controle de Trabalhos</title>
</head>

<body>

<h1><?php echo DISCIPLINA; ?></h1>
<hr />

<h2>Controle de trabalhos</h2>
<dl>
<?php
	if ( !isdir( REPOSITORIO ) ) {
		echo "O sistema está indisponível temporariamente. Consulte o responsável pelo sistema.";
	}
	$diretorio = opendir( REPOSITORIO );
	while ( false !== ( $arquivo = readdir( $diretorio ) ) ) {
		if ( !is_dir( REPOSITORIO . "/" . $arquivo ) && ereg( "^tr",  $arquivo ) ) {
			$repositorio[] = $arquivo;
		}
	}
	sort( $repositorio );
	foreach ( $repositorio as $dados_trabalho ) {
		$trabalho =& new Trabalho( REPOSITORIO . "/" . $dados_trabalho );
		echo "\t<dt>$trabalho->nome</dt>";
		echo "<dd>Descrição: $trabalho->descricao</dd>";
		echo "<dd>Data de entraga: " . date( "d/n/Y G:i (T)", strtotime( $trabalho->data_entrega ) ) . "</dd>";
		echo "<dd>Operações possíveis: ";
		echo "<a href=\"consulta.php?id=" . $trabalho->id . "\"> [Consultar] </a>";
		echo "<a href=\"entrega.php?id=" . $trabalho->id . "\"> [Entregar] </a>";
		echo "</dd>";
		echo "<br />";
	}
?>
</dl>

<a href="geral.php">Resumo de todos os trabalhos, notas e médias</a>


<hr />
<h2>Controle de usuários</h2>
<dl>
	<li><a href="pagina_senha.php">Alterar senha/email ou gerar nova senha</a></li>
</dl>

<hr />

</body>

</html>
