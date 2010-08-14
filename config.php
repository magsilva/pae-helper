<?php

/**
* Disciplina a qual será feito o controle de trabalhos.
*/
define('DISCIPLINA', 'Programação Orientada a Objetos');

/**
* Email do monitor ou estagiário PAE da disciplina.
*/
define('MONITOR', 'magsilva@icmc.usp.br');

/**
* Diretório a ser utilizado como repositório dos trabalhos dos alunos.
*/
define('REPOSITORIO', 'example');

/**
* Arquivo contendo os dados sobre os alunos. O formato deste arquivo
* é CSV (comma separated values), contendo os seguintes dados sobre
* os alunos (nesta ordem): número USP, nome, senha, email.
*/
define('BASE_DADOS', 'example/alunos.txt');

/**
* Nota mínima dos trabalhos (normalmente é 50).
*/
define('NOTA_MINIMA', 50);


/**
* Habilita ou não a utilização de conexões seguras quando comunicando
* dados sensíveis do usuário.
*/
define('USAR_CONEXAO_SEGURA', true);

/**
* Critérios para "avaliação" dos trabalhos. Se criar novos critérios,
* acrescente aqui o respectivo nome de arquivo que o identificará.
*/
define('CORRECAO_V0', 'corrigido-v0.py');
define('CORRECAO_V1', 'corrigido-v1.py');
define('CORRECAO_V2', 'corrigido-v2.py');
define('CORRECAO_V3', 'corrigido-v3.py');
define('CORRECAO_V4', 'corrigido-v4.py');

?>
