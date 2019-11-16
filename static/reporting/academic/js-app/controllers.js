angular.module("academic").controller('orgComplianceSummaryController', ['$scope', '$sce', '$location', '$base64', '$timeout', 'logger', 'courseFactory', 'utilServices', 'courseServices', function ($scope, $sce, $location, $base64, logger, $timeout, utilServices, courseServices) {

	$scope.logger = logger;
	
	/**
     * Encode String
     * @param course_code
     * @returns {*}
     */
    $scope.encode = function (course_code) {

        return $base64.encode(course_code);
    }

}]);

