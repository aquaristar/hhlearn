angular.module("assignmentsApp").factory("assignmentsFactory", ['$http', '$q', '$cookies', function ($http, $q, $cookies) {

    var factory = {};

    factory.APIGetAssignmentList = function (options) {

        var d = $q.defer();

        var defaults = {
            "format": "json"
        };

        $http.get("/api/v1/assignments", {params:_.extend(defaults, options)}).success(function (data, status, headers, config) {

            d.resolve(data, status, headers, config);

        }).error(function (data, status, headers, config) {

            d.resolve(data, status, headers, config);

        }).finally(function (data, status, headers, config) {

            d.resolve(data, status, headers, config);


        });

        return d.promise;
    };


    factory.APICourseStart = function (options) {

        var d = $q.defer();

        var defaults = {
           "format": "json",
           "courseID": "",
           "monthlySafetyCourse": ""
        };

        $http.get("/api/course/start/", { params: _.extend(defaults, options)}).success(function (data, status, headers, config) {

            d.resolve(data, status, headers, config);

        }).error(function (data, status, headers, config) {

            d.resolve(data, status, headers, config);

        }).finally(function (data, status, headers, config) {

            d.resolve(data, status, headers, config);


        });


        return d.promise;
    };

        /**
     * The method to get user info
     */
    factory.APICreateAssignment = function (options) {
        var d = $q.defer();
        var defaults = {
            "format": "json"
        };
        var url = "/api/v1/assignments"
        $http.post(url, _.extend(defaults, options)).success(function (data, status, headers, config) {
            d.resolve(data, status, headers, config);
        }).error(function (data, status, headers, config) {
            d.resolve(data, status, headers, config);
        }).finally(function (data, status, headers, config) {
            d.resolve(data, status, headers, config);
        });
        return d.promise;
    };

    /**
     * The method to get user info
     */
    factory.APIEditAssignment = function (options) {
        var d = $q.defer();
        var defaults = {
            "format": "json",
        };

        var url = "/api/v1/assignment" + "/" + options.id;
        $http.put(url, _.extend(defaults, options)).success(function (data, status, headers, config) {
            d.resolve(data, status, headers, config);
        }).error(function (data, status, headers, config) {
            d.resolve(data, status, headers, config);
        }).finally(function (data, status, headers, config) {
            d.resolve(data, status, headers, config);
        });
        return d.promise;
    };

    /**
     * The method to get user info
     */
    factory.APIDeleteAssignment = function (options) {
        var d = $q.defer();
        var defaults = {
            "format": "json",
        };

        var url = "/api/v1/assignment" + "/" + options.id;
        $http.delete(url, _.extend(defaults, options)).success(function (data, status, headers, config) {
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