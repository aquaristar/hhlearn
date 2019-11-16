var registerViewModel = {


    /*
     after error is displayed and then user try to enter password or email then
     hide error message.
     */
    userKeypress : function(target,event) {

        $(event.target).parent('.form-group').removeClass('has-error');
        $(event.target).attr( "title", "" );
        $(event.target).attr( "data-original-title", "" );
    }

};

// Activates knockout
ko.applyBindings(registerViewModel, document.getElementById("form_register"));
