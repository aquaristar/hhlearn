/**
 * The controller for Admin Users view page
 */
angular.module("users").controller('usersListController',
['$scope', '$sce', '$location', 'filterFilter', 'logger', '$filter', '$base64', '$timeout', 'userFactory', 'utilServices', 
function ($scope, $sce, $location, filterFilter, logger, $filter, $base64, $timeout, userFactory, utilServices) {
	$scope.tests = [];
	$scope.currentUser = {};
	$scope.is_reactivate = false;
	$scope.is_deactivate = false;
	
	//variables for active users
	$scope.activeUsers = {};
	$scope.perPage = 10;    
    $scope.activeUserSearchKeywords = '';
    $scope.currentActiveUserPage = 1;
    $scope.filteredActiveUsers = {};
    $scope.activeUserSort = 'username';
    
    //variables for inactive users
	$scope.inactiveUsers = {}
	$scope.inactiveUserPerPage = 10;    
    $scope.inactiveUserSearchKeywords = '';
    $scope.currentInactiveUserPage = 1;
    $scope.filteredInactiveUsers = {};
    $scope.inactiveUserSort = 'username';


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
    
    /**
     * functions for active Users
     */
	$scope.onFilterChange = function() {
	    $scope.selectActiveUserPage(1);
	    $scope.currentActiveUserPage = 1;
	    return $scope.row = '';
	};
	$scope.onNumPerPageChange = function() {
	    $scope.selectActiveUserPage(1);
	    return $scope.currentActiveUserPage = 1;
	};

	$scope.onOrderChange = function(exp, reverse) {		
		$scope.filteredActiveUsers = $filter('orderBy')($scope.filteredActiveUsers, exp, false)
	    $scope.selectActiveUserPage(1);
	    $scope.currentActiveUserPage = 1;
	    return $scope.row = '';
	};
	$scope.searchActiveUsers = function() {
		$scope.activeUserSearchKeywords = $('#user_search').val();		
	    $scope.filteredActiveUsers = $filter('filter')($scope.activeUsers, $scope.activeUserSearchKeywords);
	    return $scope.onFilterChange();
	};
	
	$scope.selectActiveUserPage = function (page) {
        var end, start;
        start = (page - 1) * $scope.perPage;
        end = start + $scope.perPage;
        return $scope.currentFilteredActiveUsers = $scope.filteredActiveUsers.slice(start, end);        
    };
    
    /**
     * functions for inactive Users
     */
	$scope.onInactiveUserFilterChange = function() {
	    $scope.selectInactiveUserPage(1);
	    $scope.currentInactiveUserPage = 1;
	    return $scope.row = '';
	};
	$scope.onInactiveUserNumPerPageChange = function() {
	    $scope.selectInactiveUserPage(1);
	    return $scope.currentInactiveUserPage = 1;
	};

	$scope.onInactiveUserOrderChange = function(exp, reverse) {		
		$scope.filteredInactiveUsers = $filter('orderBy')($scope.filteredInactiveUsers, exp, false)
	    $scope.selectInactiveUserPage(1);
	    $scope.currentInactiveUserPage = 1;
	    return $scope.row = '';
	};
	$scope.searchInactiveUsers = function() {
		$scope.inactiveUserSearchKeywords = $('#ia_user_search').val();		
	    $scope.filteredInactiveUsers = $filter('filter')($scope.inactiveUsers, $scope.inactiveUserSearchKeywords);
	    return $scope.onInactiveUserFilterChange();
	};
	
	$scope.selectInactiveUserPage = function (page) {
        var end, start;
        start = (page - 1) * $scope.inactiveUserPerPage;
        end = start + $scope.inactiveUserPerPage;
        return $scope.currentFilteredInactiveUsers = $scope.filteredInactiveUsers.slice(start, end);        
    };
    
    $scope.selectCurrentUser = function (obj) {
    	//initialize modal variables
    	$scope.is_reactivate = false;
    	$scope.is_deactivate = false;
    	//set currentUser object
		$scope.currentUser = obj;
		return;    	
    }    
    
    //Activate User
    $scope.activateUser = function (activate) {
    	if (activate == false) {
    		if ( $scope.is_deactivate == true ) {
    			userFactory.APIChangeUser({"method": "activate", "user_id": $scope.currentUser.id, "is_active": activate }).then(function (data) {
					if (data.status == 'success') {
						$scope.currentUser.is_active = activate;
						$scope.updateAllViews();
						logger.logSuccess("User Deactivated Succesfully");
					}    				
				});
    		}
    	} else {
    		if ( $scope.is_reactivate == true ) {
    			userFactory.APIChangeUser({"method": "activate", "user_id": $scope.currentUser.id, "is_active": activate }).then(function (data) {
					if (data.status == 'success') {
						$scope.currentUser.is_active = activate;
						$scope.updateAllViews();
						logger.logSuccess("User Activated Succesfully");
					}    				
				});
    		}
    	}    	
    	return true;
    } 
    
    $scope.updateAllViews = function() {
    	//prepare users data
    	$scope.activeUsers = filterFilter($scope.users, {
	        is_active: true
	    });
	    $scope.inactiveUsers = filterFilter($scope.users, {
	        is_active: false,
	    });
    	$scope.searchActiveUsers();
    	$scope.selectActiveUserPage($scope.currentActiveUserPage);	        	
    	$scope.searchInactiveUsers();
    	$scope.selectInactiveUserPage($scope.currentInactiveUserPage);
    }
	
	$scope.loadAllUsers = function() {
	  	try {	        
	        userFactory.APIGetAllUsers({}).then(function (data) {	    
	            $scope.users = data.users;
	            $scope.users = $filter('orderBy')($scope.users, '-username', true)
			    //update views
			    $scope.updateAllViews();
	        });
	    }
	    catch (err) {
	        $scope.alertData = false;
	    }
	};
	//first time load all users 
	$scope.loadAllUsers();
}]);

