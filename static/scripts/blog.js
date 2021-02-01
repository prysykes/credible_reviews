var add_comment = $('.add_comment');
var comment_form = $('#comment_form')

$('#id_name, #id_email, #id_content ').addClass('form-control');

add_comment.click(function(){
    comment_form.toggleClass('hide_form');
});

