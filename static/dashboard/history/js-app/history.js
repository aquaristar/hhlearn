/**
 * Created with IntelliJ IDEA.
 * User: bahmed
 * Date: 10/15/2013
 * Time: 6:26 PM
 * To change this template use File | Settings | File Templates.
 */
var dashboard_core_history = {

    //currentProfit: ko.observable(-50),
    /*
     lets observe user email
     */
    loginEmail: ko.observable(''),


    /*
     when user press cross button then execute this and hide error message.
     */
    toggle : function(target, event) {

        $( "ul#"+event.target.id ).toggle("slow");
    },

    init: function() {
        _.bindAll(
            this,
            'toggle'
        );
    }
};

// Activates knockout
ko.applyBindings(dashboard_core_history, document.getElementById("app_history"));