function time(){
    var d = new Date()
    var h = d.getHours()
    var m = d.getMinutes()
    var s = d.getSeconds()
    var z = d.getMilliseconds()

    if(s<10){
        s = "0"+s
    }
    document.getElementById("relogio").innerHTML = h+":"+m+":"+s
    setInterval("time()",1000)

    /*if(s<20){
        document.getElementById("navbar-costom").style.backgroundColor = "#ed3437"
        document.getElementById("footer").style.backgroundColor = "#ed3437"
    }else if(s>=40){
        document.getElementById("navbar-costom").style.backgroundColor = "#2b7044"
        document.getElementById("footer").style.backgroundColor = "#2b7044"
    }else{
        document.getElementById("navbar-costom").style.backgroundColor = "#fff215"
        document.getElementById("footer").style.backgroundColor = "#fff215"
    }*/
}

