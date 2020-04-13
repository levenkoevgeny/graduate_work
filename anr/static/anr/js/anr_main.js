var scince = 2; var dissertation = 3; var nir = 1;

function hide_divs() {
    $('#sciencework_div, #nir_div, #dissertation_div').css('display', 'none');
}


function change_anr_divs(id) {
    hide_divs();
    switch (id) {
        case scince:
            $('#sciencework_div').css('display', 'block');
            $('#id_sciencework').prop("required", true);
            break;
        case dissertation:
            $('#dissertation_div').css('display', 'block');
            $('#id_dissertation').prop("required", true);
            break;
        case nir:
            $('#nir_div').css('display', 'block');
            $('#id_nir').prop("required", true);
            break;
    }
}


function init_page() {
    change_anr_divs(parseInt($('#id_development_kind').val()));
}


$( document ).ready(function() {
    'use strict'

    $('.select2_class').select2();

    init_page();

    $('#id_development_kind').on('change', function () {

        change_anr_divs(parseInt($(this).val()));
    });

});