angular.module("course").factory("courseFactory", ['$http', '$q', function ($http, $q) {

    var factory = {};


    factory.APIGetCourse = function (options) {

        var d = $q.defer();

        var defaults = {
           "format": "json"
           // "SORT": "name",
           // "PAGENUMBER": "1"
        };

        $http.get("/api/courses/", { params: _.extend(defaults, options)}).success(function (data) {

            d.resolve(data);
        });

        return d.promise;
    };
	
	factory.APITestStart = function (options) {

        var d = $q.defer();

        var defaults = {
           "format": "json",
           "courseID": "",
           "monthlySafetyCourse": ""
        };

        $http.get("/api/test/start/", { params: _.extend(defaults, options)}).success(function (data, status, headers, config) {

            d.resolve(data, status, headers, config);

        }).error(function (data, status, headers, config) {

            d.resolve(data, status, headers, config);

        }).finally(function (data, status, headers, config) {

            d.resolve(data, status, headers, config);


        });
	

        return d.promise;
    };

	/*
	 * save font-size
	 */
	factory.APISaveFontSize = function (options) {

        var d = $q.defer();

        var defaults = {
            "format": "json",               
        };

        $http.post("/api/courses/", _.extend(defaults, options)).success(function (data, status, headers, config) {

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