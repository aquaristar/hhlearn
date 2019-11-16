$(function() {

    $("select[name='state']").selectpicker({style: 'btn-lg btn-primary'});
    $("select[name='country']").selectpicker({style: 'btn-lg btn-primary'});
    $("select[name='company_type']").selectpicker({style: 'btn-lg btn-primary'});
    $("select[name='lead_id']").selectpicker({style: 'btn-lg btn-primary'});
    $("select[name='module_consistent']").selectpicker({style: 'btn-lg btn-primary'});
    $("select[name='services_consistent']").selectpicker({style: 'btn-lg btn-primary'});
    $("select[name='grade_consistent']").selectpicker({style: 'btn-lg btn-primary'});
    $("select[name='job_titles_consistent']").selectpicker({style: 'btn-lg btn-primary'});
    $("select[name='company_accredited']").selectpicker({style: 'btn-lg btn-primary'});
    $("select[name='entire_company_accredited']").selectpicker({style: 'btn-lg btn-primary'});
    $("select[name='accreditation_consistent']").selectpicker({style: 'btn-lg btn-primary'});
    $("select[name='accreditation_aganecy']").selectpicker({style: 'btn-lg btn-primary'});
    $("select[name='use_monthly_safety_courses']").selectpicker({style: 'btn-lg btn-primary'});
    $("select[name='use_electronic_postings']").selectpicker({style: 'btn-lg btn-primary'});
    $("select[name='electronic_postings_consistent']").selectpicker({style: 'btn-lg btn-primary'});
    $("select[name='store_ssn']").selectpicker({style: 'btn-lg btn-primary'});
    $("select[name='use_custom_employee_id']").selectpicker({style: 'btn-lg btn-primary'});



    // jQuery UI Datepicker
    var datepickerSelector = '#date_added,#date_activated,#next_recurring_date';
    $(datepickerSelector).datepicker({
        showOtherMonths: true,
        selectOtherMonths: true,
        dateFormat: "d MM, yy",
        yearRange: '-1:+1'
    }).prev('.btn').on('click', function (e) {
            e && e.preventDefault();
            $(datepickerSelector).focus();
        });
    $.extend($.datepicker, {_checkOffset:function(inst,offset,isFixed){return offset}});

    // Now let's align datepicker with the prepend button
    $(datepickerSelector).datepicker('widget').css({'margin-left': -$(datepickerSelector).prev('.input-group-btn').find('.btn').outerWidth()});



})(jQuery);