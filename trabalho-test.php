<?php
require( "config.php" );
require( "trabalho.php" );
$a =& new Trabalho( "tr3.xml" );
echo $a->converter_para_csv();
?>
