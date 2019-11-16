angular.module('documents', []).config(function ($interpolateProvider, $locationProvider){
	
	$interpolateProvider.startSymbol('{[');

    $interpolateProvider.endSymbol(']}');
}).run(function($rootScope,$http, $cookies, editableOptions) {

    editableOptions.theme = 'bs3';

    //  Focr CSRF token compatibility with Django
    $http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];

});