<?php
	require_once( "header.php" );
	require_once( "config.php" );
	require_once( "trabalho.php" );
	require_once( "aluno.php" );
	require_once( "classe.php" );

	$arquivo = REPOSITORIO . "/" . $_REQUEST[ "id" ] . ".xml";
	if ( !file_exists( $arquivo ) ) {
		exit();
	}
	$trabalho =& new Trabalho( $arquivo );
?>

<head>
	<title><?php echo DISCIPLINA . " - " . $trabalho->nome ?> - Entrega de trabalho </title>
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
	<style type="text/css">
		dd { margin-left: 2em }
	</style>
</head>

<body>

<h1>Envio de Trabalhos</h1>

<?php
if ( time() > strtotime( $trabalho->data_entrega ) ) {
	echo strftime( "O prazo para enviar os trabalhos se esgotou (a data e horário limites eram, respectivamente, %e/%m/%G, horário %T. ", strtotime( $trabalho->data_entrega ) );
	echo strftime( "Agora, no servidor, a data é %e/%m/%G e o horário %T.", time() );
	echo "</body></html>";
	exit;
}

/**
* A tática é sempre pessimista: os erros tem o seu código de tratamento próxima a verificação de condição
* de existência do mesmo.
*/
if ( !$_REQUEST[ "numero_usp_lider" ] || !$_REQUEST[ "senha" ] || !is_uploaded_file( $_FILES['arquivo']['tmp_name'] ) ) {
	echo strftime( "O prazo para enviar os trabalhos é %e/%m/%G, horário %T. ", mktime( HORA, MINUTO , 0, MES, DIA, ANO ) );
	echo strftime( "Agora, no servidor, a data é %e/%m/%G e o horário %T.", time() );
} else {
	$classe =& new Classe( BASE_DADOS );
	$aluno =& $classe->pegar_aluno( $_REQUEST[ "numero_usp_lider" ], $_REQUEST[ "senha" ] );
	if ( is_null( $aluno ) ) {
		echo "Número USP ou senha incorreta. Por favor, tente novamente.";
	} else {
		echo "Gravando trabalho sob a responsabilidade de " . $_REQUEST[ "numero_usp_lider" ] . "...";
		if ( !$aluno->gravar_arquivo( $trabalho, $_FILES['arquivo']['tmp_name'] ) ) {
			echo "Erro no envio do arquivo. Por favor, tente novamente.";
		} else {
			echo "OK";
			$grupo_ok = TRUE;
			for ( $i = 1; $i < $trabalho->tamanho_grupo; $i++ ) {
				if ( $_REQUEST[ "numero_usp_$i" ] != NULL && $classe->possui_aluno( $_REQUEST[ "numero_usp_$i" ] ) ) {
					echo "<br />" . $_REQUEST[ "numero_usp_lider" ] . " responsabilizando-se por " . $_REQUEST[ "numero_usp_$i" ] . "...";
			
					$grupo_ok &= $aluno->responsabilizar_por( $trabalho, $_REQUEST[ "numero_usp_$i" ] );
					echo "OK";
				}
			}
			$subject = "Entrega de trabalho de DISCIPLINA";
			$message = "Trabalho recebido com sucesso ($numero_usp_lider)";

			if ( ! $grupo_ok ) {
				$message .= "\n\nATENÇÃO\nErro no recebimento de trabalho do grupo. Os componentes eram:";
				$message .= $_REQUEST[ "numero_usp_lider" ];
				$message .= " (líder)";
				for ( $i = 1; $i < $trabalho->tamanho_grupo; $i++ ) {
					if ( $_REQUEST[ "numero_usp_$i" ] != NULL ) {
						$message .= ", ";
						$message .= $_REQUEST[ "numero_usp_$i" ];
					}
				}
				$message .= ".";
			}
			$headers .= "From: " . MONITOR . ">\r\n";
			$headers .= "To: " . MONITOR . ">\r\n";
			ini_set( SMTP, "mail.icmc.usp.br" );
			mail( MONITOR, $subject, $message, $headers );
		}
	}
}
?>

<br />

<form name="envio_trabalho" enctype="multipart/form-data" method="post" action="<?php echo $_SERVER[ "PHP_SELF" ] . "?id=" . $_REQUEST[ "id" ] ?>">
	<dl>
	<br /><label for="numero_usp_lider">Número USP do líder do grupo</label>
	<dd><input type="text" name="numero_usp_lider" size="10" id="numero_usp_lider" /></dd>
<?php
	if ( $trabalho->tamanho_grupo > 1 ) {
?>
		<br />Número USP dos outros elementos do grupo:
<?php
		for ( $i = 1; $i < $trabalho->tamanho_grupo; $i++ ) {
			echo "<dd><input type=\"text\" name=\"numero_usp_$i\" size=\"10\" id=\"numero_usp_$i\" /></dd>";
		}
?>
	<br /><label for="senha">Senha do líder do grupo</label>
	<dd><input type="password" name="senha" maxlength="10" id="senha" /></dd>
	<br />
	<br /><label for="arquivo">Arquivo</label>
	<input type="hidden" name="MAX_FILE_SIZE" value=MAX_UPLOAD_SIZE />
	<dd><input type="file" name="arquivo" size="50" id="arquivo" /></dd>
	</dl>
	<br /><input type="submit" name="enviar" value="Enviar" /><input type="reset" name="limpar" value="Limpar" />
</form>
	
<?
	require_once( "footer.php" );
?>
