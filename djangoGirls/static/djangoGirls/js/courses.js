$(document).ready(function(){

//==========================Cursos===============================
    $("#table-vocacional").hide();

    $("#nav-vocacional").click(function (event) {
        event.preventDefault();
        $("#table-regular").hide();
        $("#table-vocacional").show();
        $("#nav-vocacional").addClass("active");
        $("#nav-regular").removeClass("active");
    });

     $("#nav-regular").click(function (event) {
        event.preventDefault();
        $("#table-vocacional").hide();
        $("#table-regular").show();
        $("#nav-regular").addClass("active");
        $("#nav-vocacional").removeClass("active");

    });



    //==================================Biblioteca======================
    //$(".tree-menu").addClass("fadeOutUp");
/*
    function muda(tipo){
        if(tipo===1){
            $(".tree-menu").hide();

        }else if(tipo===0){
                $(".tree-menu").show();
        }
    }

    $(".tree-menu").hide();
    a=0;

    $(".tree").click(function (event){
        event.preventDefault();

        if(a===0){
            a=1;
            $(".tree-menu").show();
        }else{
            a=0;
            $(".tree-menu").hide();
        }
*/
    //$(".tree-menu").removeClass("fadeOutUp");
    //$(".tree-menu").addClass("fadeInDown");

    /*if($(".tree-menu").hide()){
        $(".tree-menu").show();
    }else{
        $(".tree-menu").hide();
    }





    });*/




});

