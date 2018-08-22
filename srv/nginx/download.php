<?php

 $file = "/code/tasks/alarm/alarm-table.json";
 $file = fopen('/code/tasks/alarm/alarm-table.json','r') or die("Unable to find file");
 $json = fread($file,filesize('/code/tasks/alarm/alarm-table.json'));
 fclose($file);
 var_dump(json_decode($json));



//  if(!file_exists($file)) die("I'm sorry, the file doesn't seem to exist.");
//  $type = filetype($file);

 // Send file headers
//  header("Content-type: $type");
//  header("Content-Disposition: attachment;filename=alarm-table.json");
//  header("Content-Transfer-Encoding: binary"); 
//  header('Pragma: no-cache'); 
//  header('Expires: 0');
//  // Send the file contents.
//  set_time_limit(0); 
//  readfile($file)

?>