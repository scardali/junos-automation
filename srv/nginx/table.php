<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<!-- <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<link rel="stylesheet" href=" http://cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css">
<script src="http://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js"></script> -->
<!-- Use this for local development -->
<script src="js/jquery.min.js"></script>
<link rel="stylesheet" href="css/jquery.dataTables.min.css">
<script src="js/jquery.dataTables.min.js"></script>
<script src="js/main.js"></script>

</head>
<body>

    <table cellpadding="3" cellspacing="0" border="0" style="width: 67%; margin: 0 auto 2em auto;">
         <thead>
            <tr>
                <th>Target</th>
                <th>Search text</th>
                <th>Treat as regex</th>
                <th>Use smart search</th>
            </tr>
        </thead>
        <tbody id="searchbars"></tbody>
    </table>

    <div id="main_wrapper" style="text-align:center;">
        <table id="myTable" class="display" style="width:100%">
            <thead><tr id='table'></tr></thead>
        </table>
    </div>
    <div id='timestamp'><p></p></div>
    <button class="print-bt" type="button" onclick="" style="width:150px; line-height:2;">Download as CSV</button>
</body>
</html>
