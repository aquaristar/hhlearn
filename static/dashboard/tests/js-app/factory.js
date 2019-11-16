angular.module("tests").factory("testFactory", ['$http', '$q', function ($http, $q) {

    var factory = {};


    factory.APIGetTest = function (options) {
        var d = $q.defer();
        var defaults = {
           "format": "json"
        };
        $http.get("/api/tests/", { params: _.extend(defaults, options)}).success(function (data) {
            d.resolve(data);
        });
        return d.promise;
    };
    
    factory.APIGetAllTest = function (options) {
        var d = $q.defer();
        var defaults = {
           "format": "json"
        };
        $http.get("/api/tests/all/", { params: _.extend(defaults, options)}).success(function (data) {
            d.resolve(data);
        });
        return d.promise;
    };
    
    factory.APIEndTest = function (options) {
        var d = $q.defer();
        var defaults = {
           "format": "json"
        };
        $http.get("/api/test/end", { params: _.extend(defaults, options)}).success(function (data) {
            d.resolve(data);
        });
        return d.promise;
    };
    
    factory.APITestResult = function (options) {
        var d = $q.defer();
        var defaults = {
           "format": "json"
        };
        $http.get("/api/test/result", { params: _.extend(defaults, options)}).success(function (data) {
            d.resolve(data);
        });
        return d.promise;
    };
    
    factory.APITestChange = function (options) {    
        var d = $q.defer();
        var defaults = {
            "format": "json",               
        };
        $http.post("/api/tests/", _.extend(defaults, options)).success(function (data, status, headers, config) {
            d.resolve(data, status, headers, config);
        }).error(function (data, status, headers, config) {
            d.resolve(data, status, headers, config);
        }).finally(function (data, status, headers, config) {
            d.resolve(data, status, headers, config);
        });    
        return d.promise;
    }
    
    factory.APIGetTestData = function (options) {
    	var d = $q.defer();
        var defaults = {
           "format": "json"
        };
        $http.get("/api/test/add_edit", { params: _.extend(defaults, options)}).success(function (data) {
            d.resolve(data);
        });
        return d.promise;
    }
    
    factory.APISaveTest = function (options) {
    	var d = $q.defer();
        var defaults = {
           "format": "json"
        };
        $http.post("/api/test/add_edit/", _.extend(defaults, options)).success(function (data, status, headers, config) {
            d.resolve(data, status, headers, config);
        }).error(function (data, status, headers, config) {
            d.resolve(data, status, headers, config);
        }).finally(function (data, status, headers, config) {
            d.resolve(data, status, headers, config);
        });
        return d.promise;
    }
    
    factory.APIChangeTestQuestion = function (options) {
    	var d = $q.defer();
        var defaults = {
           "format": "json"
        };
        $http.post("/api/test/question/", _.extend(defaults, options)).success(function (data, status, headers, config) {
            d.resolve(data, status, headers, config);
        }).error(function (data, status, headers, config) {
            d.resolve(data, status, headers, config);
        }).finally(function (data, status, headers, config) {
            d.resolve(data, status, headers, config);
        });
        return d.promise;
    }
    
    factory.APIGetTestQuestion = function(options) {
    	var d = $q.defer();
        var defaults = {
           "format": "json"
        };
        $http.get("/api/test/question/", { params: _.extend(defaults, options)}).success(function (data) {
            d.resolve(data);
        });
        return d.promise;
    }
    
    factory.APIGetCountyFips = function(options) {
    	var d = $q.defer();
        var defaults = {
           "format": "json"
        };
        $http.get("/api/test/question/county_fips", { params: _.extend(defaults, options)}).success(function (data) {
            d.resolve(data);
        });
        return d.promise;
    }

    return factory;
}]);