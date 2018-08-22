<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<link rel="stylesheet" href="http://cdn.datatables.net/1.10.19/css/jquery.dataTables.min.css">
<script src="http://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js"></script>
<script type="text/javascript">
    function filterGlobal () {
        $('#myTable').DataTable().search(
            $('#global_filter').val(),
            $('#global_regex').prop('checked'),
            $('#global_smart').prop('checked')
        ).draw();
    }
    function filterColumn ( i ) {
        $('#myTable').DataTable().column( i ).search(
            $('#col'+i+'_filter').val(),
            $('#col'+i+'_regex').prop('checked'),
            $('#col'+i+'_smart').prop('checked')
        ).draw();
    }

    $(document).ready( function () {
        var task = <?php echo json_encode($_GET['task'], JSON_HEX_TAG); ?>;
        let filename = 'tasks/'+task+'/'+task+'-table.json';
        var csvfile = 'tasks/'+task+'/'+task+'.csv';
        var link = "<a href = " + csvfile + ">Download as CSV</a>";
        document.getElementById('csvlink').innerHTML = link;
        /**Render the page **/
        var headers;
        switch(task){
            case 'version':
                headers = ['Switch','Junos Version'];
                break;
            case 'vlan':
                headers = ['Switch','Vlan Name','Vxlan Name','Vlan Tag','Interface'];
                break;
            case 'commit':
                headers = ['Switch','Client','Sequence Number','User','Date/Time'];
                break;
            case 'interface':
                headers = ['Switch','Interface','Description','Operational Status','Admin Status','Address Family'];
                break;
            case 'alarm':
                headers = ['Switch','Alarm Class','Alarm Description','Alarm Time','Alarm Type'];
                break; 
            case 'ethernet':
                headers = ['Switch','Vlan Name','Vlan ID','Interface','Mac'];
                break;
            case 'multicast':
                headers = ['Switch','Vlan Name','Multicast Interface','Multicast Group Address','Multicast Listener Address'];
                break;
            case 'lacp':
                headers = ['Switch','AE Interface','Receive Status','Interface Name','Transmit Status','Mux State'];
                break;                
        }

        var table_headers = "";
        var search_headers = "";
        search_headers += "<tr id='filter_global'>\
                    <td>Global search</td>\
                    <td align='center'><input type='text' class='global_filter' id='global_filter'></td>\
                    <td align='center'><input type='checkbox' class='global_filter' id='global_regex'></td>\
                    <td align='center'><input type='checkbox' class='global_filter' id='global_smart' checked='checked'></td>\
                </tr>";

        for(var i = 0; i < headers.length; i++){
            j = i+1;
            table_headers += "<th>"+headers[i]+"</th>";
            search_headers += "<tr id='filter_col"+j+"' data-column='"+i+"'>\
                    <td>"+headers[i]+"</td>\
                    <td align='center'><input type='text' class='column_filter' id='col"+i+"_filter'></td>\
                    <td align='center'><input type='checkbox' class='column_filter' id='col"+i+"_regex'></td>\
                    <td align='center'><input type='checkbox' class='column_filter' id='col"+i+"_smart' checked='checked'></td>\
                </tr>";
        }
        document.getElementById('table').innerHTML = table_headers;
        document.getElementById('searchbars').innerHTML = search_headers;
        /**Render the tables **/
        var table = $('#myTable').DataTable( {
            "ajax": filename,
            "paging": false,
            "scrollY": 400
        } );
        setInterval( function (){
            table.ajax.reload();
        }, 5000 ); 
        
        $('input.global_filter').on( 'keyup click', function () {
        filterGlobal();
        } );

        $('input.column_filter').on( 'keyup click', function () {
        filterColumn( $(this).parents('tr').attr('data-column') );
        } );


    } );

  
</script>
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
    <table id="myTable" class="display" style="width:100%">
        <thead>
            <tr id='table'></tr>
        </thead>
    </table>
    <div id='csvlink'></div>

</body>
</html>
