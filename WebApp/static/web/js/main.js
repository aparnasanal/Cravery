// Wait until DOM is ready
$(document).ready(function () {

    "use strict";

    // 1️⃣ Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show'); // Remove spinner
            }
        }, 1);
    };
    spinner();

    // 2️⃣ WOW.js animations
    if (typeof WOW === 'function') {
        new WOW().init();
    }

    // 3️⃣ Owl Carousel initialization
    if ($.fn.owlCarousel) {
        $('.header-carousel').owlCarousel({
            loop: true,
            margin: 0,
            nav: true,
            items: 1,
            dots: true,
            autoplay: true,
            autoplayTimeout: 5000,
            autoplayHoverPause: true,
            responsiveClass: true
        });
    }

    // 4️⃣ Back to top button (optional)
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });

    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });

    // 5️⃣ Other JS you need can go here

});
