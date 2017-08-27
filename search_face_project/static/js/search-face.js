	$(document).ready( function() {
	    $("#test-button").click( function(event) {
	        var querystr = $("#query-box").val();
	    $.get('/results/',
	        {query: querystr}, function(data){
	            $('#result-area').html(data);
	        });

	    });

	});