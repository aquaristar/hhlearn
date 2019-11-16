angular.module("history").controller('historyController', ['$modal', '$rootScope', '$scope', '$sce', '$filter', '$location', '$base64', '$timeout', 'historyFactory', 'utilServices', 
function ($modal, $rootScope, $scope, $sce, $filter, $location, $base64, $timeout, historyFactory, utilServices) {

    /*
     This will hold data for test history node.
     */
    $scope.isCollapsed = true;
    
    $scope.testHistory = {};    
    $scope.perPage = 10;    
    $scope.testHistorySearchKeywords = '';
    $scope.currentTestHistoryPage = 1;    
    $scope.filteredTestHistory = [];    
    $scope.testHistorySort = '-completed';
    
    /*
     This will hold data for inservice history node.
     */
    $scope.inserviceHistory = {};    
    $scope.inservicePerPage = 10;    
    $scope.inserviceHistorySearchKeywords = '';
    $scope.currentInserviceHistoryPage = 1;    
    $scope.filteredInserviceHistory = [];    
    $scope.inserviceHistorySort = 'inservices.inservice_title';
    
    /*
     This will hold data for external courses. 
     */
    $scope.ecourseHistory = {};    
    $scope.ecoursePerPage = 10;    
    $scope.ecourseHistorySearchKeywords = '';
    $scope.currentEcourseHistoryPage = 1;    
    $scope.filteredEcourseHistory = [];    
    $scope.ecourseHistorySort = 'external_courses.external_courses_id';


    
    $scope.currentTestAttempt = {};
    
    $scope.row = '';
    
    $scope.tzCode = '';
    
    $scope.Math = Math;
    
	
	 /**
     * Encode course number
     * @param course_code
     * @returns {*}
     */
    $scope.scrollToTop = function () {
    	alert("Asdf");
        return;
    }
    
    $scope.to_trusted = function (html_code) {
        return utilServices.to_trusted(html_code);
    }
    
    
    $scope.encode = function (course_code) {

        return $base64.encode(course_code);
    }
    
	$scope.onFilterChange = function() {
	    $scope.selectTestHistoryPage(1);
	    $scope.currentTestHistoryPage = 1;
	    return $scope.row = '';
	};
	$scope.onNumPerPageChange = function() {
	    $scope.selectTestHistoryPage(1);
	    return $scope.currentTestHistoryPage = 1;
	};
	$scope.onOrderChange = function() {
	    $scope.selectTestHistoryPage(1);
	    return $scope.$scope.testHistory = 1;
	};
	$scope.searchTestHistory = function() {
	    $scope.filteredTestHistory = $filter('filter')($scope.testHistory, $scope.testHistorySearchKeywords);
	    return $scope.onFilterChange();
	};
	/*$scope.order = function(rowName) {
	    if ($scope.row === rowName) return;
	    $scope.row = rowName;
	    $scope.currentFilteredHistories = $filter('orderBy')($scope.testHistory, rowName);
	    return $scope.onOrderChange();
	};*/
	
	$scope.selectTestHistoryPage = function (page) {
        var end, start;
        start = (page - 1) * $scope.perPage;
        end = start + $scope.perPage;
        return $scope.currentFilteredTestHistories = $scope.filteredTestHistory.slice(start, end);        
    };
    
	//inservice functions
	$scope.onInserviceFilterChange = function() {
	    $scope.selectInserviceHistoryPage(1);
	    $scope.currentInserviceHistoryPage = 1;
	    return $scope.row = '';
	};	
	$scope.onInserviceOrderChange = function() {
	    $scope.selectInserviceHistoryPage(1);
	    return $scope.$scope.inserviceHistory = 1;
	};
    $scope.selectInserviceHistoryPage = function (page) {
        var end, start;
        start = (page - 1) * $scope.inservicePerPage;
        end = start + $scope.inservicePerPage;
        return $scope.currentFilteredInserviceHistories = $scope.filteredInserviceHistory.slice(start, end);        
    };
    
    $scope.searchInserviceHistory = function() {
	    $scope.filteredInserviceHistory = $filter('filter')($scope.inserviceHistory, $scope.inserviceHistorySearchKeywords);
	    return $scope.onInserviceFilterChange();
	};
	/*$scope.order = function(rowName) {
	    if ($scope.row === rowName) return;
	    $scope.row = rowName;
	    $scope.currentFilteredHistories = $filter('orderBy')($scope.testHistory, rowName);
	    return $scope.onOrderChange();
	};*/
    

    $scope.selectInserviceHistoryPage = function (page) {
        var end, start;
        start = (page - 1) * $scope.inservicePerPage;
        end = start + $scope.inservicePerPage;
        return $scope.currentFilteredInserviceHistories = $scope.filteredInserviceHistory.slice(start, end);        
    };
    
    
    //External Courses functions
	$scope.onEcourseFilterChange = function() {
	    $scope.selectEcourseHistoryPage(1);
	    $scope.currentEcourseHistoryPage = 1;
	    return $scope.row = '';
	};	
	$scope.onEcourseOrderChange = function() {
	    $scope.selectEcourseHistoryPage(1);
	    return $scope.$scope.ecourseHistory = 1;
	};
    $scope.selectEcourseHistoryPage = function (page) {
        var end, start;
        start = (page - 1) * $scope.ecoursePerPage;
        end = start + $scope.ecoursePerPage;
        return $scope.currentFilteredEcourseHistories = $scope.filteredEcourseHistory.slice(start, end);        
    };
    
    $scope.searchEcourseHistory = function() {
	    $scope.filteredEcourseHistory = $filter('filter')($scope.ecourseHistory, $scope.ecourseHistorySearchKeywords);
	    return $scope.onEcourseFilterChange();
	};
	/*$scope.order = function(rowName) {
	    if ($scope.row === rowName) return;
	    $scope.row = rowName;
	    $scope.currentFilteredHistories = $filter('orderBy')($scope.testHistory, rowName);
	    return $scope.onOrderChange();
	};*/
    

    $scope.selectEcourseHistoryPage = function (page) {
        var end, start;
        start = (page - 1) * $scope.ecoursePerPage;
        end = start + $scope.ecoursePerPage;
        return $scope.currentFilteredEcourseHistories = $scope.filteredEcourseHistory.slice(start, end);        
    };
    
    
    $scope.changeDateFormat = function (date, format) {
    	return moment(date).format(format);
    };
    
    $scope.setCurrentTestAttempt = function (obj) {    	
    	
    	try {
            
            historyFactory.APIGetTestAttemptDetail({'testAttemptID': obj.id}).then(function (data) {
                /*
                 Assigning test related data.
                 */
                $scope.currentTestAttempt = data.testAttemptData; 
                $scope.currentTestAttempt.correct_percentage = Math.round($scope.currentTestAttempt.correct_questions_count / $scope.currentTestAttempt.total_questions_count * 100)                           	
                var modalInstance = $modal.open({
			      templateUrl: 'my.html',
			      controller: 'historyModalInstanceCtrl',			      		      
			      resolve: {
			        currentTestAttempt: function () {
			          return $scope.currentTestAttempt;
			        }
			      }
			    });
                
			    
            });
       } catch (err) {
            $scope.currentTestAttempt = false;
       }
    }    
    
    /*
     Load test - This is our main method will be called on page load.
     */
    $scope.loadTestHistory = function () {
        /*
         This will split the URL into array.
         sample: http://hhlearn.dev.oddovo.net:8081/dashboard/courses/TVMwMTA5/
         */
        var courseCodeEncypted = document.URL.split('/')

        try {
            
            historyFactory.APIGetTestHistory({}).then(function (data) {
                /*
                 Assigning test related data.
                 */
                $scope.testHistory = data.courseData;
                $scope.testHistory = $filter('orderBy')($scope.testHistory, 'completed', true)
                $scope.tzCode = data.tzCode;
                $scope.isDst = data.isDst;
                $scope.searchTestHistory();
            	$scope.selectTestHistoryPage($scope.currentTestHistoryPage);
            	
            	
            	$scope.inserviceHistory = data.inservicesData;
                $scope.searchInserviceHistory();
            	$scope.selectInserviceHistoryPage($scope.currentInserviceHistoryPage);
            	
            	$scope.ecourseHistory = data.externalCourseData;
                $scope.searchEcourseHistory();
            	$scope.selectEcourseHistoryPage($scope.currentEcourseHistoryPage);
            	
            	
            	/*$scope.testHistory = data.courseData;                
                $scope.tzCode = data.tzCode;
                $scope.searchTestHistory();
            	$scope.selectTestHistoryPage($scope.currentTestHistoryPage);*/
            	
                /*
                 Just scroll the page to top :)
                 */
                utilServices.scrollToTop();                

            });
        }
            /*
             If something goes wrong... then just set Course Data to false and we will take care of rest on HTML side.
             */
        catch (err) {
            $scope.courseData = false;
        }

    };
    
    $scope.getTzCode = function(t) {
    	if ($scope.isDst == true) {
	    	if ($rootScope.isInDST(t) == true) {    		
	    		return $scope.tzCode[1];
	    	} else {
	    		return $scope.tzCode[0];
	    	}
    	}
    	return $scope.tzCode[0];
    }
    
    $scope.loadTestHistory();    

}]);

angular.module('history').controller('historyModalInstanceCtrl', function ($scope, $modalInstance, currentTestAttempt) {

  $scope.currentTestAttempt = currentTestAttempt;  
  $scope.cancel = function () {
    $modalInstance.dismiss('cancel');
  };
});

$(function(){
    $('.slim-test-attempts').slimScroll({
        height: '250px'
    });    
});
