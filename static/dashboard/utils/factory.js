/**
This module will control all the error messages.

@dependency: $scope             toastr - the main scope
*/
angular.module("utilsApp").factory("logger", ["$http", "$q", function ($http, $q) {

    var factory = {};

    var logIt;

    toastr.options = {
        "closeButton": true,
        "positionClass": "toast-bottom-right",
        "timeOut": "3000"
    };

    logIt = function(message, type) {
        return toastr[type](message);
    };

    factory.logCustom = function(message, type) {
        logIt(message, type);
    };
    factory.log = function(message) {
        logIt(message, 'info');
    };

    factory.logWarning = function(message) {
        logIt(message, 'warning');
    };

    factory.logSuccess = function(message) {
        logIt(message, 'success');
    };

    factory.logError = function(message) {
        logIt(message, 'error');
    };

    return factory;

}]).factory("utilsFactory", ["$http", "$q", function ($http, $q) {

    var factory = {};

    factory.APIToggleMenu = function (options) {

        var d = $q.defer();

        var defaults = {
            "format": "json"
        };

        $http.get("/api/v1/toggle_menu", {params:_.extend(defaults, options)}).success(function (data, status, headers, config) {

            d.resolve(data, status, headers, config);

        }).error(function (data, status, headers, config) {

            d.resolve(data, status, headers, config);

        }).finally(function (data, status, headers, config) {

            d.resolve(data, status, headers, config);

        });

        return d.promise;
    };

    return factory;

}]);