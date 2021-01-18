$(document).ready(function () {
    var search_display = $('#tm-search-display');
    var search_form = $('#tm-search-form');
    var business = $('#business');
    var response = $('#response');

    business.keyup(function () { 
        $.ajax({
            type: "GET",
            url: "{% url 'search_business'%}",
            data: {
                'search_text': business.val(),
            },
            success: searchSuccess,
            dataType: 'html',

        })
    });
    
    
});

function searchSuccess(data, textStatus, jqXHR) {
    response.html(data)
}
