<?php 
    $task = $_POST['task'];
    $headerline = $_POST['headers'];
    $filename = "tasks/$task/$task.csv";
    $csvfile = fopen($filename,'w') or die("Unable to open file.");
    fputcsv($csvfile,$headerline);

    foreach($_POST['data'] as $data)
        fputcsv($csvfile,$data);
    fclose($csvfile);
?>