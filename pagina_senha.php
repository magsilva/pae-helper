<?php 
	if ( USAR_CONEXAO_SEGURA && ! $_SERVER[ "HTTPS" ] ) {
		ob_start();
		header( "Location: https://" . $_SERVER["HTTP_HOST"] . " /" . $_SERVER["PHP_SELF"] ); 
		exit;
	} 

	require( "classe.php" );
	define( "MUTEX_ID", 12345 );
	define( "MUTEX_VALUE", 1 );
	define( "MUTEX_PERM", 0700 );
?>

<!DOCTYPE html PUBLIC "-//IETF//DTD XHTML 1.1//EN">

<html>

<head>
	<title>Altera��o de senha - <?php echo DISCIPLINA ?></title>
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
	<style type="text/css">
		dd { margin-left: 2em }
	</style>
</head>

<body>

<?php
if ( $_REQUEST[ "$numero_usp" ] ) {
	$mutex = sem_get( MUTEX_ID, MUTEX_VALUE, MUTEX_PERM );
	sem_acquire( $mutex );

	$classe =& new Classe( BASE_DADOS );
	if ( $_REQUEST[ "senha_antiga" ] || $_REQUEST[ "senha_nova" ] || $_REQUEST[ "senha_nova_conferida" ] || $_REQUEST[ "email " ] ) {
		if ( $classe->possui_aluno( $_REQUEST[ "numero_usp" ] ) ) {
			$aluno =& $classe->pegar_aluno( $_REQUEST[ "numero_usp" ], $_REQUEST[ "senha_antiga" ] );
			if ( ! is_null( $aluno ) ) {
				if ( $_REQUEST[ "senha_nova" ] == $_REQUEST[ "senha_nova_conferida" ] ) {
					$aluno->alterar_senha( $_REQUEST[ "senha_nova" ] );
					echo "Senha alterada.\n";
					if ( $email ) {
						$aluno->alterar_email( $_REQUEST[ "email" ] );
						echo "Email alterado para $alunos->email.\n";
					} else {
						echo "Email inalterado.";
					}
					$classe->salvar();
				} else {
					echo "A senha nova e sua repeti��o n�o confere. Por favor, tente novamente.\n";
				}
			} else {
				echo "Senha incorreta. Por favor, tente novamente.\n";
			}
		} else {
			echo "N�mero USP incorreto ou aluno n�o matriculado na disciplina. Por favor, tente novamente.\n";
		}
	} else {
		$classe->enviar_nova_senha( $_REQUEST[ "numero_usp" ] );
		$classe->salvar();
		echo "Uma nova senha foi gerada e enviada para o seu email.\n";
	}
	sem_release( $mutex );
} else {
?>


<h1 id="alterar">Altera��o de senha</h1>
<hr />

<p>Digito seu n�mero USP, email, senha antiga e senha nova. Todo usu�rio novo possui a senha "teste123". Caso tenha esquecido sua senha anterior, consulte a se��o <a href="#recuperar">Recupera��o de senha</a>. Informe tamb�m o seu endere�o de email (ele ser� utilizado para possibilitar a recupera��o de sua senha, se isto for necess�rio).</p>

<form name="alterar_senha" enctype="multipart/form-data" method="post" action="<? echo $_SERVER["PHP_SELF"] ?>">
<dl>
	<br /><label for="numero_usp">N�mero USP</label>
	<dd><input type="text" name="numero_usp" size="10" id="numero_usp" /></dd>
	<br /><label for="senha_antiga">Senha antiga</label>
	<dd><input type="password" name="senha_antiga" maxlength="10" id="senha_antiga" /></dd>
<br /><label for="senha">Senha nova</label>
	<dd><input type="password" name="senha_nova" maxlength="10" id="senha_nova" /></dd>
	<br /><label for="senha">Senha nova (novamente, para conferir)</label>
	<dd><input type="password" name="senha_nova_conferida" maxlength="10" id="senha_nova_conferida" /></dd>
	<br /><label for="email">Email</label>
	<dd><input type="text" name="email" size="60" id="email" /></dd>
	<br />
</dl>
<br /><input type="submit" name="enviar" value="Enviar" />
</form>

<hr />	
<h1 id="recuperar">Recupera��o de senha</h1>

<p>Caso tenha esquecido sua senha, informe seu n�mero USP. Uma senha nova ser� gerada e enviada para o seu email (informado quando alterada a senha pela primeira vez). Caso este processo n�o funciona, entre <A HREF="mailto:<?php echo MONITOR ?>">em contato com o estagi�rio da disciplina</a>.</p>

<form name="recuperar_senha" enctype="multipart/form-data" method="post" action="<? echo $_SERVER["PHP_SELF"] ?>">
<dl>
	<br /><label for="numero_usp">N�mero USP</label>
	<dd><input type="text" name="numero_usp" size="10" id="numero_usp" /></dd>
</dl>
<br /><input type="submit" name="enviar" value="Enviar" />
</form>

<?php
}
?>

</body>

</html>
