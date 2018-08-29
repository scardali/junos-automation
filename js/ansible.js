
$(document).ready( function () {
    $('button.ansible-bt').on('click',function(){
        $.ajax({
            type: 'POST',
            url: 'run.php',
            success: function(response){
                console.log(response);
            }
        });

    });

} );