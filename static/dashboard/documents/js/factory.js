angular.module("documents").factory("documentsFactory", ['$http', '$q', function ($http, $q) {

    var factory = {};


    factory.APIGetDocuments = function (options) {

        var d = $q.defer();

        var defaults = {
           "format": "json"
           // "SORT": "name",
           // "PAGENUMBER": "1"
        };

        $http.get("/api/v1/documents", { params: _.extend(defaults, options)}).success(function (data) {

            d.resolve(data);
        });

        return d.promise;
    };

    return factory;
}]);