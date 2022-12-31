var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
})
$(document).ready(function() {
    let navLink = $('a[href$="' + location.pathname + '"]');
    navLink.addClass('active');
    navLink.attr("aria-current", "page");
});
