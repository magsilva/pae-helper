<?php
	require_once( "config.php" );
	require_once( "trabalho.php" );
	require_once( "classe.php" );
?>

<!DOCTYPE html PUBLIC "-//IETF//DTD XHTML 1.1//EN">

<html>

<head>
	<title>Programação Orientada a Objetos - Resumo das notas</title>
</head>

<body>

<h1><?php echo DISCIPLINA; ?></h1>
<hr />

<h2>Notas dos trabalhos</h2>
<dl>
<?php
	$diretorio = opendir( REPOSITORIO );
	while ( false !== ( $arquivo = readdir( $diretorio ) ) ) {
		if ( !is_dir( REPOSITORIO . "/" . $arquivo ) && ereg( "^tr",  $arquivo ) ) {
			$repositorio[] = $arquivo;
		}
	}
	sort( $repositorio );
	$trabalhos = array();
	$classe =& new Classe( BASE_DADOS );
	$alunos =& $classe->alunos;

?>

<table>
<tr>
	<th>Número USP</th>
	<th>Nome</th>
<?php
	foreach ( $repositorio as $dados_trabalho ) {
		$trabalho =& new Trabalho( REPOSITORIO . "/" . $dados_trabalho );
		$trabalhos[] = $trabalho;
		echo "\t<th>$trabalho->nome</th>";
	}

?>
	<th>Média</th>
</tr>
<?
	$i = 0;
	foreach ( $alunos as $aluno ) {
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

		$media = 0;
		$menor_nota = 100;
		foreach ( $trabalhos as $trabalho ) {
			echo "\n\t\t<td align=\"center\">";
			$nota = $aluno->calcular_nota_arredondada( $trabalho );
			if ( $nota < $menor_nota ) {
				$menor_nota = $nota;
			}
			$media += $nota;
			// Notas menores que 5 são escritas em vermelho
			if ( $nota < NOTA_MINIMA ) {
				echo "<font color=\"#FF0000\">$nota</font>";
			} else {
				echo "$nota";
			}
			echo "</td>";
		}
	
		echo "\n\t\t<td align=\"center\">";
		$media = round( $media  / ( sizeof( $trabalhos ) - 1 ), 0);
		// Médias menores que 5 são escritas em vermelho
		if ( $media < NOTA_MINIMA ) {
			echo "<font color=\"#FF0000\">$media</font>";
		} else {
			echo "$media";
		}
		echo "\t</td>";
		echo "</tr>";
		$i++;
	}
?>

	
</table>

</body>

</html>
