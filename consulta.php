<?php
	require( "config.php" );
	require( "trabalho.php" );
	require( "classe.php" );

	$arquivo = REPOSITORIO . "/" . $_REQUEST[ "id" ] . ".xml";
	if ( !file_exists( $arquivo ) ) {
		exit();
	}

	$trabalho =& new Trabalho( $arquivo );
?>

<head>
	<title><?php echo DISCIPLINA . " - " . $trabalho->nome . " - Notas" ?></title>
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head>

<body>

<h1><?php echo $trabalho->nome ?> - Notas</h1>

<br />
<hr />

<table border=1 cellpadding=3 cellspacing=0>
	<tr>
		<th>Número USP</th>
		<th>Nome</th>
		<th>Trabalho</th>
		<th>Nota</th>
		<th>Nota Arredondada</th>
	</tr>

<?php
	$classe =& new Classe( BASE_DADOS );
	$alunos =& $classe->alunos;
	reset( $alunos );
	$i = 0;
	while ( $aluno = &current( $alunos ) ) {
		echo "\n\t";

		// Melhora a visualização da tabela, intercalando linhas em branco com linhas coloridas.
		if ( ( $i % 2 ) != 0 ) {
			echo '<tr bgcolor="#DDDDDD">';
		}	else {
			echo '<tr>';
		}

		// Os dados do aluno propriamente dito.
		echo "\n\t\t<td align=\"center\">$aluno->numero_usp</td>";
		echo "\n\t\t<td><a href=\"mailto:$aluno->email\">$aluno->nome</a></td>";
		echo "\n\t\t<td align=\"center\">";
		if ( $aluno->pegar_trabalho( $trabalho ) != -1 ) {
			echo "<a href=\"" . $aluno->pegar_trabalho( $trabalho ) . "\"><img border=\"0\" src=disk.gif></a>";
		}
		echo "</td>";
		
		// Notas menores que 5 são escritas em vermelho
		echo "\n\t\t<td align=\"center\">";
		$nota = $aluno->calcular_nota( $trabalho );
		if ( $nota < NOTA_MINIMA ) {
			echo "<font color=\"#FF0000\">$nota</font>";
		} else {
			echo "$nota";
		}
		echo "</td>";


		// Notas menores que 5 são escritas em vermelho
		echo "\n\t\t<td align=\"center\">";
		$nota = $aluno->calcular_nota_arredondada( $trabalho );
		if ( $nota < NOTA_MINIMA ) {
			echo "<font color=\"#FF0000\">$nota</font>";
		} else {
			echo "$nota";
		}
		echo "</td>";
		echo "\n\t</tr>";

		$i++;
		next( $alunos );
	}
?>

</table>

</body>
