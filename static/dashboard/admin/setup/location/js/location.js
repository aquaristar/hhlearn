var step_location = angular.module('step_location', []);

step_location.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

function LocationForm() {
    this.is_electronic_postings_enabled = null;
    this.is_organization_accredited = null;
    this.is_signup_monthly_safety_program = null;
};

LocationForm.prototype.submit = function ($scope, $http) {

};


$(function () {

    /*
     START http://hhlearn.dev.oddovo.net:8081/dashboard/admin/setup/location_2_1
     */
    var is_primary = new Array();
    var is_command_location = new Array();
    var is_primary_already_exist = false;
    var is_command_location_already_exist = false;
    var is_primary_total_no = 0;
    var is_command_location_total_no = 0;

    /*
     this if for the fancy dropdown.
     */
    $("select[id='selectpicker']").selectpicker({style: 'btn-lg btn-primary'});

    /*
     this is for formatting phone numbers.
     */
    $("#phone,#fax,#point_of_contact_phone,.phone_number,input[id$='-phone'],input[id$='-fax']").mask("(999) 999-9999");


    $("select[name$='-is_primary']").each(function (index) {

        /*
         lets store everything in array for later use
         */

        is_primary[index] = $(this);

         if ($(this).val() != 1) {

                $(this).next("div").find("button").addClass("disabled");
                is_primary_total_no = is_primary_total_no + 1;
        }
        /*
         fire this on change
         */
    }).change(function () {

            /*
             on change run through loop
             */
            for (var i = 0; i < is_primary.length; i++) {

                /*
                 if element changed is in array which we created on page load.
                 */
                if (is_primary[i].is($(this))) {
                    /*
                     if selected value is YES the don't need to do anything for this element
                     */
                    if ($(this).val() == 1) {
                        /*
                        if this dropdown is yes then we need to disable second dropdown because both can't be YES on one location
                         */
                       // is_command_location[i].prop('disabled', true).next("div").find("button").addClass("disabled");
                    }
                    /*
                     lets disable rest of elements  if they have avlue of 0
                     */
                    else if ($(this).val() == 0) {


                        /*
                         lets enable the second dropdown becuse this is NO
                         */
                        for (var i = 0; i < is_command_location.length; i++) {

                            if(is_command_location[i].val()==1)
                            {
                                is_command_location_already_exist = true;
                            }
                        }

                        if(!is_command_location)
                        {
                           // is_command_location[i].prop('disabled', false).next("div").find("button").removeClass("disabled");
                            is_command_location[i].next("div").find("button").removeClass("disabled");

                        }


                        /*
                         If user have selected NO then we need to enable all other dropdowns for user.
                         */
                        for (var i = 0; i < is_primary.length; i++) {

                            if(is_command_location[i].val()!=1)
                            {
                               // is_primary[i].prop('disabled', false).next("div").find("button").removeClass("disabled");
                                is_primary[i].next("div").find("button").removeClass("disabled");

                            }
                        }
                    }
                }
                /*
                 disable all other dropdowns if it's not chnaged.
                 */
                else {
                    //is_primary[i].prop('disabled', true).next("div").find("button").addClass("disabled");
                    is_primary[i].next("div").find("button").addClass("disabled");
                }

            }


        });

      if(is_primary_total_no == is_primary.length)
      {
          for (var i = 0; i < is_primary.length; i++) {

              is_primary[i].next("div").find("button").removeClass("disabled");
          }
      }






    $("select[name$='-is_command_location']").each(function (index) {

        /*
         lets store everything in array for later use
         */

        is_command_location[index] = $(this);
        if ($(this).val() != 1) {

            $(this).next("div").find("button").addClass("disabled");
            is_command_location_total_no = is_command_location_total_no + 1;
        }

        /*
         fire this on change
         */
    }).change(function () {

            /*
             on change run through loop
             */
            for (var i = 0; i < is_command_location.length; i++) {

                /*
                 if element changed is in array which we created on page load.
                 */
                if (is_command_location[i].is($(this))) {
                    /*
                     if selected value is YES the don't need to do anything for this element
                     */
                    if ($(this).val() == 1) {
                        /*
                         if this dropdown is yes then we need to disable second dropdown because both can't be YES on one location
                         */
                       // is_primary[i].prop('disabled', true).next("div").find("button").addClass("disabled");
                    }
                    /*
                     lets disable rest of elements  if they have avlue of 0
                     */
                    else if ($(this).val() == 0) {

                        /*
                         lets enable the second dropdown becuse this is NO
                         */
                       /* for (var i = 0; i < is_primary.length; i++) {

                            if(is_primary[i].val()==1)
                            {
                                is_primary_already_exist = true;
                            }
                        }

                        if(!is_primary_already_exist)
                        {
                            is_primary[i].prop('disabled', false).next("div").find("button").removeClass("disabled");

                        }    */

                        /*
                         If user have selected NO then we need to enable all other dropdowns for user.
                         */
                        for (var i = 0; i < is_command_location.length; i++) {


                                //is_command_location[i].prop('disabled', false).next("div").find("button").removeClass("disabled");
                                is_command_location[i].next("div").find("button").removeClass("disabled");


                        }
                    }
                }
                /*
                 disable all other dropdowns if it's not chnaged.
                 */
                else {
                    //is_command_location[i].prop('disabled', true).next("div").find("button").addClass("disabled");
                    is_command_location[i].next("div").find("button").addClass("disabled");
                }

            }


        });


    if(is_command_location_total_no == is_command_location.length)
    {
        for (var i = 0; i < is_command_location.length; i++) {

            is_command_location[i].next("div").find("button").removeClass("disabled");
        }
    }
    $( "#2_1_submit_button" ).click(function() {

        var is_primary_available = false;
        var is_command_location_available = false;

        for (var i = 0; i < is_primary.length; i++) {

            if(is_primary[i].val()==1)
            {
                is_primary_available = true;

            }
        }

        for (var i = 0; i < is_command_location.length; i++) {

            if(is_command_location[i].val()==1)
            {
                is_command_location_available = true;

            }
        }

        if(!is_primary_available)
        {
            $("#is_primary_error").css("display", "block");
        }
        if(!is_primary_available)
        {
            $("#is_command_location_error").css("display", "block");
        }

        if(is_command_location_available && is_primary_available)
        {
                return true;
        }
        else {
            event.preventDefault();
        }

    });
    /*
     END http://hhlearn.dev.oddovo.net:8081/dashboard/admin/setup/location_2_1
     */



    /*
     START http://hhlearn.dev.oddovo.net:8081/dashboard/admin/setup/location_2_2
     */

    var is_accredited = new Array();
    var accreditation_agency = new Array();


    $("select[name$='-accreditation_agency']").each(function (index) {

        accreditation_agency[index] = $(this);

    });

    $("select[name$='-is_accredited']").each(function (index) {

        /*
         lets store everything in array for later use
         */

        is_accredited[index] = $(this);

        if ($(this).val() != 1) {

            $(this).parent().parent().parent().parent().parent().next(".row").css("display", "none");

        }
        /*
         fire this on change
         */
    }).change(function () {

            if ($(this).val() == 1) {

                $(this).parent().parent().parent().parent().parent().next(".row").css("display", "block");
            }
            else if($(this).val() == 0)
            {
                $(this).parent().parent().parent().parent().parent().next(".row").css("display", "none");
            }

        /*
         fire this on change
         */
    });
});