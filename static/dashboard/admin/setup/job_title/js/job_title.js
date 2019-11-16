$(function() {

    $("select[id='selectpicker']").selectpicker({style: 'btn-lg btn-primary'});

    $("select[name='custom_job_titles_enabled']").each(function (index) {

        if ($(this).val() == 0) {

            $(this).parent().parent().parent().parent().parent().next(".row").css("display", "none");
        }
        else if ($(this).val() == 1) {

            $(this).parent().parent().parent().parent().parent().next(".row").css("display", "block");
        }

    }).change(function () {


            if ($(this).val() == 0) {

                $(this).parent().parent().parent().parent().parent().next(".row").css("display", "none");
            }
            else if ($(this).val() == 1) {

                $(this).parent().parent().parent().parent().parent().next(".row").css("display", "block");
            }

        });




    var all_occupational_exposure = new Array();

    $("select[name$='-all_occupational_exposure']").each(function (index) {

        /*
         lets store everything in array for later use
         */

        all_occupational_exposure[index] = $(this);

        if ($(this).val() == 1) {

           // $(this).next("div").find("button").addClass("disabled");

            //$(this).parent().parent().parent().parent().parent().next(".row").css("display", "none");
        }
        /*
         fire this on change
         */
    }).change(function () {


            if ($(this).val() == 1) {

                // $(this).next("div").find("button").addClass("disabled");

                $(this).parent().parent().parent().parent().parent().next("div").find("select option[value='1']").removeAttr('selected');

                $(this).parent().parent().parent().parent().parent().next("div").find("select option[value='0']").attr('selected', 'selected');

                $(this).parent().parent().parent().parent().parent().next("div").find(".filter-option").text("No")

                $(this).parent().parent().parent().parent().parent().next("div").find("button").addClass("disabled");
            }
            else {
                $(this).parent().parent().parent().parent().parent().next("div").find("button").removeClass("disabled");
            }

        });

    var some_occupational_exposure = new Array();

    $("select[name$='-some_occupational_exposure']").each(function (index) {

        /*
         lets store everything in array for later use
         */

        some_occupational_exposure[index] = $(this);

        /*
         fire this on change
         */
    }).change(function () {




            if ($(this).val() == 1) {

                // $(this).next("div").find("button").addClass("disabled");

                $(this).parent().parent().parent().parent().parent().prev("div").find("select option[value='1']").removeAttr('selected');

                $(this).parent().parent().parent().parent().parent().prev("div").find("select option[value='0']").attr('selected', 'selected');

                $(this).parent().parent().parent().parent().parent().prev("div").find(".filter-option").text("No")

                $(this).parent().parent().parent().parent().parent().prev("div").find("button").addClass("disabled");
            }
            else {
                $(this).parent().parent().parent().parent().parent().prev("div").find("button").removeClass("disabled");
            }



        });

});