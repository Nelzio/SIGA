$(document).ready(function(){
    var pathname_app = window.location.pathname.split('/');
    if(pathname_app.length<3){
        $('.navbar-costom-nav li#nav-home').addClass('active');
    }else{
        $('.navbar-costom-nav li#nav-'+pathname_app[1]).addClass('active');
    }





    $("#teste").click(function(event){
        event.preventDefault(); 
        $('#doteste').dropdown('toggle');
        $('.dropdown-toggle').dropdown()
    });

    $('.dropdown-menu').dropdown("show")















        $(function () {
            $(window).scroll(function () {
                // set distance user needs to scroll before we fadeIn navbar
                if ($(this).scrollTop() > 200) {
                    $('.navbar-costom').addClass("fixed-top");
                    //$('.navbar-costom').fadeIn();
                } else {
                    //$('.navbar-costom').fadeOut();
                    $('.navbar-costom').removeClass("fixed-top");
                }
            });

            
        });


        //var newURL = window.location.pathname.split('/');
        //var newURL1 = window.location.host;   
        //var newURL2 = window.location.hostname;
        //var newURL3 = window.location.protocol;
        //var newURL4 = window.location.pathname;
        //var newURL5 = window.location.href;   
        //var newURL6 = window.location.hash;   
        //var newURL7 = window.location.search; 

        
        




});