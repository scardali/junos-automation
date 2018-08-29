<?php 

$command = escapeshellcmd('/code/ansible/run.py');
$output = shell_exec($command);

echo $output
?>