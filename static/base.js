$(document).ready(function() {
    let navLink = $('a[href$="' + location.pathname + '"]');
    navLink.addClass('active');
    navLink.attr("aria-current", "page");
});