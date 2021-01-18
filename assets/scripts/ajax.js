$(document).ready(function () {
    var review_div = $('#tm-review-rating-star');
    var next = $('#next-page');
    var prev = $('#previous-page');


    var auto_review = null;
    review_div.mouseover(function () { 
        clearInterval(auto_review);
        
    });

    review_div.mouseout(function () { 
        auto_review = setInterval(ajax_review, 5000);
        
    });
    
    
    function ajax_review(){
        var currentHref = next.attr('href');//?page=1
        var currentPage = parseInt((currentHref).split('=')[1]);
        var nextPage = currentPage + 1;
        if (currentPage > 10 && auto_review != null) {
            clearInterval(auto_review)
        } else{next.attr('href', "?page=" + nextPage);}
        
        review_div.load(`${currentHref} #tm-review-rating-star > *`);
    };

    auto_review = setInterval(ajax_review, 5000);

    // next.on('click', function(e){
    //     e.preventDefault();
        
    //     debugger;
    //     this.search = "?page=" + (parseInt(this.search.split('=')[1]) + 1)
    //     review_div.load(`${this.href} #tm-review-rating-star > *`);
       
    // })

    
    // prev.click(function(){
    //     var url = $(this).attr('href');
    // })
    // function ajax_get_companies(params) {
    //     var XHR = new XMLHttpRequest()
    // }

    // ajax_get_companies();   
  
});