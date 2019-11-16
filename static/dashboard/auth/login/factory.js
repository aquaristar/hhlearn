angular.module("loginApp").factory("loginFactory", ['$http', '$q', function ($http, $q) {

    var factory = {};

    factory.APIAuthLogin = function (options) {

        var d = $q.defer();

        var defaults = {
            "format": "json",
            "username": "",
            "password": "",
            "rememberMe": true
        };

        $http.post("/api/v1/auth/login", _.extend(defaults, options)).success(function (data, status, headers, config) {

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