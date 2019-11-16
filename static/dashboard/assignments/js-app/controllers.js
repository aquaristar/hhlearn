angular.module("assignmentsApp").controller('assignmentsCtrl', ['$scope', '$sce', '$filter', '$base64', 'logger', 'assignmentsFactory', function ($scope, $sce, $filter, $base64, logger, assignmentsFactory) {


    $scope.apiResponse = {};

    $scope.assignmentsFactory = assignmentsFactory;

    $scope.logger = logger;

    $scope.assignments = {};

    $scope.safety_assignments = {};

    $scope.assignmentSearchKeyword = '';

    $scope.safetyAssignmentSearchKeyword = '';

    /**
     * number of users per page.
     */
    $scope.perPage = 10;

    /**
     * page number.
     */
    $scope.assignmentPageNumber = 1;

    $scope.safetyAssignmentPageNumber = 1;


    $scope.filteredAssignments = [];

    $scope.filteredSafteyAssignments = [];

    $scope.assignmentSort = 'due_date';

    $scope.safetyAssignmentSort = 'due_date';


    /**
     * Encode course number
     * @param course_code
     * @returns {*}
     */
    $scope.encode = function (course_code) {

        return $base64.encode(course_code);
    }


    /**
     * this brings back list of available groups in org when user clicks on ADD NEW USER
     */
    $scope.getAssignmentList = function () {

        /**
         * calling method in factory to make API call.
         */
        $scope.assignmentsFactory.APIGetAssignmentList().then(function (response) {

            /**
             * storing response form api.
             */
            $scope.apiResponse = response.data;

            $scope.assignments = response.data.assignments;
            $scope.assignments = $filter('orderBy')($scope.assignments, '-due_date', true)

            $scope.safety_assignments = response.data.safety_assignments;
			
			$scope.searchAssignment();
            $scope.selectAssignmentPage($scope.assignmentPageNumber);
            
            $scope.selectSafetyAssignmentPage($scope.safetyAssignmentPageNumber);

            if (!_.isUndefined($scope.apiResponse.response)) {
                /**
                 * log message and show notification on screen.
                 */
                $scope.logger.logCustom($scope.apiResponse.response.message, $scope.apiResponse.response.status)
            }


        });

    };


	$scope.onFilterChange = function() {
	    $scope.selectAssignmentPage(1);
	    $scope.assignmentPageNumber = 1;
	    return $scope.row = '';
	};
	
	$scope.onOrderChange = function(exp, reverse) {
		$scope.filteredAssignments = $filter('orderBy')($scope.assignments, exp, false)
	    $scope.selectAssignmentPage(1);
	    $scope.assignmentPageNumber = 1;
	    return $scope.row = '';
	};
	
	$scope.searchAssignment = function() {
		//$scope.assignmentSearchKeyword = $('#alert_search').val();		
	    $scope.filteredAssignments = $filter('filter')($scope.assignments, $scope.assignmentSearchKeyword);
	    return $scope.onFilterChange();
	};
    $scope.selectAssignmentPage = function (page) {        
        var end, start;
        start = (page - 1) * $scope.perPage;
        end = start + $scope.perPage;
        return $scope.currentFilteredAssignments = $scope.filteredAssignments.slice(start, end);
    };


    $scope.selectSafetyAssignmentPage = function (page) {
        var end, start;
        start = (page - 1) * $scope.perPage;
        end = start + $scope.perPage;
        return $scope.filteredSafteyAssignments = $filter('filter')($scope.safety_assignments, $scope.safetyAssignmentSearchKeyword).slice(start, end);
    };


    $scope.dateDue = function (number_of_days, date_assigned) {

        return moment(date_assigned).add('days', number_of_days).format("MM/DD/YYYY");
    };

    /**
     * This method is called when user clicks on start assignment button.
     * @param assignment
     * @returns {*}
     */
    $scope.startAssignment = function (assignment) {

         /**
         * assignment start API
         */
        $scope.assignmentsFactory.APICourseStart({assignmentID:assignment.id, courseID:assignment.course.id, monthlySafetyCourse:assignment.course.monthly_safety_course}).then(function (data) {

            /**
             * storing response form api.
             */
            $scope.apiResponse = data;

             if (!_.isUndefined($scope.apiResponse.response)) {
                /**
                 * log message and show notification on screen.
                 */
                $scope.logger.logCustom($scope.apiResponse.response.message, $scope.apiResponse.response.status)

                if ($scope.apiResponse.response.status == "success") {

                        window.location = '/dashboard/course/'+$scope.encode(assignment.course.id)+':'+$scope.encode(assignment.course.monthly_safety_course)+':'+$scope.encode(assignment.id);
                }
            }


        });
    };


    $scope.getAssignmentList();

}]);
