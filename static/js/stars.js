
$(document).ready(function(){

    // Review form star rating system 
    $(".formStars").click(function(){
        $(this).css("color", "#cbab82");
        $(this).prevAll("label").css("color", "#cbab82");
        $(this).nextAll("label").css("color", "#e6e6e6");
    });

    

});