angular.module("users").factory("userFactory", ['$http', '$q', function ($http, $q) {

    var factory = {};
    
    /**
     * The method to get user info or meta info
     *  1. if user_id is not null then get user info for this id
     *  2. if user_id is -1 then get meta info for adding user  
     */
    factory.APIGetAllUsers = function (options) {
        var d = $q.defer();
        var defaults = {
           "format": "json"
        };
        $http.get("/api/users", { params: _.extend(defaults, options)}).success(function (data) {
            d.resolve(data);
        });
        return d.promise;
    };
    
    /**
     * The method to get user info
     */
    factory.APIGetUser = function (options) {
        var d = $q.defer();
        var defaults = {
           "format": "json"
        };
        $http.get("/api/user", { params: _.extend(defaults, options)}).success(function (data) {
            d.resolve(data);
        });
        return d.promise;
    };
    
    /**
     * The method to get user info
     */
    factory.APIChangeUser = function (options) {
        var d = $q.defer();
        var defaults = {
            "format": "json",               
        };
        $http.post("/api/user/", _.extend(defaults, options)).success(function (data, status, headers, config) {
            d.resolve(data, status, headers, config);
        }).error(function (data, status, headers, config) {
            d.resolve(data, status, headers, config);
        }).finally(function (data, status, headers, config) {
            d.resolve(data, status, headers, config);
        });    
        return d.promise;
    };
    
    /**
     * The method to get user info or meta info
     *  1. if user_id is not null then get user info for this id
     *  2. if user_id is -1 then get meta info for adding user  
     */
    factory.APIGetAddEditInfo = function (options) {
        var d = $q.defer();
        var defaults = {
           "format": "json"
        };
        $http.get("/api/user/add_edit", { params: _.extend(defaults, options)}).success(function (data) {
            d.resolve(data);
        });
        return d.promise;
    };
    
    /**
     * The Method to add new user or change user
     */
    factory.APIAddEditUser = function (options) {    
        var d = $q.defer();
        var fd = new FormData();
        fd.append( "format", "json" );
        fd.append( "profile", angular.toJson(options.profile));
        fd.append( "file", options.files[0]);
        fd.append( "method", options.method);        
        
        $http.post("/api/user/add_edit/", fd, {
            transformRequest: angular.identity,
            headers: {'Content-Type': undefined}
        }).success(function (data, status, headers, config) {
            d.resolve(data, status, headers, config);
        }).error(function (data, status, headers, config) {
            d.resolve(data, status, headers, config);
        }).finally(function (data, status, headers, config) {
            d.resolve(data, status, headers, config);
        });    
        return d.promise;
    };

    /**
     * The method to get user info or meta info
     *  1. if user_id is not null then get user info for this id
     *  2. if user_id is -1 then get meta info for adding user
     */
    factory.APIGetCoursesList = function (options) {
        var d = $q.defer();
        var defaults = {
           "format": "json"
        };
        $http.get("/api/assignment_courses_list", { params: _.extend(defaults, options)}).success(function (data) {
            d.resolve(data);
        });
        return d.promise;
    };
    
   
    return factory;
}]);