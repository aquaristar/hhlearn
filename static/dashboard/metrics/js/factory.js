angular.module("metrics").factory("metricsFactory", ['$http', '$q', function ($http, $q) {

    var factory = {};


    factory.APIGetMetrics = function (options) {

        var d = $q.defer();

        var defaults = {
           "format": "json"
           // "SORT": "name",
           // "PAGENUMBER": "1"
        };

        $http.get("/api/v1/metrics", { params: _.extend(defaults, options)}).success(function (data) {

            d.resolve(data);
        });

        return d.promise;
    };

    return factory;
}]);