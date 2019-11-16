$(function() {

    //$("select[id='selectpicker']").selectpicker({style: 'btn-lg btn-primary'});



    var departments_enabled = new Array();

    $("select[name$='-departments_enabled']").each(function (index) {

        /*
         lets store everything in array for later use
         */

        departments_enabled[index] = $(this);

        if ($(this).val() != 1) {

            $(this).parent().parent().parent().parent().parent().next(".row").css("display", "none");

        }
        /*
         fire this on change
         */
    }).change(function() {

        if ($(this).val() == 1) {

            $(this).parent().parent().parent().parent().parent().next(".row").css("display", "block");
        }
        else if($(this).val() == 0)
        {
            $(this).parent().parent().parent().parent().parent().next(".row").css("display", "none");
        }

    });

})(jQuery);