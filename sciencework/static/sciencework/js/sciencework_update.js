$( document ).ready(function() {
    'use strict'


    var id = $('#id_kind').val();
    init_fields(parseInt(id));

    var selected_option_magazine = $('#id_magazine option:selected').val();
    var selected_option_digest = $('#id_digest option:selected').val();

    if (selected_option_magazine !='') {
        $('#magazinekindradio').click();
    }

    if (selected_option_digest !='' ) {
        $('#digestkindradio').click();
    }

    var selected_option_international_base = $('#id_ininternational option:selected').val();

    if (selected_option_international_base > 0 ) {
        $('#id_ininternational').prop("disabled", false).prop("required", true);
        $('#ininternational_check').prop("checked", true);

    }

    var select_option_conference = $('#id_conference').val();

    if (select_option_conference !=''){
        $('#forum_result_check').click();
    }

    var select_option_grif = $('#id_grif').val();

    if (select_option_grif !=''){
        $('#id_grif_check').click();
    }

});