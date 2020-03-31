$( document ).ready(function() {
    'use strict'

    $('#id_candidate_specialty, #id_doctor_specialty').select2();

    $( "#id_is_docentvak").on( "click", function() {
        if ($(this).prop("checked")==true){
            $("#id_docentvak_date").prop( "disabled", false);
        } else {
            $("#id_docentvak_date").prop( "disabled", true);
        }
    });

    $( "#id_is_professor").on( "click", function() {
        if ($(this).prop("checked")==true){
            $("#id_professor_date").prop( "disabled", false);
        } else {
            $("#id_professor_date").prop( "disabled", true);
        }
    });


    $( "#id_is_candidate").on( "click", function() {
        if ($(this).prop("checked")==true){
            $("#id_candidate_date").prop( "disabled", false);
            $("#id_candidate_title").prop( "disabled", false);
            $("#id_candidate_specialty").prop( "disabled", false);
        } else {
            $("#id_candidate_date").prop( "disabled", true);
            $("#id_candidate_title").prop( "disabled", true);
            $("#id_candidate_specialty").prop( "disabled", true);
        }
    });

    $( "#id_is_doctor").on( "click", function() {
        if ($(this).prop("checked")==true){
            $("#id_doctor_date").prop( "disabled", false);
            $("#id_doctor_title").prop( "disabled", false);
            $("#id_doctor_specialty").prop( "disabled", false);
        } else {
            $("#id_doctor_date").prop( "disabled", true);
            $("#id_doctor_title").prop( "disabled", true);
            $("#id_doctor_specialty").prop( "disabled", true);
        }
    });

});