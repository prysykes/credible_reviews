var add_comment = $('.add_comment');
var comment_form = $('#comment_form');
var add_comment_reply = $('.add_comment_reply');
var reply_form = $('.reply_form');

var clicker_r = 1
add_comment_reply.click(function(){
    var current_index = add_comment_reply.index($(this))
    
    
        
    reply_form.eq(current_index).toggleClass('hide_form')
    if (clicker_r == 1) {
        $(this).text('hide reply')
        clicker_r = 0
    }else if (clicker_r == 0){
        $(this).text("reply")
        clicker_r = 1;
    }
    
});


$('#id_name, #id_email, #id_content ').addClass('form-control');

add_comment.click(function(){
    comment_form.toggleClass('hide_form');
});

