$(function() {

    $("select[id='selectpicker']").selectpicker({style: 'btn-lg btn-primary'});

    $("select[name='regions_enabled']").each(function (index) {

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


    var vals = [];
    var textvals = [];

    var selected_values = [];

  $("select[name='locations']").each(function (index) {



    }).change(function () {

          vals = [];
          textvals = [];
          getMultipleSelectVals("id_locations")

          $("select[name='departments'] option").each( function( i, option ) {

              self = $(this);

              $.each(textvals, function( index, value ) {

                  if (self.text().indexOf(value) >= 0){

                      selected_values.push(self.val())
                  }
              });

              $("select[name='departments']").val(selected_values)
          });
    });



    function getMultipleSelectVals( id ){
        $( '#' + id + ' :selected' ).each( function( i, selected ) {
            vals[i] = $( selected ).val();
            textvals[i] = $( selected ).text();
        });
    }// end function


});