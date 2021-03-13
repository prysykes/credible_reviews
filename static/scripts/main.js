$(document).ready(function () {
    
    var display_company = $('#tm-display-companies');
    var hide_category_button = $('#hide_category_button');
    var tm_company_category = $('#tm_company_category');
    var send_message_button = $('#tm_send_message_button');
    var message_div = $('#tm_send_message_div');
    var add_review = $('#tm-add-review-div');
    var review_button = $('#tm-review-button');
    var message_div_display = $('#user_message_div');
    var delete_message = $('.tm_delete_message');
    var message_hide_button = $('#tm_show_mesages');
    var average_rating = $('#tm-average_rating');
    var remarks = $('#tm-remarks');
    var companies = $('#tm-companies');
    var list_company_button = $('#list_company_button');
    var list_company_display = $('#list_company_display');
    var claimed_detail = $('#tm-claimed-detail');
    var claimed = $('#tm-claimed');
    var share_button = $('.share_button');
    var social_share = $('.social_share');
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

    
    message_div_display.hide()
    list_company_display.hide()
    display_company.hide()

   
    // begin toggle message division
    send_message_button.click(function() {
        message_div.toggleClass('formhidden');
        $("#id_subject").focus();
        add_review.addClass('formhidden');
    }) 
    // toggle review on detail page

    review_button.click(function(){
        add_review.toggleClass('formhidden');
        $("#id_rating").focus();
        message_div.addClass("formhidden"); 
    });


    // begin toggle message division
    var clicker_m = 1
    message_hide_button.click(function(){
        message_div_display.slideToggle(600);
        message_div_display.scrollTop(700)
        review_display.hide();
        display_company.hide();
        
        if (clicker_m == 1) {
            $(this).text("Hide Messages")
            clicker_m = 0
        }else if (clicker_m == 0){
            $(this).text("Show Messages")
            clicker_m = 1;
        }
        
        
    })

    // begin styling of filter inputs on browsereviews page
    var clicker_c = 1
    companies.click(function(){
        display_company.slideToggle(600);
        review_display.hide(); 
        message_div_display.hide();
        if (clicker_c == 1) {
            $(this).text("Hide Companies")
            clicker_c = 0
        }else if (clicker_c == 0){
            $(this).text("Show Companies")
            clicker_c = 1;
        }
    })

    // setting tabindex to 1 for forms on company detail page
    // review_button.click(function(){
    //     $("#id_rating").focus();
    // })
    
    // add bootsrap form control for submit review fields
   $("#id_company, #search_company, #id_message, #id_subject, #id_review_text").addClass('form-control')

   // add bootsrap form control for  submit generic review fields
    $("#id_company_name_g, #id_subject_g, #id_company_phone_g, #id_company_email_g, #id_review_text_g, #id_company_address_g, #id_company_state_g, #id_company_sector_g, #id_picture_evidence_g, #id_company_logo_g, #id_company_website_g, #id_rating_g").addClass('form-control')
    $('#id_rating_g').attr({
        'class': 'form-control',
        'placeholder': 'maximum = 5',
        'min': 1,
        'max':5,
    })
    
    // begin stylin go of filter inputs on featured page
    avg_rating_input.attr({
        'min': 1,
        'max': 5,
        'placeholder': 'max=5',
    });

    $("#id_average_rating, #id_company_name, #id_company_sector, #id_company_state").addClass('form-control');

    // adding bootsrap form-control class to company sign-up page
    $("#id_username, #id_password1, #id_password2, #id_first_name, #id_last_name, #id_email, #id_phone, #id_designation, #id_profile_photo, #id_location, #id_new_password1, #id_new_password2").addClass('form-control');
    
    // implementing delete message
    delete_message.click(function () {
        
        return confirm("This action can't be undone, delete? ")

      })

    // implementing share button toggle
    share_button.click(function(){
        
        var current_index = share_button.index($(this))
        
        social_share.eq(current_index).toggleClass('formhidden')
        
        
        
       
        
    });

    // begin show/hide company category
    var clicker = 0
    hide_category_button.click(function(){
        tm_company_category.toggle(600);
        if (clicker==0){
            hide_category_button.text("Show Sectors")
            clicker = 1
        }else if (clicker == 1){
            hide_category_button.text("Hide Sectors")
            clicker = 0
        }
        
        
        
    });
    

    // end show/hide company category
    
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
    
    /* implementing view reviews toggle for company profile */
    var clicker_r = 1
    view_reviews.click(function(){
        review_display.slideToggle(600);
        display_company.hide();
        message_div_display.hide();
        if (clicker_r == 1) {
            $(this).text("Show Reviews")
            clicker_r = 0
        }else if (clicker_r == 0){
            $(this).text("Hide Reviews")
            clicker_r = 1;
        }
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
    // implementing allow message div to permanently scroll to buttom
    message_div_display.scrollTop(700)

    // End window effect
    topBtn.click(function(){
        $('html').animate({scrollTop: 0}, 1000);
      }); 
      

  
});
