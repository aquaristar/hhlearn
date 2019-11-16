angular.module("profileApp").factory("profileFactory", ['$http', '$q', function ($http, $q) {

    var factory = {};

    factory.APIProfile = function (options) {

        var d = $q.defer();

        var defaults = {
            "format": "json"
        };

        $http.get("/api/v1/profile", {params:_.extend(defaults, options)}).success(function (data, status, headers, config) {

            d.resolve(data, status, headers, config);

        }).error(function (data, status, headers, config) {

            d.resolve(data, status, headers, config);

        }).finally(function (data, status, headers, config) {

            d.resolve(data, status, headers, config);

        });

        return d.promise;
    };

    factory.APISaveProfile = function (options) {

        var d = $q.defer();

        var defaults = {
            "format": "json",
            "email": "",
            "first_name": "",
            "last_name": "",
            "address": "",
            "city": "",
            "state": "",
            "postal_code": "",
            "country": "",
            "phone": ""
        };

        $http.post("/api/v1/profile", _.extend(defaults, options)).success(function (data, status, headers, config) {

            d.resolve(data, status, headers, config);

        }).error(function (data, status, headers, config) {

            d.resolve(data, status, headers, config);

        }).finally(function (data, status, headers, config) {

            d.resolve(data, status, headers, config);

        });

        return d.promise;
    };


    factory.APIProfileMin = function (options) {

        var d = $q.defer();

        var defaults = {
            "format": "json",
            "username": "",
            "account_name": "",
            "password": "",
            "rememberMe": true
        };

        $http.get("/api/v1/profile/min",  _.extend(defaults, options)).success(function (data, status, headers, config) {

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