$( document ).ready(function() {
    $("[data-toggle=tooltip]").tooltip();
    $("[data-toggle=popover]").popover();


    /*JS print click handler*/
    $("#glossary-words").on('click', '.print', function(){

        //get the modal box content and load it into the printable div
        $(".printable").html(
            $("#glossary-words").html()                        
        );
        $(".printable .modal-footer").remove();
//fire the print method
        //window.print();
        $(".printable").printElement(
            {
            overrideElementCSS:[
		'thisWillBeTheCSSUsed.css',
		{ href:'/static/dashboard/common/css/style.css',media:'print'}]
            });      
    });
    
    /*JS print click handler*/
    $("#referralAgencies").on('click', '.print', function(){

        //get the modal box content and load it into the printable div
        $(".printable").html(
            $("#referralAgencies").html()
        );
//fire the print method
        //window.print();
        $(".printable .modal-footer").remove();
        
        $(".printable").printElement(
            {
            overrideElementCSS:[
		'thisWillBeTheCSSUsed.css',
		{ href:'/static/dashboard/common/css/style.css',media:'print'}]
            });
    });
    
    
    /*JS print click handler*/
    //$("#courseNotes").on('click', '.print', function(){
    function printCourseNotes() {
        //get the modal box content and load it into the printable div
        $("#p_course_notes").html($("#text_course_notes").val());
        $("#p_course_notes").show();
        $("#text_course_notes").hide();
        $(".printable").html(
            $("#courseNotes").html()
        );
        $(".printable .modal-footer").remove();
//fire the print method
        //window.print();

        $(".printable").printElement(
            {
                overrideElementCSS: [
                    'thisWillBeTheCSSUsed.css',
                    { href: '/static/dashboard/common/css/style.css', media: 'print'}]
            });

        $("#p_course_notes").hide();
        $("#text_course_notes").show();
    }
    //});
    
        /*JS print click handler*/
    $("#appendixModal").on('click', '.print', function() {

        //get the modal box content and load it into the printable div
        $(".printable").html(
            $("#appendixModal").html()
        );
        $(".printable .modal-footer").remove();
//fire the print method
        //window.print();
        
        $(".printable").printElement(
            {
            overrideElementCSS:[
		'thisWillBeTheCSSUsed.css',
		{ href:'/static/dashboard/common/css/style.css',media:'print'}]
            });
        
    });

});

function printCourseNotes() {
    //get the modal box content and load it into the printable div
    $(".p_course_notes").html($(".text_course_notes").val());
    $(".p_course_notes").show();
    $(".text_course_notes").hide();
    $(".printable").html(
        $('.print-window').html()
    );
    $(".printable .modal-footer").remove();
//fire the print method
    //window.print();

    $(".printable").printElement(
        {
            overrideElementCSS: [
                'thisWillBeTheCSSUsed.css',
                { href: '/static/dashboard/common/css/style.css', media: 'print'}]
        });

    $(".p_course_notes").hide();
    $(".text_course_notes").show();
}


function printWindow() {
    //get the modal box content and load it into the printable div
    $(".printable").html(
        $('.print-window').html()
    );
    $(".printable .modal-footer").remove();
    //fire the print method
    //window.print();

    $(".printable").printElement(
        {
        overrideElementCSS:[
    'thisWillBeTheCSSUsed.css',
    { href:'/static/dashboard/common/css/style.css',media:'print'}]
        });

}