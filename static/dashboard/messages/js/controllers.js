angular.module("messages").controller('messagesController', ['$modal', '$scope', '$sce', 'logger', '$filter', '$location', '$base64', '$timeout', 'messagesFactory', 'utilServices', 
	function ($modal, $scope, $sce, logger, $filter, $location, $base64, $timeout, messagesFactory, utilServices) {

    /*
     This will hold data for test history node.
     */
    $scope.messageData = {};    
    $scope.perPage = 10;
    
    $scope.messageSearchKeywords = '';
    $scope.currentMessagePage = 1;
    $scope.filteredMessages = [];
    $scope.mSort = 'id';
    
    
    $scope.rMessageData = {};    
    $scope.rMessagePerPage = 10;
    
    $scope.rMessageSearchKeywords = '';
    $scope.currentRMessagePage = 1;
    $scope.filtereRdMessages = [];
    $scope.rMessageSort = 'id';
    
    
    $scope.currentMessage = {};
    
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
	    $scope.selectMessagePage(1);
	    $scope.currentMessagePage = 1;
	    return $scope.row = '';
	};
	$scope.onNumPerPageChange = function() {
	    $scope.selectMessagePage(1);
	    return $scope.currentMessagePage = 1;
	};
	$scope.onOrderChange = function() {
	    $scope.selectMessagePage(1);
	    return $scope.$scope.messages = 1;
	};
	$scope.searchMessage = function() {
		$scope.messageSearchKeywords = $('#message_search').val();		
	    $scope.filteredMessages = $filter('filter')($scope.messageData, $scope.messageSearchKeywords);
	    return $scope.onFilterChange();
	};
	/*$scope.order = function(rowName) {
	    if ($scope.row === rowName) return;
	    $scope.row = rowName;
	    $scope.currentFilteredHistories = $filter('orderBy')($scope.testHistory, rowName);
	    return $scope.onOrderChange();
	};*/
	
	$scope.selectMessagePage = function (page) {
        var end, start;
        start = (page - 1) * $scope.perPage;
        end = start + $scope.perPage;
        return $scope.currentFilteredMessages = $scope.filteredMessages.slice(start, end);        
    };
    
    //readed message
    $scope.onRFilterChange = function() {
	    $scope.selectRMessagePage(1);
	    $scope.currentRMessagePage = 1;
	    return $scope.row = '';
	};
	$scope.onNumRPerPageChange = function() {
	    $scope.selectRMessagePage(1);
	    return $scope.currentRMessagePage = 1;
	};
	$scope.onROrderChange = function() {
	    $scope.selectRMessagePage(1);
	    return $scope.$scope.rMessages = 1;
	};
	$scope.searchRMessage = function() {
		$scope.rMessageSearchKeywords = $('#read_message_search').val();
	    $scope.filteredRMessages = $filter('filter')($scope.rMessageData, $scope.rMessageSearchKeywords);
	    return $scope.onRFilterChange();
	};
	/*$scope.order = function(rowName) {
	    if ($scope.row === rowName) return;
	    $scope.row = rowName;
	    $scope.currentFilteredHistories = $filter('orderBy')($scope.testHistory, rowName);
	    return $scope.onOrderChange();
	};*/
	
	$scope.selectRMessagePage = function (page) {
        var end, start;
        start = (page - 1) * $scope.rMessagePerPage;
        end = start + $scope.rMessagePerPage;
        return $scope.currentFilteredRMessages = $scope.filteredRMessages.slice(start, end);        
    };
    
    $scope.changeDateFormat = function (date, format) {
    	return moment(date).format(format);
    };
    
    $scope.setCurrentMessage = function (obj) {
    	
    	$scope.currentMessage = obj;
    	var modalInstance = $modal.open({
			      templateUrl: 'my.html',
			      controller: 'messageModalInstanceCtrl',			      		      
			      resolve: {
			        currentMessage: function () {
			          return $scope.currentMessage;
			        }
			      }
			    });		
    	
    }    
    
    /*
     Load test - This is our main method will be called on page load.
     */
    $scope.loadMessages = function () {
        /*
         This will split the URL into array.
         sample: http://hhlearn.dev.oddovo.net:8081/dashboard/courses/TVMwMTA5/
         */
        var courseCodeEncypted = document.URL.split('/')

        try {
            
            messagesFactory.APIGetMessages({}).then(function (data) {
                /*
                 Assigning test related data.
                 */
                $scope.messageData = data.messages;
                $scope.searchMessage();
            	$scope.selectMessagePage($scope.currentMessagePage);
            	
            	$scope.rMessageData = data.readed_messages;
                $scope.searchRMessage();
            	$scope.selectRMessagePage($scope.currentRMessagePage);
            	
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
            $scope.messageData = false;
        }

    };
    
    $scope.changeMessageStatusToReaded = function(obj, index) {
    	 try {
            
            messagesFactory.APIMessageChange({"message_id": obj.id, "acknowledged": 1}).then(function (data) {
                /*
                 Assigning test related data.
                 */                            	
	            
	            if (data.status = 'success') {	            	
        			$scope.messageData.splice(index, 1);	  
        			$scope.searchMessage();
            		$scope.selectMessagePage($scope.currentMessagePage);
                          			
	            	$scope.rMessageData.push(data.message);
	            	$scope.searchRMessage();
            		$scope.selectRMessagePage($scope.currentRMessagePage);
            		
            		$scope.changeMessageCount();
            			
	            	return logger.log('Message Acknowledged!');
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
    
    $scope.changeMessageCount = function() {
    	if ($scope.messageData.length > 0) {
    		jQuery("#message_count").text($scope.messageData.length);
    	} else {
    		jQuery("#message_count").text("");
    	}
    };

    
    $scope.loadMessages();    

}]);

angular.module('messages').controller('messageModalInstanceCtrl', function ($scope, $modalInstance, currentMessage) {

  $scope.currentMessage = currentMessage;  
  $scope.cancel = function () {
    $modalInstance.dismiss('cancel');
  };
});
