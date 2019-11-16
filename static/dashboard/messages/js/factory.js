angular.module("messages").factory("messagesFactory", ['$http', '$q', function ($http, $q) {

    var factory = {};


    factory.APIGetMessages = function (options) {

        var d = $q.defer();

        var defaults = {
           "format": "json"
           // "SORT": "name",
           // "PAGENUMBER": "1"
        };

        $http.get("/api/v1/messages", { params: _.extend(defaults, options)}).success(function (data) {

            d.resolve(data);
        });

        return d.promise;
    };
    
    factory.APIMessageChange = function (options) {

        var d = $q.defer();

        var defaults = {
           "format": "json"
           // "SORT": "name",
           // "PAGENUMBER": "1"
        };

        $http.post("/api/v1/messages", _.extend(defaults, options)).success(function (data, status, headers, config) {

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