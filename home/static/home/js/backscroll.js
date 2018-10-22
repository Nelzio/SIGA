
function main() {

    (function () {
       'use strict';

        
    
      // jQuery Parallax
      function initParallax() {
        $('#intro').parallax("100%", 0.3);
        $('#services').parallax("100%", 0.3);
        $('#aboutimg').parallax("100%", 0.3);	
        $('#testimonials').parallax("100%", 0.1);
      }
      initParallax();
    }());
    
    
    }

    var pathname_app = window.location.pathname.split('/');
    if(window.location.pathname.split('/')[1]==="about"){
        main();
    }