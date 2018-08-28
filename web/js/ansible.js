
$(document).ready( function () {
    $('button.ansible-bt').on('click',function(){
        $.ajax({
            type: 'POST',
            url: 'dosomething.py',
            success: function(response){
                console.log(response);
            }
        });

    });

} );