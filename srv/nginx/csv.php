<?php 
$headers = array("switch","junos version");
$data = array("ex","junos-18");

$task = $_GET['task'];
$filename = "tasks/$task/parsed-data.csv";
$csvfile = fopen($filename,'w') or die("Unable to open file.");
for($i = 0; $i < count($headers)-1; $i++){
    fwrite($csvfile,$headers[$i]);
    fwrite($csvfile,",");
}
fwrite($csvfile,$headers[count($headers)-1]);
fwrite($csvfile,"\n")

?>