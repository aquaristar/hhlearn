angular.module("alerts").controller('alertsController', ['$modal', '$scope', '$sce', 'logger', '$filter', '$location', '$base64', '$timeout', 'alertsFactory', 'utilServices', 
	function ($modal, $scope, $sce, logger, $filter, $location, $base64, $timeout, alertsFactory, utilServices) {

    /*
     This will hold data for test history node.
     */
    $scope.alertData = {};    
    $scope.perPage = 10;
    
    $scope.alertSearchKeywords = '';
    $scope.currentAlertPage = 1;
    $scope.filteredAlerts = [];
    $scope.alertSort = 'id';
    
    
    $scope.rAlertData = {};    
    $scope.rAlertPerPage = 10;
    
    $scope.rAlertSearchKeywords = '';
    $scope.currentRAlertPage = 1;
    $scope.filtereRdAlerts = [];
    $scope.rAlertSort = 'id';
    
    
    $scope.currentAlert = {};
    
    $scope.row = '';
    
    $scope.tzCode = '';
    
    $scope.Math = Math;
    
	
	 /**
     * Encode course number
     * @param course_code
     * @returns {*}
     */

    $scope.to_trusted = function (html_code) {
        return utilServices.to_trusted(html_code);
    }
    
    $scope.trancateString = function (str) {
    	if (str.length <= 40) {
    		return str;
    	} else{
    		str = str.substring(0, 40) + '...';
    		return str;
    	}
    }
    
    $scope.encode = function (course_code) {

        return $base64.encode(course_code);
    }
    
	$scope.onFilterChange = function() {
	    $scope.selectAlertPage(1);
	    $scope.currentAlertPage = 1;
	    return $scope.row = '';
	};
	$scope.onNumPerPageChange = function() {
	    $scope.selectAlertPage(1);
	    return $scope.currentAlertPage = 1;
	};
	$scope.onOrderChange = function() {
	    $scope.selectAlertPage(1);
	    return $scope.$scope.alerts = 1;
	};
	$scope.searchAlert = function() {
		$scope.alertSearchKeywords = $('#alert_search').val();		
	    $scope.filteredAlerts = $filter('filter')($scope.alertData, $scope.alertSearchKeywords);
	    return $scope.onFilterChange();
	};
	/*$scope.order = function(rowName) {
	    if ($scope.row === rowName) return;
	    $scope.row = rowName;
	    $scope.currentFilteredHistories = $filter('orderBy')($scope.testHistory, rowName);
	    return $scope.onOrderChange();
	};*/
	
	$scope.selectAlertPage = function (page) {
        var end, start;
        start = (page - 1) * $scope.perPage;
        end = start + $scope.perPage;
        return $scope.currentFilteredAlerts = $scope.filteredAlerts.slice(start, end);        
    };
    
    //readed alert
    $scope.onRFilterChange = function() {
	    $scope.selectRAlertPage(1);
	    $scope.currentRAlertPage = 1;
	    return $scope.row = '';
	};
	$scope.onNumRPerPageChange = function() {
	    $scope.selectRAlertPage(1);
	    return $scope.currentRAlertPage = 1;
	};
	$scope.onROrderChange = function() {
	    $scope.selectRAlertPage(1);
	    return $scope.$scope.rAlerts = 1;
	};
	$scope.searchRAlert = function() {
		$scope.rAlertSearchKeywords = $('#read_alert_search').val();
	    $scope.filteredRAlerts = $filter('filter')($scope.rAlertData, $scope.rAlertSearchKeywords);
	    return $scope.onRFilterChange();
	};
	/*$scope.order = function(rowName) {
	    if ($scope.row === rowName) return;
	    $scope.row = rowName;
	    $scope.currentFilteredHistories = $filter('orderBy')($scope.testHistory, rowName);
	    return $scope.onOrderChange();
	};*/
	
	$scope.selectRAlertPage = function (page) {
        var end, start;
        start = (page - 1) * $scope.rAlertPerPage;
        end = start + $scope.rAlertPerPage;
        return $scope.currentFilteredRAlerts = $scope.filteredRAlerts.slice(start, end);        
    };
    
    $scope.changeDateFormat = function (date, format) {
    	return moment(date).format(format);
    };
    
    $scope.setCurrentAlert = function (obj) {
    	$scope.currentAlert = obj;
    	var modalInstance = $modal.open({
			      templateUrl: 'my.html',
			      controller: 'alertModalInstanceCtrl',			      		      
			      resolve: {
			        currentAlert: function () {
			          return $scope.currentAlert;
			        }
			      }
		});
    }    
    
    /*
     Load test - This is our main method will be called on page load.
     */
    $scope.loadAlerts = function () {
        /*
         This will split the URL into array.
         sample: http://hhlearn.dev.oddovo.net:8081/dashboard/courses/TVMwMTA5/
         */
        var courseCodeEncypted = document.URL.split('/')

        try {
            
            alertsFactory.APIGetAlerts({}).then(function (data) {
                /*
                 Assigning test related data.
                 */
                $scope.alertData = data.alerts;
                $scope.searchAlert();
            	$scope.selectAlertPage($scope.currentAlertPage);
            	
            	$scope.rAlertData = data.readed_alerts;
                $scope.searchRAlert();
            	$scope.selectRAlertPage($scope.currentRAlertPage);
            	
            	$scope.tzCode = data.tzCode;
            	
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
            $scope.alertData = false;
        }

    };
    
    $scope.changeAlertStatusToReaded = function(obj, index) {
    	 try {
            
            alertsFactory.APIAlertChange({"alert_id": obj.id, "acknowledged": 1}).then(function (data) {
                /*
                 Assigning test related data.
                 */                            	
	            
	            if (data.status = 'success') {	            	
        			$scope.alertData.splice(index, 1);	  
        			$scope.searchAlert();
            		$scope.selectAlertPage($scope.currentAlertPage);
                          			
	            	$scope.rAlertData.push(data.alert);
	            	$scope.searchRAlert();
            		$scope.selectRAlertPage($scope.currentRAlertPage);
            		
            		$scope.changeAlertCount();
            			
	            	return logger.log('Alert Acknowledged!');
	            } else {
	            	return logger.logError('Error:' + data.response);
	            }
            });
        }
        /*
         If something goes wrong... then just set Course Data to false and we will take care of rest on HTML side.
         */
        catch (err) {
           alert(err);
        }
    };
    
    $scope.changeAlertCount = function() {
    	if ($scope.alertData.length > 0) {
    		jQuery("#alert_count").text($scope.alertData.length);
    	} else {
    		jQuery("#alert_count").text("");
    	}
    };
    
    $scope.loadAlerts();    

}]);

angular.module('alerts').controller('alertModalInstanceCtrl', function ($scope, $modalInstance, currentAlert) {

  $scope.currentAlert = currentAlert;  
  $scope.cancel = function () {
    $modalInstance.dismiss('cancel');
  };
});
