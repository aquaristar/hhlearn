var viewModel = {


    /*
     after error is displayed and then user try to enter password or email then
     hide error message.
     */
    userKeypress : function(target,event) {

        $(event.target).parent('.form-group').removeClass('has-error');
        $(event.target).attr( "title", "" );
        $(event.target).attr( "data-original-title", "" );
    },

    payment_method_image :  ko.observable("http://placehold.it/35"),

    show_credit_card_form : ko.observable(false),

    show_payment_icon : ko.observable(false),

    selected_payment_type : {},

    selected_number_of_user : {},

    membership_plan_change : {},

    state_change : {},

    selected_number_of_user_cost : ko.observable(""),

    show_number_of_user_cost : ko.observable(false),


    payment_type_change: function (target,element) {

        if(!target.selected_payment_type)
        {
            target.show_credit_card_form(false);

            target.show_payment_icon(false);

        }
        else {
            target.show_payment_icon(true);
            target.payment_method_image($(element.target).find("option:selected").attr('data-image'));
            $(element.target).parent().find(".label-important").text('');

            /*
             Paypal payment method have ID==4
             */
            if(target.selected_payment_type=="1")
            {
                target.show_credit_card_form(false);

            }
            else {
                target.show_credit_card_form(true);
            }

        }





    },

    number_of_user_change: function (target,element) {

        if(target.selected_number_of_user=="")
        {
            this.show_number_of_user_cost(false);

        }
        else {
            this.show_number_of_user_cost(true);
            this.selected_number_of_user_cost("$"+$(element.target).find("option:selected").attr('data-monthly-price'));
            $(element.target).parent().find(".label-important").text('');
        }


    },

    membership_plan_change: function (target,element) {

            $(element.target).parent().find(".label-important").text('');

    },

    state_change: function (target,element) {

            $(element.target).parent().find(".label-important").text('');

    }
};

var payment = payment || {};

$(function() {

    payment.VM =  viewModel;

    ko.applyBindings(payment.VM, document.getElementById("app_payment"));


    if(payment.VM.selected_payment_type){

        $("#payment_method").val(payment.VM.selected_payment_type).change();
    }

    if(payment.VM.selected_number_of_user){

        $("#user_pack").val(payment.VM.selected_number_of_user).change();
    }


});

