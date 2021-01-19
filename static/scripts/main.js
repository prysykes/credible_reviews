$(document).ready(function () {
    
    
    
    var display_company = $('#tm-display-companies');
    var send_message_button = $('#tm_send_message_button');
    var message_div = $('#tm_send_message_div');
    var add_review = $('#tm-add-review-div');
    var review_button = $('#tm-review-button');
    var delete_message = $('.tm_delete_message');
    var message_hide_button = $('#tm_show_mesages');
    var average_rating = $('#tm-average_rating');
    var remarks = $('#tm-remarks');
    var companies = $('#tm-companies');
    var list_company_button = $('#list_company_button');
    var list_company_display = $('#list_company_display');
    var claimed_detail = $('#tm-claimed-detail');
    var claimed = $('#tm-claimed');
    var review_display = $('#tm-display-reviews');
    var view_reviews = $('#tm-reviews');
    var delete_review = $('.tm-delete-review');
    var topBtn = $('#topBtn');
    var request_review  = $('.tm-request-review');
    var request_review_display = $('.tm-request-review-display');
    var form_filter_button = $('#tm-form-filter-button');
    var form_filter = $('#tm-form-filter');
    var avg_rating_input = $('#id_average_rating');
    var filter_button_div = $('#tm-filter-button-div');
    var review_rating = $('#tm-review-rating-star .review');
    var star_one = $('#star_one');
    var star_two = $('#star_two');
    var star_three = $('#star_three');
    var star_four = $('#star_four');
    var star_five = $('#star_five');

    
    review_display.show()
    list_company_display.hide()

   
    // begin toggle message division
    send_message_button.click(function() {
        message_div.toggleClass('formhidden');
        add_review.addClass('formhidden');
    }) 
    // toggle review on detail page

    review_button.click(function(){
        add_review.toggleClass('formhidden');
        message_div.addClass("formhidden"); 
    });


    // begin toggle message division
    message_hide_button.click(function(){
        $('#user_message_div').slideToggle(600);
        review_display.hide();

    })
    // begin stylin go of filter inputs on featured page
    avg_rating_input.attr({
        'min': 1,
        'max': 5,
        'placeholder': 'max=5',
    });

    $("#id_average_rating, #id_company_name, #id_company_sector, #id_company_state").addClass('form-control');
    
    // implementing delete message
    delete_message.click(function () {
        
        return confirm("Are you sure you want to delete message? ")

      })
    /* $('#tm-filter-form').focusout(function(){
        
        form_filter.hide();
    }) */
    // end stylin go of filter inputs on featured page

    // begin stylin go of filter inputs on browsereviews page
    $('#id_company, #id_rating, #id_date_added').addClass('form-control')
    $('#id_rating').attr({
        'min': 1,
        'max': 5,
        'placeholder': 'max=5',
        'width': 90,
    });

    $('#id_date_added').attr({
        'placeholder': 'format=2020-10-22'
    })
    // begin stylin go of filter inputs on browsereviews page
    display_company.hide();
    companies.click(function(){
        display_company.slideToggle(600);
        review_display.hide(); 
    })
    /* hides detail for profile company page with no claimed company.
        using booleanfield claimed. */
    
      
    // implementing send review togle display
    request_review_display.hide(); 
    request_review.click(function(){
        request_review_display.slideToggle(600); 
        
    });
    //end implementation
    
    // implementing form fillter button toglleslide
    form_filter.hide()
    form_filter_button.click(function(){
        form_filter.slideToggle(600);
    })

    claimed_detail.hide(); 
    if (claimed.text() == "False"){
        claimed_detail.show();
    }else{
        list_company_display.hide();
    }

    list_company_button.click(function () {
        list_company_display.slideToggle(600);
        
    })
    /*
        reviewbutton below and addreviewdiv are found on
        the details page of each company
    */
    
    // average rating for company profile
    
    if (average_rating.text() == 0 ){
        remarks.text('Very Poor');
        remarks.addClass('text-danger');
    } else if (average_rating.text() == 1 ){
        remarks.text('Very Poor');
        remarks.addClass('text-danger');
    } else if (average_rating.text() == 2 ){
        remarks.text(' Poor');
        remarks.addClass('text-warning');
    } else if (average_rating.text() == 3 ){
        remarks.text('Good');
        remarks.addClass('text-info');
    } else if (average_rating.text() == 4 ){
        remarks.text('Very Good');
        remarks.addClass('text-primary');
    } else if (average_rating.text() == 5 ){
        remarks.text('Excellent');
        remarks.addClass('text-success');
    } 
    
    var average = $('#tm_average');
    
    /* var login = $('#tm-login');
    var login_company = $('#tm-login-company'); */

    // implementing star rating for company page
    
    if (average.text() == 1) {
        star_one.addClass('checked');
    } else if (average.text() == 2) {
        star_one.addClass('checked');
        star_two.addClass('checked');
    } else if (average.text() == 3) {
        star_one.addClass('checked');
        star_two.addClass('checked');
        star_three.addClass('checked');        
    } else if (average.text() == 4) {
        star_one.addClass('checked');
        star_two.addClass('checked');
        star_three.addClass('checked');
        star_four.addClass('checked');  
    } else if (average.text() == 5) {
        star_one.addClass('checked');
        star_two.addClass('checked');
        star_three.addClass('checked');
        star_four.addClass('checked'); 
        star_five.addClass('checked'); 
    }
    var search_sticky = $('#tm-search-pane');
    search_sticky.hide();
    
    /* login.hide(); */
    /* login_company.hide(); */
    topBtn.hide();
    
    
    
    delete_review.click(function(){
        return confirm("Are you sure you want to delete this review ?");
    });
    /*delete_review_regular.click(function(){
        //e.preventDefault();
        alert("Hello"); //confirm("Are you sure you want to delete review");
    });
    /* implementing view reviews toggle for company profile */
    view_reviews.click(function(){
        review_display.slideToggle(600);
        display_company.hide();
    });

    // begind back to top animation
    $(window).scroll(function () { 
        if ($(this).scrollTop() > 40){
            topBtn.show();
            search_sticky.show();
        
        }else {
            topBtn.hide();
            search_sticky.hide();
        }
        
    }); 
    

    // End window effect
    topBtn.click(function(){
        $('html').animate({scrollTop: 0}, 1000);
      }); 
      

  
});
