<?php
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
	echo strftime( "O prazo para enviar os trabalhos se esgotou (a data e hor�rio limites eram, respectivamente, %e/%m/%G, hor�rio %T. ", strtotime( $trabalho->data_entrega ) );
	echo strftime( "Agora, no servidor, a data � %e/%m/%G e o hor�rio %T.", time() );
	echo "</body></html>";
	exit;
}

if ( $_REQUEST[ "numero_usp_lider" ] && $_REQUEST[ "senha" ] && is_uploaded_file( $_FILES['arquivo']['tmp_name'] ) ) {
	$classe =& new Classe( BASE_DADOS );
	$aluno =& $classe->pegar_aluno( $_REQUEST[ "numero_usp_lider" ], $_REQUEST[ "senha" ] );
	if ( ! is_null( $aluno ) ) {
		echo "Gravando trabalho sob a responsabilidade de " . $_REQUEST[ "numero_usp_lider" ] . "...";
		if ( $aluno->gravar_arquivo( $trabalho, $_FILES['arquivo']['tmp_name'] ) ) {
			echo "OK";
			$grupo_ok = TRUE;
			if ( $_REQUEST[ "numero_usp_1" ] != NULL && $classe->possui_aluno( $_REQUEST[ "numero_usp_1" ] ) ) {
				echo "<br />" . $_REQUEST[ "numero_usp_lider" ] . " responsabilizando-se por " . $_REQUEST[ "numero_usp_1" ] . "...";
			
				$grupo_ok &= $aluno->responsabilizar_por( $trabalho, $_REQUEST[ "numero_usp_1" ] );
				echo "OK";
			}
			if ( $_REQUEST[ "numero_usp_2" ] != NULL && $classe->possui_aluno( $_REQUEST[ "numero_usp_2" ] ) ) {
				echo "<br />" . $_REQUEST[ "numero_usp_lider" ] . " responsabilizando-se por " . $_REQUEST[ "numero_usp_2" ] . "...";
				$grupo_ok &= $aluno->responsabilizar_por( $trabalho, $_REQUEST[ "numero_usp_2" ] );
				echo "OK";
			}
			$subject = "Entrega de trabalho de DISCIPLINA";
			$message = "Trabalho recebido com sucesso ($numero_usp_lider $numero_usp_1 $numero_usp_2.";

			if ( ! $grupo_ok ) {
				$message .= "\n\nATEN��O\nErro no recebimento de trabalho do grupo. O l�der era";
				$message .= $_REQUEST[ "numero_usp_lider" ];
				$message .= " e os outros elementos do grupo eram ";
				$message .= $_REQUEST[ "numero_usp_1" ];
				$message .= " e ";
				$message .= $_REQUEST[ "numero_usp_2" ];
			}
			$headers .= "From: " . MONITOR . ">\r\n";
			$headers .= "To: " . MONITOR . ">\r\n";
			ini_set( SMTP, "mail.icmc.usp.br" );
			mail( MONITOR, $subject, $message, $headers );
		} else {
			echo "Erro no envio do arquivo. Por favor, tente novamente.";
		}
	} else {
		echo "N�mero USP ou senha incorreta. Por favor, tente novamente.";
	}
} else {
	echo strftime( "O prazo para enviar os trabalhos � %e/%m/%G, hor�rio %T. ", mktime( HORA, MINUTO , 0, MES, DIA, ANO ) );
	echo strftime( "Agora, no servidor, a data � %e/%m/%G e o hor�rio %T.", time() );
?>

<br />

<form name="envio_trabalho" enctype="multipart/form-data" method="post" action="<?php echo $_SERVER[ "PHP_SELF" ] . "?id=" . $_REQUEST[ "id" ] ?>">
	<dl>
	<br /><label for="numero_usp_lider">N�mero USP do l�der do grupo</label>
	<dd><input type="text" name="numero_usp_lider" size="10" id="numero_usp_lider" /></dd>
	<br />N�mero USP dos outros elementos do grupo
	<dd><input type="text" name="numero_usp_1" size="10" id="numero_usp_1" /></dd>
	<dd><input type="text" name="numero_usp_2" size="10" id="numero_usp_2" /></dd>
	<br /><label for="senha">Senha do l�der do grupo</label>
	<dd><input type="password" name="senha" maxlength="10" id="senha" /></dd>
	<br />
	<br /><label for="arquivo">Arquivo</label>
	<input type="hidden" name="MAX_FILE_SIZE" value=MAX_UPLOAD_SIZE />
	<dd><input type="file" name="arquivo" size="50" id="arquivo" /></dd>
	</dl>
	<br /><input type="submit" name="enviar" value="Enviar" /><input type="reset" name="limpar" value="Limpar" />
</form>
	
<?php
}
?>
	
</body>
