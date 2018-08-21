<?php
 $file = "/code/tasks/alarm/alarm-table.json";
 if(!file_exists($file)) die("I'm sorry, the file doesn't seem to exist.");

 $type = filetype($file);
 // Get a date and timestamp
 $today = date("F j, Y, g:i a");
 $time = time();
 // Send file headers
 header("Content-type: $type");
 header("Content-Disposition: attachment;filename=alarm-table.json");
 header("Content-Transfer-Encoding: binary"); 
 header('Pragma: no-cache'); 
 header('Expires: 0');
 // Send the file contents.
 set_time_limit(0); 
 readfile($file)

?>