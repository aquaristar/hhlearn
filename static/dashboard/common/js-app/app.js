angular.module('dashboardApp', ['loginApp','signupApp','resetApp','langApp','profileApp',
								'assignmentsApp', 'xeditable' ,'ngResource', 'ngCookies','utilsApp', 
								'base64', 'ui.bootstrap', 'course', 'tests', 'history', 'metrics', 
								'documents', 'tasks', 'academic', 'angularSpinner', 'app.chart.ctrls',
								'app.chart.directives', 'ui.bootstrap', 'ngMap', 'easypiechart',
								'alerts', 'messages', 'users'])
.config(function ($interpolateProvider, $locationProvider, $httpProvider) {
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

}).run(function($rootScope, $http, $cookies, editableOptions) {

    editableOptions.theme = 'bs3';

    //  Focr CSRF token compatibility with Django
    $http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
    
    $rootScope.isInDST = function(t) {
    	if (t == undefined) return false;
    	var date = new Date(Date.parse(t));    	
        var dow = date.getUTCDay();
        var month = date.getUTCMonth() + 1;
        var day = date.getUTCDate();
        var hour = date.getUTCHours();
	    //January, february, a																																																																																																																																																																																																																																																																																																																																																				nd december are out.
	    if (month < 3 || month > 11) return false;
	    //April to October are in
	    if (month > 3 && month < 11) return true;
	    var previousSunday = day - dow
	    //In march, we are DST if our previous sunday was on or after the 8th.    
	    if (month == 3) { 
	        if (previousSunday >= 8){
	            if (day == previousSunday && previousSunday < 15 && hour < 2) return false;
	            return true;
	        }
	    }        
	    //In november we must be before the first sunday to be dst.
	    //That means the previous sunday must be before the 1st.
	    if (previousSunday <= 0) return true;																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																											
	    if (previousSunday <= 7 && day == previousSunday && hour < 2) return true;
	    return false;    	
    }

});
