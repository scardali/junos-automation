<?php 

$command = escapeshellcmd('hello.sh');
$output = shell_exec($command);
echo $output;
?>