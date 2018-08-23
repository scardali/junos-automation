<?php 
$headers = array("switch","junos version");
$task = $_GET['task'];
$headerline = $_GET['headers'];
$filename = "tasks/$task/parsed-data.csv";
$csvfile = fopen($filename,'w') or die("Unable to open file.");
fwrite($csvfile,$headerline);
fwrite($csvfile,"\n");
$count = count(explode('&', $_SERVER['QUERY_STRING']));
$count -= 3;
for($i = 0; $i < $count; $i++){
    $var = sprintf("d%d",$i);
    $data = $_GET[$var];
    fwrite($csvfile,$data);
    fwrite($csvfile,"\n");
}

fclose($csvfile);
?>