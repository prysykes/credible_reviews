var add_comment = $('.add_comment');
var comment_form = $('#comment_form');
var add_comment_reply = $('.add_comment_reply');
var reply_form = $('.reply_form');


add_comment_reply.click(function(){
    reply_form.toggleClass('hide_form');
});


$('#id_name, #id_email, #id_content ').addClass('form-control');

add_comment.click(function(){
    comment_form.toggleClass('hide_form');
});

