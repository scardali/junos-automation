<?php
    echo date("Y-m-d H:i:s", substr(filectime($_GET['file']), 0, 10));
?>