/**
 * The Controller for the Admin Users Add/Edit page
 */
angular.module("users").controller('UserAddEditController',
['$modal', '$scope', '$sce', '$location', 'filterFilter', 'logger', '$filter', '$base64', '$timeout', 'userFactory', 'assignmentsFactory', 'utilServices',
function ($modal, $scope, $sce, $location, filterFilter, logger, $filter, $base64, $timeout, userFactory, assignmentsFactory, utilServices) {
	$scope.user_id = -1;
	$scope.profile = {};
	$scope.job_titles = [];
	$scope.departments = [];
	$scope.locations = [];
	$scope.regions = [];
	$scope.sample_photos = [];
	$scope.modules = [];
	$scope.confirm_password = [];

    $scope.assignments = {};
    $scope.assignmentSearchKeyword = '';
    $scope.minDate = new Date();

    /**
     * number of users per page.
     */
    $scope.perPage = 10;

    /**
     * page number.
     */
    $scope.assignmentPageNumber = 1;
    $scope.filteredAssignments = [];
    $scope.assignmentSort = 'due_date';

    $scope.onAssignmentFilterChange = function() {
	    $scope.selectAssignmentPage(1);
	    $scope.assignmentPageNumber = 1;
	    return $scope.row = '';
	};

	$scope.onAssignmentOrderChange = function(exp, reverse) {
		$scope.filteredAssignments = $filter('orderBy')($scope.assignments, exp, false)
	    $scope.selectAssignmentPage(1);
	    $scope.assignmentPageNumber = 1;
	    return $scope.row = '';
	};

	$scope.searchAssignment = function() {
		//$scope.assignmentSearchKeyword = $('#alert_search').val();
	    $scope.filteredAssignments = $filter('filter')($scope.assignments, $scope.assignmentSearchKeyword);
	    return $scope.onAssignmentFilterChange();
	};
    $scope.selectAssignmentPage = function (page) {
        var end, start;
        start = (page - 1) * $scope.perPage;
        end = start + $scope.perPage;
        return $scope.currentFilteredAssignments = $scope.filteredAssignments.slice(start, end);
    };
    
    $scope.to_trusted = function (html_code) {
        return utilServices.to_trusted(html_code);
   	}; 
    	
	$scope.trancateString = function (str, len) {
    	if (str.length <= len) {
    		return str;
    	} else{
    		str = str.substring(0, len) + '...';
    		return str;
    	}
    }
    
    $scope.encode = function (course_code) {

        return $base64.encode(course_code);
    }
    
    /**
     * functions for active Tests
     */
	$scope.onFilterChange = function() {
	    $scope.selectQuestionPage(1);
	    $scope.currentQuestionPage = 1;
	    return $scope.row = '';
	};
	$scope.onNumPerPageChange = function() {
	    $scope.selectQuestionPage(1);
	    return $scope.currentQuestionPage = 1;
	};
	$scope.onOrderChange = function() {
	    $scope.selectQuestionPage(1);
	    return $scope.$scope.questions = 1;
	};
	$scope.searchQuestions = function() {
		$scope.questionSearchKeywords = $('#question_search').val();		
	    $scope.filteredQuestions = $filter('filter')($scope.questions, $scope.questionSearchKeywords);
	    return $scope.onFilterChange();
	};
	
	$scope.selectQuestionPage = function (page) {
        var end, start;
        start = (page - 1) * $scope.perPage;
        end = start + $scope.perPage;
        $scope.currentQuestionPage = page;
        return $scope.currentFilteredQuestions = $scope.filteredQuestions.slice(start, end);        
    };
	
	$scope.saveUser = function() {		
		try {
			var method = $scope.profile.id == -1?"add":"change";
			var options = { profile: $scope.profile,
							files: document.getElementById('id_photo_file').files,
							method: method,}
			userFactory.APIAddEditUser(options).then(function(data) {
				if (data.status == 'success') {					
					 $scope.profile = data.profile;
					 $scope.profile['user']['confirm_password'] = $scope.profile['user']['password'];
					 logger.logSuccess("User Saved Succesfully");
				} else {
					alert(data.message);
				}
			});
		} catch (err) {
			alert(err);	
		}
	}
	
	
	//validate function
	$scope.is_valid_question = function() {
		var valid = true;
		if ($scope.current_question.is_state == true && $scope.current_question.state_id == 0) {
			$scope.state_validation_msg = 'You have to select state!';			
			valid = false;		
		}
		return valid;
	}
	
	//initialize profile data for add action
	$scope.initProfileData = function() {
		$scope.profile = {
			department: "",			
			id: -1,
			job_title: "",
			location: "",			
			organization_id_number: "",
			phone_alternate: "",
			phone_oncall: "",
			phone_work: "",
			sample_avatar: null,
			profile_modules: [],
			region:"",
			region: null,
			user_social_security_number: "",
			user: {},			
		};		
		$scope.initProfileModules();
		$scope.initProfileUser();
	}
	
	$scope.initProfileModules = function() {
		var i = 0;
		$scope.profile.modules = [];		
		for (i = 0; i < $scope.modules.length; i++) {
			$scope.profile.modules.push({ active_inactive: false,
										   coremodules: $scope.modules[i]
										});
		}		
	}
	
	$scope.initProfileUser = function() {
		$scope.profile.user = {		
			username: "",
			email: "",
			password: "",
			confirm_password: "",
			first_name: "",
			last_name: "",
			is_active: true,
			type: "",
		}
	}
	
	$scope.setSampleImage = function (obj, url) {  	
	  	$(selected_sample).css('border', "none");
	  	$(selected_sample).css('margin', "10px");
	  	$("#sample_avatar").val(url);
	  	$scope.profile.sample_avatar = url;
	  	var selected_sample = obj;
	  	$(selected_sample).css('border', "2px solid rgb(200, 200, 200)");
	  	$(selected_sample).css('margin', "8px");
	  	$('#profile_photo').attr('src', "/static/dashboard/common/images/avatars/" + url);
	  	$('#btn_sample_avatars_modal_hide').click();
	  	document.getElementById('id_photo_file').value = null;
  	}
	
	//load question meta data
	$scope.loadUserData = function() {
		var userCodeEncrypted = document.URL.split('/');
		var method = userCodeEncrypted[5];
    	var user_id = userCodeEncrypted[6].split("#")[0];    	    	
    	//var test_id = testCodeDecrypted;//$base64.decode(testCodeDecrypted);    	
    	//if (method=="add" || isNaN(user_id) || user_id == "") user_id = 1;
		try {
			userFactory.APIGetAddEditInfo({'method': 'meta', 'user_id': user_id}).then(function(data) {
				if (data.status == 'success') {					
					//init test data
					$scope.profile = data.profile;
					$scope.job_titles = data.job_titles;
					$scope.departments = data.departments;
					$scope.locations = data.locations;
					$scope.regions = data.regions;
					$scope.sample_photos = data.sample_photos;
					$scope.user_types = data.user_types;	
					//initialize profile data for add action									
					if (data.profile == null) {
						$scope.modules = data.modules;
						$scope.initProfileData();
					}
					$scope.profile['user']['confirm_password'] = $scope.profile['user']['password'];					
					//$scope.county_fips = data.county_fips;
				} else {
					alert(data.message);
				}
			});
		} catch (err) {
			alert(err);	
		}
	}

    $scope.loadAssignments = function() {
        if (!jQuery.isEmptyObject($scope.assignments)) return;
        /**
         * calling method in factory to make API call.
         */
        var userCodeEncrypted = document.URL.split('/');
		var method = userCodeEncrypted[5];
    	var user_id = userCodeEncrypted[6].split("#")[0];
        assignmentsFactory.APIGetAssignmentList({'user_id': user_id}).then(function (response) {
            /**
             * storing response form api.
             */

            $scope.assignments = response.data.assignments;
            $scope.assignments = $filter('orderBy')($scope.assignments, '-due_date', true);

			$scope.searchAssignment();
            $scope.selectAssignmentPage($scope.assignmentPageNumber);

        });

    };

    $scope.openAddAssignmentModal = function() {
        var userCodeEncrypted = document.URL.split('/');
		var method = userCodeEncrypted[5];
    	var user_id = userCodeEncrypted[6].split("#")[0];
        userFactory.APIGetCoursesList({'method': 'meta', 'user_id': user_id}).then(function (response) {
            /**
             * storing response form api.
             */
            $scope.courses = response.courses;
            var modalInstance = $modal.open({
              templateUrl: 'addAssignmentModal.html',
              controller: 'addAssignmentModalInstanceCtrl',
              resolve: {
                courses: function () {
                  return $scope.courses;
                }
              }
            });

            modalInstance.result.then(function (data) {
                assignmentsFactory.APICreateAssignment({'user_id': user_id, 'course_id': data.course_id, 'over_due': $filter('date')(data.due_date, 'yyyy/MM/dd')})
                    .then(function (response) {
                        if ( response.status == "success") {
                            logger.logSuccess("Assignment Created Succesfully");
                            $scope.assignments.push(response.response);
                            $scope.assignments = $filter('orderBy')($scope.assignments, '-due_date', true);
                            $scope.searchAssignment();
                            $scope.selectAssignmentPage($scope.assignmentPageNumber);
                        } else {
                            logger.logSuccess("Error");
                        }
                });
            });
        });

    };

    $scope.changeAssignmentDate = function(assignment) {
        $scope.current_assignment = assignment;
        assignmentsFactory.APIEditAssignment({'id': assignment.id, 'over_due': $filter('date')(assignment.due_date, 'yyyy/MM/dd')})
            .then(function (response) {
                logger.logSuccess("Assignment Updated Succesfully");
                if (response.assignment) {
                    index = $scope.assignments.indexOf($scope.current_assignment);
        	        $scope.assignments.splice(index, 1);
                    $scope.assignments.push(response.assignment);
                    $scope.assignments = $filter('orderBy')($scope.assignments, '-due_date', true);
                    $scope.searchAssignment();
                    $scope.selectAssignmentPage($scope.assignmentPageNumber);
                }
        });
    };

    $scope.openDeactivateModal = function(assignment) {
        $scope.current_assignment = assignment;
        var modalInstance = $modal.open({
          templateUrl: 'courseDeactivateModal.html',
          controller: 'courseDeactivateModalInstanceCtrl'
        });
        modalInstance.result.then(function (activate) {
            assignmentsFactory.APIDeleteAssignment({'id': assignment.id, 'over_due': $filter('date')(assignment.due_date, 'yyyy/MM/dd')})
            .then(function (response) {
                logger.logSuccess("Assignment Deleted Succesfully");
                index = $scope.assignments.indexOf($scope.current_assignment);
                $scope.assignments.splice(index, 1);
                $scope.assignments = $filter('orderBy')($scope.assignments, '-due_date', true);
                $scope.searchAssignment();
                $scope.selectAssignmentPage($scope.assignmentPageNumber);
            });
        });
    };
	
	return $scope.loadUserData();
	
}]);

