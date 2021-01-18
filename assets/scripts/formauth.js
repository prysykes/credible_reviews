$(document).ready(function(){
    // star show other text
    $('#other').hide();
    $('#proof').hide();    
    $('#category').change(function(){
        if ($('#category').val() == 'otherSelect') {
            $('#other').show(600);
        }else {
            $('#other').hide(600);
        }
       
    }); // end show other text
    
    $('#individualForm').submit(function () { 
        // start confirm password and option select
        if ($('#password').val() != $('#Cpassword').val()){
            alert("Passwords don't Match");
            return false;
        }else if ($('#category').val() == 'Choose a Category'){
            alert('You have not Selected any Category')
                 $('#category').focus();
            return false
        }else if ($('#state').val() == 'Choose a State'){
            alert("You have not Selected Company's State of Operation")
                 $('#state').focus();
            return false
        }else if ($('#title').val() == 'Choose a Title'){
            alert("Please Select a Suitable Title")
                 $('#title').focus();
            return false
        }
        
        else {
            return true;
        };
            
        
    });
    // start privacy condition
    $('#individualFormSubmit').click(function(){
        if ($('#agreeTerms').prop('checked') == true){
            return true;
        }else {
            alert('Please agree to our privacy statement!')
            return false;
        }
    }
       
    );        
    
    // start package choice
    if($('#yes').change(function(){
        $('#proof').show(600);
    }));

    if($('#no').change(function(){
        $('#proof').hide(600);
    }));


});

