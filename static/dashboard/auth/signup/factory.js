angular.module("signupApp").factory("signupFactory", ['$http', '$q', function ($http, $q) {

    var factory = {};

    factory.APIAuthSignup = function (options) {

        var d = $q.defer();

        var defaults = {
            "format": "json",
            "org_name": "",
            "first_name": "",
            "username": "",
            "last_name": "",
            "email": "",
            "password": ""
        };



        $http.post("/api/v1/auth/signup", _.extend(defaults, options)).success(function (data, status, headers, config) {

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