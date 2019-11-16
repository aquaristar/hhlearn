$(function () {
	$(window).scroll(function () {
		if ($(this).scrollTop() != 0) {
			$('#toTop').fadeIn();
		} else {
			$('#toTop').fadeOut();
		}
	});

	$('#toTop').click(function () {
		$('body,html').animate({scrollTop : 0}, 500);
	});

});

<!-- Toggle -->
$('.togglehandle').click(function () {
	$(this).toggleClass('active')
	$(this).next('.toggledata').slideToggle()
});

// alert close 
$('.clostalert').click(function () {
	$(this).parent('.alert').fadeOut()
});

<!-- Tooltip -->
$('.tooltip-test').tooltip();

<!-- Accrodian -->
var $acdata = $('.accrodian-data'),
	$acclick = $('.accrodian-trigger');

$acdata.hide();
$acclick.first().addClass('active').next().show();

$acclick.on('click', function (e) {
	if ($(this).next().is(':hidden')) {
		$acclick.removeClass('active').next().slideUp(300);
		$(this).toggleClass('active').next().slideDown(300);
	}
	e.preventDefault();
});

<!-- News stip clickable-->
$(".news-strip ul li").click(function () {
	window.location = $(this).find("a").attr("href");
	return false;
});

$(".clientTestimonial img,.customerTestimonial img").click(function (e) {

	$("#txt-companyname").html($(this).data("companyname"));
	$("#txt-employeename").html($(this).data("employeename"));
	$("#txt-employeeposition").html($(this).data("employeeposition"));
	$("#txt-employeecount").html($(this).data("employeecount"));
	$("#txt-locationcount").html($(this).data("locationcount"));
	$("#txt-description").html($(this).data("description"));
	$("#videolink").attr('src', $(this).data("videolink"));

	//alert($(this).data( "videolink" ));
});

$('#clientTestimonial').carousel({
	interval : 2000
})
$('#customerTestimonial').carousel({
	interval : 2000
})

$(".demo-tutorial img").click(function (e) {

	$("#videolink").attr('src', $(this).data("videolink"));

	//alert($(this).data( "videolink" ));
});

var videoID = document.URL.split('#')[1];

if ($("#" + videoID).length != 0) {
	$("#videolink").attr('src', $("#" + videoID).data("videolink"));
}

$("[rel='tooltip']").tooltip();


// Javascript to enable link to tab
var url = document.location.toString();
if (url.match('#')) {

	$('.nav-tabs a[href=#'+url.split('#')[1]+']').tab('show') ;

	e.preventDefault();
}

// Change hash for page-reload
$('.nav-tabs a').on('shown', function (e) {
	window.location.hash = e.target.hash;
})
	
