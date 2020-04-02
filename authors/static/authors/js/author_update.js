$( document ).ready(function() {
    'use strict'

    initialize();


    function initialize() {
        if ($("#id_is_docentvak").prop("checked") === true) {
            $("#id_docentvak_date").prop( "disabled", false);
        } else {
            $("#id_docentvak_date").prop( "disabled", true);
        }

        if ($("#id_is_professor").prop("checked") === true) {
            $("#id_professor_date").prop( "disabled", false);
        } else {
            $("#id_professor_date").prop( "disabled", true);
        }

        if ($("#id_is_candidate").prop("checked") === true) {
            $("#id_candidate_date").prop( "disabled", false);
            $("#id_candidate_title").prop( "disabled", false);
            $("#id_candidate_specialty").prop( "disabled", false);
        } else {
            $("#id_candidate_date").prop( "disabled", true);
            $("#id_candidate_title").prop( "disabled", true);
            $("#id_candidate_specialty").prop( "disabled", true);
        }

        if ($("#id_is_doctor").prop("checked") === true) {
            $("#id_doctor_date").prop( "disabled", false);
            $("#id_doctor_title").prop( "disabled", false);
            $("#id_doctor_specialty").prop( "disabled", false);
        } else {
            $("#id_doctor_date").prop( "disabled", true);
            $("#id_doctor_title").prop( "disabled", true);
            $("#id_doctor_specialty").prop( "disabled", true);
        }

    }



});