<?php

/**
* Disciplina a qual ser� feito o controle de trabalhos.
*/
define('DISCIPLINA', 'Programa��o Orientada a Objetos');

/**
* Email do monitor ou estagi�rio PAE da disciplina.
*/
define('MONITOR', 'magsilva@icmc.usp.br');

/**
* Diret�rio a ser utilizado como reposit�rio dos trabalhos dos alunos.
*/
define('REPOSITORIO', 'example');

/**
* Arquivo contendo os dados sobre os alunos. O formato deste arquivo
* � CSV (comma separated values), contendo os seguintes dados sobre
* os alunos (nesta ordem): n�mero USP, nome, senha, email.
*/
define('BASE_DADOS', 'example/alunos.txt');

/**
* Nota m�nima dos trabalhos (normalmente � 50).
*/
define('NOTA_MINIMA', 50);


/**
* Habilita ou n�o a utiliza��o de conex�es seguras quando comunicando
* dados sens�veis do usu�rio.
*/
define('USAR_CONEXAO_SEGURA', true);

/**
* Crit�rios para "avalia��o" dos trabalhos. Se criar novos crit�rios,
* acrescente aqui o respectivo nome de arquivo que o identificar�.
*/
define('CORRECAO_V0', 'corrigido-v0.py');
define('CORRECAO_V1', 'corrigido-v1.py');
define('CORRECAO_V2', 'corrigido-v2.py');
define('CORRECAO_V3', 'corrigido-v3.py');
define('CORRECAO_V4', 'corrigido-v4.py');

?>