angular.module('users').controller('addAssignmentModalInstanceCtrl', function ($scope, $modalInstance, assignmentsFactory, courses ) {

    $scope.courses = courses;
    $scope.data = {
        course_id: -1,
        over_due: ''
    };

    $scope.minDate = new Date();

    $scope.today = function() {
        return $scope.dt = new Date();
    };
    $scope.today();
    $scope.showWeeks = true;
    $scope.toggleWeeks = function() {
        return $scope.showWeeks = !$scope.showWeeks;
    };
    $scope.clear = function() {
        return $scope.dt = null;
    };
    $scope.disabled = function(date, mode) {
        //return mode === 'day' && (date.getDay() === 0 || date.getDay() === 6);
        return false;
    };
    $scope.toggleMin = function() {
        var _ref;
        /*return $scope.minDate = (_ref = $scope.minDate) != null ? _ref : {
              "null": new Date()
        };*/
        return $scope.minDate = new Date();
    };
    //$scope.toggleMin();
    $scope.open = function($event) {
        $event.preventDefault();
        $event.stopPropagation();
        return $scope.opened = true;
    };
    $scope.dateOptions = {
        'year-format': "'yy'",
        'starting-day': 1
    };
    $scope.formats = ['dd-MMMM-yyyy', 'yyyy/MM/dd', 'shortDate'];

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };

    $scope.print = function () {
        printWindow($('.modal-content'));
    };

    $scope.createAssignment = function () {
        $modalInstance.close($scope.data);
    };

});

angular.module('users').controller('courseDeactivateModalInstanceCtrl', function ($scope, $modalInstance) {

    $scope.data = {
        is_deactivate:  false
    };
    $scope.ok = function () {
        if ($scope.data.is_deactivate == true) {
            $modalInstance.close(true);
        } else {
            $modalInstance.dismiss('cancel');
        }
    };

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };

});