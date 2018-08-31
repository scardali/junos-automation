
$(document).ready( function () {
    var task = getParameterByName('task');
    let filename = 'tasks/'+task+'/'+task+'-table.json';
    
    var headers = renderSearchbars(task);
    getTimestamp(filename);
    var table = renderTable(filename);
    downloadAsCsv(table, headers, task);

} );

function downloadAsCsv(table, headers, task){
    $('button.print-bt').on('click', function() {     
        var csvfile = 'tasks/'+task+'/'+task+'.csv';
        var rowData = table.rows({search: 'applied'}).data();

        var data = [];
        for(i = 0; i < rowData.length; i++)
            data.push(rowData[i]);
        $.ajax({
            type: 'POST',
            url: 'csv.php',
            data: {
                task: task,
                headers: headers, 
                data: data
                },
            success: function(){
                document.location.href = csvfile;
            }
        });

   } );
}

function renderTable(filename){
    var table = $('#myTable').DataTable( {
        "ajax": filename,
        "paging": false,
        "scrollY": 400,
        "select": true
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
    return table;
}

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

function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, '\\$&');
    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, ' '));
}

function renderSearchbars(task){
    var headers;
    switch(task){
        case 'version':
            headers = ['Switch','Junos Version'];
            break;
        case 'vlan':
            headers = ['Switch','Vlan Name','Vxlan Name','Vlan Tag','Interface'];
            break;
        case 'commit':
            headers = ['Switch','Client','Sequence Number','User','Date/Time','Comment'];
            break;
        case 'interface':
            headers = ['Switch','Interface','Description','Operational Status','Admin Status','Address Family','HW Address','Input Errors','Output Errors'];
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
    return headers;

}

function getTimestamp(filename){
    var url = "get_time.php?file="+filename;
    $.ajax({
        type: 'POST',
        url: url,
        success: function(response){
            document.getElementById('timestamp').innerHTML = "Data last updated: "+response;
        }
    });

}
