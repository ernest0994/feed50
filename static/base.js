var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
})
$(document).ready(function() {
    $('#data').DataTable();
    let navLink = $('a[href$="' + location.pathname + '"]');
    navLink.addClass('active');
    navLink.attr("aria-current", "page");
});
