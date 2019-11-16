var organization = angular.module('organization', []);

organization.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

function OrganizationForm() {
    this.is_electronic_postings_enabled = null;
    this.is_organization_accredited = null;
    this.is_signup_monthly_safety_program = null;
};

OrganizationForm.prototype.submit = function($scope, $http) {

};


$(function() {

    /*
    this if for the fancy dropdown.
     */
    /*$("select[id='selectpicker']").selectpicker({style: 'btn-lg btn-primary'});*/

    /*
    this is for formatting phone numbers.
     */
    $("#phone,#fax,#point_of_contact_phone,.phone_number").mask("(999) 999-9999");


    /*
     START  http://hhlearn.dev.oddovo.net:8081/dashboard/admin/setup/organization_1_6
     */

    function cloneMore(selector, type, box_number) {
        var newElement = $(selector).clone(true);

       var total = $('#id_' + type + '-TOTAL_FORMS').val();


       var temp = parseInt(total);


        newElement = newElement.attr('id','official_box_'+temp);



        newElement.find("[name|='officials']").each(function() {
            var name = $(this).attr('name').replace('-' + (box_number) + '-','-' + temp + '-');
            var id = 'id_' + name;
            $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
        });
        newElement.find('label').each(function() {
            var newFor = $(this).attr('for').replace('-' + (box_number) + '-','-' + temp + '-');
            $(this).attr('for', newFor);
        });
        total++;
        $('#id_' + type + '-TOTAL_FORMS').val(total);
        $(selector).after(newElement);

    }

    $(".add_official_box").click(function(event,target) {

        event.preventDefault();

        var box_to_select = '#official_box_'+event.target.id;

        var box_number =  parseInt(event.target.id);

        $(this).attr('id',$('#id_officials-TOTAL_FORMS').val().toString());

        cloneMore(box_to_select, 'officials', box_number);


    });

});