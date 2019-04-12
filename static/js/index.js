$(document).ready(function() {
    $('form').on('submit', function(event) {
        $.ajax({
            data : {
                server : $('#serverInput').val(),
                alarm : $('#alarmInput').val(),
                action : $('#actionInput').val()
            },
            type : 'POST',
            url : '/process'
        })
        .done(function(data) {
            if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
            }
            else {
                console.log(data);
                var dataStr = JSON.stringify(data, null, 2);
                console.log(dataStr);
                $('#successAlert').text(dataStr).show();
				$('#errorAlert').hide()
            }
            
        });

        event.preventDefault();

    });

});