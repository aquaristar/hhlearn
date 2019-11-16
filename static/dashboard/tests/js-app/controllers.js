angular.module("tests").controller('testController', ['$modal', '$scope', '$sce', '$location', '$base64', '$timeout', 'testFactory', 'courseFactory', 'utilServices', function ($modal, $scope, $sce, $location, $base64, $timeout, testFactory, courseFactory, utilServices) {

    /*
     This will hold data for course node.
     */
    $scope.courseData = {};
    /*
     Total number of pages in course.
     */
    $scope.totalPages = 0;
    /*
     Object of $sce.trustAsHtml('') this will hold raw HTML which we need to diplay on page.
     */
    $scope.pageHTML = ''
    /*
     Show/Hide flag for the course toolbar.
     */
    $scope.tools = true;
    /*
     Default font size for the course.
     */
    $scope.fontSizeSlider = 14;
    /*
     This will hold course notes which user will enter.
     */
    $scope.courseNotes = '';
    /*
     Character limit for the course notes.
     */
    $scope.courseNotesLimit = 4000;
    $scope.singleModel = 1;    
    $scope.courseNotes = '';
    $scope.fontsize = 0;
    $scope.mandTestFailed = false;
    $scope.checkAck = false;
    
    /*
     Toggle course toolbar.
     */
    $scope.toggleTools = function () {
        $scope.tools = $scope.tools === false ? true : false;
    };
    
	$scope.to_trusted = function (html_code) {
        return utilServices.to_trusted(html_code);
   	};
    
    $scope.getCourseUrl = function() {
    	var courseCodeEncypted = document.URL.split('/');
    	
    	var courseCodeDecypted = courseCodeEncypted[courseCodeEncypted.length - 1];
        var courseCodeDecyptedArray = courseCodeDecypted.split(":");        
        var test_attempt_id = $base64.decode(courseCodeDecyptedArray[0]);        
        var course_id = $base64.decode(courseCodeDecyptedArray[1]);        
        var is_monthly_saftey = $base64.decode(courseCodeDecyptedArray[2]);
        var assignment_id = $base64.decode(courseCodeDecyptedArray[3]);
        url = '/dashboard/course/'+courseCodeDecyptedArray[1]+':'+courseCodeDecyptedArray[2]+':'+courseCodeDecyptedArray[3];
		return url;        	
    }
    
    /*
     Load test - This is our main method will be called on page load.
     */
    $scope.loadTest = function (questionNumber, answerID, arrow) {        
        var courseCodeEncypted = document.URL.split('/')
        try {
            /*
             Encrypted course ID is stored at location 5. We will get it using courseCodeEncypted[courseCodeEncypted.length - 2]
             it's just doing base64 decoding.
             */
            var courseCodeDecypted = courseCodeEncypted[courseCodeEncypted.length - 1];
            var courseCodeDecyptedArray = courseCodeDecypted.split(":");            
            var test_attempt_id = $base64.decode(courseCodeDecyptedArray[0]);            
            var course_id = $base64.decode(courseCodeDecyptedArray[1]);            
            var is_monthly_saftey = $base64.decode(courseCodeDecyptedArray[2]);
            var assignment_id = $base64.decode(courseCodeDecyptedArray[3]);
            /*
             now we have decrypted course ID so lets get the course content.
             We will call our Factory....
             We are also passing params which will override the default params in factory method.
             */
            testFactory.APIGetTest({"courseID": course_id, "isMonthlySafety": is_monthly_saftey, "testAttemptID": test_attempt_id, "assignmentID": assignment_id, "questionNumber": questionNumber, "answerID": answerID, "arrow":arrow }).then(function (data) {
                /*
                 Assigning test related data.
                 */
                $scope.testData = data.testData;                
                if ($scope.testData == 'test_complete') {
                	$scope.endTest();
                	return;	
                }                
                /*
                 Assigning course related data.
                 */
                $scope.courseData = data.courseData;
                $scope.userData = data.userData;
                $scope.courseNotes = data.courseData.user_notes;
                $scope.fontsize = $scope.userData.fontsize.id;
                //$('#font_slider').slider('setValue', $scope.fontsize);

                /*
                 Check if page node exists. Page node is empty on intro page so we need to add this check.

                 If there's page node then parse the raw html.
                 */
                if (!_.isUndefined($scope.courseData.page)) {
                    if ($scope.courseData.page.length != 0) {
                        var raw_html = courseServices.highlightGlossaryWords($scope.courseData.page[0].raw_html, data);
                    }
                    else {
                        raw_html ='';
                    }
                }                /*
                 Just scroll the page to top :)
                 */
                utilServices.scrollToTop();
            });
        }        
        catch (err) {
            $scope.courseData = false;
        }
    };

    /*
     Load next page.
     */
    $scope.loadNextQuestion = function (questionNumber) {
        var answer = $("input:radio[name=answerRadio]:checked").val();
        if (answer != undefined) {        
        	$scope.loadTest(parseInt(questionNumber), answer, 'next');
        } else {
        	alert('Please select answer!');
        }
    };

    /*
     Load previous page.
     */
    $scope.loadPreviousQuestion = function (questionNumber) {
        $scope.loadTest(parseInt(questionNumber), 'prev');
    };
    
    $scope.endTest = function () {    	
    	var courseCodeEncypted = document.URL.split('/')
        try {
            /*
             Encrypted course ID is stored at location 5. We will get it using courseCodeEncypted[courseCodeEncypted.length - 2]
             it's just doing base64 decoding.
             */
            var courseCodeDecypted = courseCodeEncypted[courseCodeEncypted.length - 1];
            var courseCodeDecyptedArray = courseCodeDecypted.split(":");            
            var test_attempt_id = $base64.decode(courseCodeDecyptedArray[0]);            
            var course_id = $base64.decode(courseCodeDecyptedArray[1]);            
            var is_monthly_saftey = $base64.decode(courseCodeDecyptedArray[2]);
            var assignment_id = $base64.decode(courseCodeDecyptedArray[3]);            		
	    	/**
	         * test End API
	         */
	        /*
             now we have decrypted course ID so lets get the course content.
             We will call our Factory....
             We are also passing params which will override the default params in factory method.
             */
            testFactory.APIEndTest({"testAttemptID": test_attempt_id}).then(function (data) {
	            $scope.apiResponse = data;				
				test_attempt_id = $scope.apiResponse.response.testAttemptID;
	            if (!_.isUndefined($scope.apiResponse.response)) {
	                /**
	                 * log message and show notification on screen.
	                 */
	                //$scope.logger.logCustom($scope.apiResponse.response.message, $scope.apiResponse.response.status)
	
	                if ($scope.apiResponse.response.status == "test_completed") {	
	                    window.location = '/dashboard/testresult/'+$base64.encode(test_attempt_id);	                     
	                } else if ( $scope.apiResponse.response.status == "retaken_test" ) {
	                	$scope.mandTestFailed = $scope.apiResponse.response.mandTestFailed;
	                	$scope.loadTest();
	                }
	            }
	        });
	    }
	    catch (err) {

        }    	   	
    };
    
    /*
     This will save the defautl font size user wants for the courses.
     */
    $scope.saveTextSize = function (fontSize) {
        try {
            $('#textSize').modal('hide');   
            $scope.fontsize = $('#font_slider').val();         
            
	        courseFactory.APISaveFontSize({	
	            'course_id': $scope.courseData.id,	            
	            "fontsize": $scope.fontsize ,	
	        }).then(function (data) {	
	            /**
	             * storing response form api.
	             */
	            $scope.apiResponse = data;	
	            if (!_.isUndefined($scope.apiResponse.response)) {
	                /**
	                 * log message and show notification on screen.
	                 */
	                $scope.logger.logCustom($scope.apiResponse.response.message, $scope.apiResponse.response.status)
	            }
	        });
	        
            $scope.alerts.push({ type: 'success', msg: 'Your default course text size is set to ' + fontSize + 'px.' });
            $timeout(utilServices.closeAlert, 5000);
            $("html, body").animate({ scrollTop: 0 }, "slow");
        }
        catch (err) {

        }
    };
    
    /**
     This will save user notes for course.
     */
    $scope.saveUserNote = function (note) {
        try {
            $('#courseNotes').modal('hide');
	        
	        courseFactory.APISaveFontSize({	
	        	"course_id": $scope.courseData.id,
	            "note": $scope.courseNotes ,
	
	        }).then(function (data) {
	            $scope.apiResponse = data;	
	            if (_.isUndefined($scope.apiResponse.response)) {
	                alert("error");
	            } else if ($scope.apiResponse.status == 'fail') {
	            	alert($scope.apiResponse.response);	            	
	            }	            
	        });           
        }
        catch (err) {
			
        }
    };
    $scope.loadTest();
    $scope.courseUrl = $scope.getCourseUrl();


    $scope.openCourseNotesModal = function() {
        var modalInstance = $modal.open({
          templateUrl: 'courseNotes.html',
          controller: 'testCourseNoteModalInstanceCtrl',
          resolve: {
            courseData: function () {
              return $scope.courseData;
            },
            courseNotesLimit: function () {
              return $scope.courseNotesLimit;
            }
          }
        });
    };

    $scope.openTextSizeModal = function() {
        var modalInstance = $modal.open({
          templateUrl: 'textSize.html',
          controller: 'testTextSizeModalInstanceCtrl',
          resolve: {
            courseData: function () {
              return $scope.courseData;
            },
            fontSize: function () {
              return $scope.fontsize;
            }
          }
        });

        modalInstance.result.then(function (size) {
          $scope.fontsize = size;
        });
    };

}]);

/**
 * The controller for Test Result Page
 */
angular.module("tests").controller('testResultController', ['$scope', '$sce', '$location', '$base64', '$timeout', 'testFactory', 'utilServices', function ($scope, $sce, $location, $base64, $timeout, testFactory, utilServices) {
	
	$scope.loadTestResult = function () {		
		var courseCodeEncypted = document.URL.split('/');
        try {
            /*
             Encrypted course ID is stored at location 5. We will get it using courseCodeEncypted[courseCodeEncypted.length - 2]
             it's just doing base64 decoding.
             */            
            var courseCodeDecypted = courseCodeEncypted[courseCodeEncypted.length - 1];
            var courseCodeDecyptedArray = courseCodeDecypted.split(":");
            var test_attempt_id = $base64.decode(courseCodeDecyptedArray[0]);            		
	    	/**
	         * test End API
	         */
	        /*
             now we have decrypted course ID so lets get the course content.
             We will call our Factory....
             We are also passing params which will override the default params in factory method.
             */
            testFactory.APITestResult({"testAttemptID": test_attempt_id}).then(function (data) {            	
            	$scope.apiResponse = data.response;            	
            	if ($scope.apiResponse.status == "success") {
            		$scope.courseData = $scope.apiResponse.courseData;
					$scope.testResultData = $scope.apiResponse.testResultData;  				
				}
                utilServices.scrollToTop();
            });
        }
        catch (err) {

        }
	};
	$scope.loadTestResult()
}]);	

/**
 * The controller for Admin tests view page
 */
angular.module("tests").controller('testViewController', ['$modal', '$scope', '$sce', '$location', 'filterFilter', 'logger', '$filter', '$base64', '$timeout', 'testFactory', 'utilServices', function ($modal, $scope, $sce, $location, filterFilter, logger, $filter, $base64, $timeout, testFactory, utilServices) {
	$scope.tests = [];
	$scope.currentTest = {};
	$scope.is_reactivate = false;
	$scope.is_deactivate = false;
	
	//variables for active tests
	$scope.activeTests = {};
	$scope.perPage = 10;    
    $scope.activeTestSearchKeywords = '';
    $scope.currentActiveTestPage = 1;
    $scope.filteredActiveTests = {};
    $scope.activeTestSort = 'course.number';
    
    //variables for inactive tests
	$scope.inactiveTests = {}
	$scope.inactiveTestPerPage = 10;    
    $scope.inactiveTestSearchKeywords = '';
    $scope.currentInactiveTestPage = 1;
    $scope.filteredInactiveTests = {};
    $scope.inactiveTestSort = 'course.number';
	
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
     * functions for active Tests
     */
	$scope.onFilterChange = function() {
	    $scope.selectActiveTestPage(1);
	    $scope.currentActiveTestPage = 1;
	    return $scope.row = '';
	};
	$scope.onNumPerPageChange = function() {
	    $scope.selectActiveTestPage(1);
	    return $scope.currentActiveTestPage = 1;
	};

	$scope.onOrderChange = function(exp, reverse) {		
		$scope.filteredActiveTests = $filter('orderBy')($scope.filteredActiveTests, exp, false)
	    $scope.selectActiveTestPage(1);
	    $scope.currentActiveTestPage = 1;
	    return $scope.row = '';
	};
	$scope.searchActiveTests = function() {
		$scope.activeTestSearchKeywords = $('#atest_search').val();		
	    $scope.filteredActiveTests = $filter('filter')($scope.activeTests, $scope.activeTestSearchKeywords);
	    return $scope.onFilterChange();
	};
	
	$scope.selectActiveTestPage = function (page) {
        var end, start;
        start = (page - 1) * $scope.perPage;
        end = start + $scope.perPage;
        return $scope.currentFilteredActiveTests = $scope.filteredActiveTests.slice(start, end);        
    };
    
    /**
     * functions for inactive Tests
     */
	$scope.onInactiveTestFilterChange = function() {
	    $scope.selectInactiveTestPage(1);
	    $scope.currentInactiveTestPage = 1;
	    return $scope.row = '';
	};
	$scope.onInactiveTestNumPerPageChange = function() {
	    $scope.selectInactiveTestPage(1);
	    return $scope.currentInactiveTestPage = 1;
	};

	$scope.onInactiveTestOrderChange = function(exp, reverse) {		
		$scope.filteredInactiveTests = $filter('orderBy')($scope.filteredInactiveTests, exp, false)
	    $scope.selectInactiveTestPage(1);
	    $scope.currentInactiveTestPage = 1;
	    return $scope.row = '';
	};
	$scope.searchInactiveTests = function() {
		$scope.inactiveTestSearchKeywords = $('#iatest_search').val();		
	    $scope.filteredInactiveTests = $filter('filter')($scope.inactiveTests, $scope.inactiveTestSearchKeywords);
	    return $scope.onInactiveTestFilterChange();
	};
	
	$scope.selectInactiveTestPage = function (page) {
        var end, start;
        start = (page - 1) * $scope.inactiveTestPerPage;
        end = start + $scope.inactiveTestPerPage;
        return $scope.currentFilteredInactiveTests = $scope.filteredInactiveTests.slice(start, end);        
    };
    
    $scope.selectCurrentTest = function (obj) {
    	//initialize modal variables
    	$scope.is_reactivate = false;
    	$scope.is_deactivate = false;
    	//set currenTest object
		$scope.currentTest = obj;
		return;    	
    }

    $scope.openActivateModal = function(t) {
        $scope.selectCurrentTest(t);
        var modalInstance = $modal.open({
          templateUrl: 'testActivateModal.html',
          controller: 'testActivateModalInstanceCtrl',
        });
        modalInstance.result.then(function (activate) {
          $scope.is_reactivate = true;
          $scope.activateTest(true);
        });
    }

    $scope.openDeactivateModal = function(t) {
        $scope.selectCurrentTest(t);
        var modalInstance = $modal.open({
          templateUrl: 'testDeactivateModal.html',
          controller: 'testDeactivateModalInstanceCtrl',
        });
        modalInstance.result.then(function (activate) {
          $scope.is_deactivate = true;
          $scope.activateTest(false);
        });
    }
    
    //Activate Tests
    $scope.activateTest = function (activate) {
    	if (activate == false) {
    		if ( $scope.is_deactivate == true ) {
    			testFactory.APITestChange({"method": "change", "test_id": $scope.currentTest.id, "is_active": false }).then(function (data) {
    				if (data.status == 'success') {
    					$scope.currentTest.is_active = false;
						$scope.updateAllViews();	
    				}    				
    			});
    		}
    	} else {
    		if ( $scope.is_reactivate == true ) {
    			testFactory.APITestChange({"method": "change", "test_id": $scope.currentTest.id, "is_active": true }).then(function (data) {
    				if (data.status == 'success') {
    					$scope.currentTest.is_active = true;
						$scope.updateAllViews();
    				}    				
    			});
    		}
    	}
    	return true;
    } 
    
    $scope.updateAllViews = function() {
    	//prepare tests data
    	$scope.activeTests = filterFilter($scope.tests, {
	        is_active: true,
	    });
	    $scope.inactiveTests = filterFilter($scope.tests, {
	        is_active: false,
	    });
    	$scope.searchActiveTests();
    	$scope.selectActiveTestPage($scope.currentActiveTestPage);	        	
    	$scope.searchInactiveTests();
    	$scope.selectInactiveTestPage($scope.currentInactiveTestPage);
    }
	
	$scope.loadAllTests = function() {
	  	try {	        
	        testFactory.APIGetAllTest({}).then(function (data) {	    
	            $scope.tests = data.tests;
	            $scope.tests = $filter('orderBy')($scope.tests, '-course.number', true)
			    //update views
			    $scope.updateAllViews();
	        });
	    }
	    catch (err) {
	        $scope.alertData = false;
	    }
	};
	//first time load all tests 
	$scope.loadAllTests();
}]);

angular.module("tests").controller('testAddController', ['$modal', '$scope', '$sce', '$location', 'filterFilter', 'logger', '$filter', '$base64', '$timeout', 'testFactory', 'utilServices', function ($modal, $scope, $sce, $location, filterFilter, logger, $filter, $base64, $timeout, testFactory, utilServices) {
	$scope.questions_tab = false;
	$scope.course_name = "";
	$scope.test_id = -1;
	$scope.is_active = true;
	$scope.test_types = [];
	$scope.type_id = -1;
	$scope.questions_count = 1;
	$scope.course_id = -1;
	$scope.question_type= -1;	
	$scope.questions = [];
	$scope.question_types = [];
	$scope.accreditation_agencies = [];
	$scope.states = [];
	$scope.county_fips = [];
	$scope.selected_county_fips = [];
	
	$scope.current_question = {};
	$scope.edit_question = {};
	$scope.current_question_type = {};
	$scope.current_accreditation_agencies = {};
	$scope.current_states = {};
	$scope.current_county_fip = {};
	
	//question count variables
	$scope.regular_count = 0;
	$scope.mand_count = 0;
	$scope.comp_count = 0;
	$scope.accredited_count = 0;
	$scope.amand_count = 0;
	$scope.state_count = 0;
	$scope.smand_count = 0;
	$scope.county_count = 0;
	$scope.cmand_count = 0;
	
	//variables for active tests	
	$scope.perPage = 10;    
    $scope.questionSearchKeywords = '';
    $scope.currentQuestionPage = 1;
    $scope.filteredQuestions = {};
    $scope.questionSort = 'question.text';
    
    //variables for activation
    $scope.is_deactivate = false;
    $scope.is_reactivate = false;
    
    //variables for validation 
    $scope.topic_validation_msg = '';
    $scope.question_validation_msg = '';
    $scope.answer_text_validation_msg = [];
    $scope.whythis_validation_msg = [];
    $scope.accreditation_validation_msg = '';
    $scope.state_validation_msg = '';
    $scope.county_validation_msg = '';
    
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
	
	$scope.saveTest = function() {
		$scope.type_id = $('#test_type').val();
		$scope.course_id = $('#course_id').val();
		$scope.questions_count = $('#questions_count').val();
		$scope.is_active = $('#test_is_active').is(":checked");
		//check if course is selected 
		if ($scope.course_id == "-1") {
			alert("Please select course!");
			return;
		}		
		if ($scope.test_id != -1) {
			options = { 'test_id': $scope.test_id,
						'type': $scope.type_id,
						'questions_count': $scope.questions_count,
						'course_id': $scope.course_id,
						'is_active': $scope.is_active,}	
		} else {
			options = { 'type': $scope.type_id,
						'questions_count': $scope.questions_count,
						'course_id': $scope.course_id,
						'is_active': $scope.is_active,}
		}
		try {
			testFactory.APISaveTest(options).then(function(data) {
				if (data.status == 'success') {
					$scope.test_id = data.test_id;
					$scope.questions_tab = true;
					$scope.course_name = $("#course_id option:selected").text();
					//disable course id selection
					$("#course_id").attr('disabled', 'disabled');
					logger.logSuccess("Test saved Successfully!");
				} else {
					alert(data.message);
				}
			});
		} catch (err) {
			alert(err);	
		}
	}
	
	$scope.onTypeChange = function() {
		$scope.type_id = $('#test_type').val();
		if ($scope.type_id == 2) {
			$scope.questions_count = 50;
			$("#questions_count").attr('disabled', 'disabled');
			$('.ui-spinner .btn').attr('disabled', 'disabled');
		} else if ( $scope.type_id == 3) {
			$scope.questions_count = 0;
			$("#questions_count").attr('disabled', 'disabled');
			$('.ui-spinner .btn').attr('disabled', 'disabled');			
		} else {
			$scope.questions_count = 1;
			$("#questions_count").removeAttr('disabled');
			$('.ui-spinner .btn').removeAttr('disabled');			
		}
	}
	
	$scope.onCourseIDChange = function() {
		$scope.course_id = $("#course_id").val();
		$scope.course_name = $("#course_id option:selected").text();
	}
	
	$scope.initAddQuestionModal = function() {
		$scope.current_question = {test_id: $scope.test_id,
								   type_id: 1 ,
								   topic: '',
								   text: '',
								   is_regular: true,
								   is_mandatory: false,
								   is_competency: false, 
								   is_accredited: false,
								   accredited_agency_id: 0,
								   accredited_is_mandatory: false,
								   is_state: false,
								   state_id: 0, 
								   state_is_mandatory: false,
								   is_county: false,
								   county_fips: 0,
								   county_fips_mandatory: false, 
								   is_active: true,
								   answers:[]};
		$scope.initAnswers();
        var modalInstance = $modal.open({
            templateUrl: 'questionAddModal.html',
            controller: 'questionAddModalInstanceCtrl',
            resolve: {
                current_question: function () {
                    return $scope.current_question;
                },
                county_fips: function() {
                    return $scope.county_fips;
                },
                accreditation_agencies: function() {
                    return $scope.accreditation_agencies;
                },
                states: function() {
                    return $scope.states;
                },
                question_types: function() {
                    return $scope.question_types;
                }
            }
        });

        modalInstance.result.then(function (current_question) {
            $scope.current_question = current_question;
            $scope.saveQuestion();
        });
	}
	
	$scope.initAnswers = function() {
		//$scope.current_question.type_id = $scope.current_question_type.id;
		$scope.current_question.answers = [];
		if ($scope.current_question.type_id == 1) {
			$scope.current_question.answers.push({is_correct: true, text:"True", why_this_choice:'', is_active: true,});
			$scope.current_question.answers.push({is_correct: false, text:"False", why_this_choice:'', is_active: true,});
		} else if ($scope.current_question.type_id == 3) {
			$scope.current_question.answers.push({is_correct: true, text:"Yes", why_this_choice:'', is_active: true,});
			$scope.current_question.answers.push({is_correct: false, text:"No", why_this_choice:'', is_active: true,});			
		} else {
			$scope.current_question.answers.push({is_correct: true, text:"", why_this_choice:'', is_active: true,});
		}
	}
	
	$scope.addAnswer = function() {
		$scope.current_question.answers.push({is_correct: false, text:"", why_this_choice:'', is_active: true,});
	}
	
	$scope.removeAnswer = function(index) {
		if ($scope.current_question.answers.length == 1) {
			alert("You can not remove this answer");
		} else {
			$scope.current_question.answers.splice(index, 1);
			return;
		}
	}
	
	//adjust one one answer of question is correct
	$scope.validateAnswer = function(index) {
		var correct_length = filterFilter($scope.current_question.answers, {
	        is_correct: true,
	    }).length;
	    if ( correct_length != 1) {
	    	if ($scope.current_question.answers[index].is_correct == false) {
	    		$scope.current_question.answers[index].is_correct = true;
	    	} else {
		    	var i = 0;
		    	for ( i = 0; i < $scope.current_question.answers.length; i++) {
		    		if (i != index) $scope.current_question.answers[i].is_correct = false;
		    	}
		    }
	    } 
	}
	
	$scope.saveQuestion = function() {		
		if ('id' in $scope.current_question) {
			try {
				testFactory.APIChangeTestQuestion({'method': 'change', 'question': $scope.current_question}).then(function(data) {
					if (data.status == 'success') {					
						index = $scope.questions.indexOf($scope.edit_question);
        				$scope.questions[index] = data.data;
        				$scope.updateQuestionsData();       				
						logger.logSuccess("Question changes saved Successfully!");
					} else {
						alert(data.message);
					}
				});
			} catch (err) {
				alert(err);	
			}
		} else {
			try {
				testFactory.APIChangeTestQuestion({'method': 'add', 'question': $scope.current_question}).then(function(data) {
					if (data.status == 'success') {					
						$scope.questions.push(data.data);
						logger.logSuccess("Question Added!");
						$scope.updateQuestionsData();
					} else {
						alert(data.message);
					}
				});
			} catch (err) {
				alert(err);	
			}
		}
	}
	
	$scope.removeQuestion = function(question) {
		try {
			testFactory.APIChangeTestQuestion({'method': 'remove', 'question': question}).then(function(data) {
				if (data.status == 'success') {					
					index = $scope.questions.indexOf(question);
        			$scope.questions.splice(index, 1);
        			$scope.updateQuestionsData();
        			logger.logSuccess("Question Removed!");        			
				} else {
					alert(data.message);
				}
			});
		} catch (err) {
			alert(err);	
		}
	}
	
	$scope.editQuestion = function(question) {
		$scope.edit_question = question;
		try {			
			testFactory.APIGetTestQuestion({'question_id': question.id}).then(function(data) {
				if (data.status == 'success') {
					q = data.question;
					$scope.current_question = {id: q.id,
											   test_id: q.test,
											   type_id: q.type.id ,
											   topic: q.topic,
											   text: q.text,
											   is_regular: q.is_regular,
											   is_mandatory: q.is_mandatory,
											   is_competency: q.is_competency, 
											   is_accredited: (q.accredited_agency==null)?false:true,
											   accredited_agency_id: (q.accredited_agency==null)?0:question.accredited_agency,
											   accredited_is_mandatory: q.accredited_is_mandatory,
											   is_state: (q.state==null)?false:true,
											   state_id: (q.state==null)?0:question.state,
											   state_is_mandatory: q.state_is_mandatory,
											   is_county: (q.county_fips==null)?false:true,
											   county_fips: (q.county_fips==null)?0:question.county_fips,
											   county_fips_mandatory: q.county_fips_mandatory, 
											   is_active: q.is_active,
											   answers:[]};
					var answers = [];
					for (var i = 0; i < q.answers.length; i++) {
						answers.push(q.answers[i].coreanswers);
					}
					$scope.county_fips = data.county_fips;
					$scope.current_question.answers = answers;

                    var modalInstance = $modal.open({
                        templateUrl: 'questionAddModal.html',
                        controller: 'questionAddModalInstanceCtrl',
                        resolve: {
                            current_question: function () {
                                return $scope.current_question;
                            },
                            county_fips: function() {
                                return $scope.county_fips;
                            },
                            accreditation_agencies: function() {
                                return $scope.accreditation_agencies;
                            },
                            states: function() {
                                return $scope.states;
                            },
                            question_types: function() {
                                return $scope.question_types;
                            }
                        }
                    });

                    modalInstance.result.then(function (current_question) {
                        $scope.current_question = current_question;
                        $scope.saveQuestion();
                    });

				} else {
					alert(data.message);
				}
			});
		} catch (err) {
			alert(err);	
		}

	}
	
	$scope.loadCountyFips = function() {
		if ($scope.current_question.state_id == 0) return;
		try {
			state = filterFilter($scope.states, {
		        id: Number($scope.current_question.state_id),
		    }, true);
		    state = state[0];
			testFactory.APIGetCountyFips({'state': state.abbreviation}).then(function(data) {				
				if (data.status == 'success') {
					$scope.county_fips = data.county_fips;
					$scope.current_question.county_fips = 0;
				} else {
					alert(data.message);
				}
			});
		} catch (err) {
			alert(err);	
		}
	}
	
	$scope.updateQuestionCount = function() {
		$scope.regular_count = filterFilter($scope.questions, { is_regular: true, is_active: true}).length;
		$scope.mand_count = filterFilter($scope.questions, { is_mandatory: true, is_active: true}).length;
		$scope.comp_count = filterFilter($scope.questions, { is_competency: true, is_active: true}).length;
		$scope.accredited_count = filterFilter($scope.questions, { accredited_agency: '!!', is_active: true}).length;
		$scope.amand_count = filterFilter($scope.questions, { accredited_is_mandatory: true, is_active: true}).length;
		$scope.state_count = filterFilter($scope.questions, { state: '!!', is_active: true}).length;
		$scope.smand_count = filterFilter($scope.questions, { state_is_mandatory: true, is_active: true}).length; 
		$scope.county_count = filterFilter($scope.questions, { state: '!!', county_fips: '!!', is_active: true}).length;
		$scope.cmand_count = filterFilter($scope.questions, { state: '!!', county_fips: '!!', county_fips_mandatory: true, is_active: true}).length;
	}
	
	//validate function
	$scope.is_valid_question = function() {
		var valid = true;
		if ($.isEmptyObject($scope.current_question)) return false;
		if ($scope.current_question.is_state == true && $scope.current_question.state_id == 0) {
			$scope.state_validation_msg = 'You have to select state!';			
			valid = false;		
		} else {
			$scope.state_validation_msg = '';
		}
		if ($scope.current_question.is_accredited == true && $scope.current_question.accredited_agency_id == 0) {
			$scope.accreditation_validation_msg = 'You have to select accreditation!';
			valid = false;
		} else {
			$scope.accreditation_validation_msg = '';
		}
		if ($scope.current_question.is_county == true && $scope.current_question.county_fips == 0) {
			$scope.county_validation_msg = 'You have to select county!';
			valid = false;
		} else {
			$scope.county_validation_msg = '';
		}
		if ($scope.current_question.text == '') {
			$scope.question_validation_msg = 'This filed is required!';
			valid = false;
		} else if ($scope.current_question.text.length > 500) {
			$scope.question_validation_msg = 'String length overflow!';
			valid = false;
		} else {
			$scope.question_validation_msg = '';
		}
		if ($scope.current_question.topic == '') {
			$scope.topic_validation_msg = 'This field is required!';
			valid = false;
		}else if ($scope.current_question.topic.length > 255){
			$scope.question_validation_msg = 'String length overflow!';
			valid = false;
		} else {
			$scope.topic_validation_msg = '';
		}
		if ($scope.current_question.answers) {
			var is_first = false;
			if ($scope.answer_text_validation_msg.length == 0 ) is_first = true;
			for (var i = 0; i < $scope.current_question.answers.length; i++) {
				answer = $scope.current_question.answers[i]
				if (is_first == true) {
					$scope.answer_text_validation_msg.push('');
					$scope.whythis_validation_msg.push('');
				}				
				if (answer.text == '' || answer.text == undefined) {					
					$scope.answer_text_validation_msg[i] = 'You need to input answer text!';			
					valid = false;					
				} else {
					$scope.answer_text_validation_msg[i] = '';
				}
				if (answer.is_correct == false && (answer.why_this_choice == '' || answer.why_this_choice == undefined)) {
					$scope.whythis_validation_msg[i] = 'You need to input this field!';
					valid = false;
				} else {
					$scope.whythis_validation_msg[i] = '';
				}
			}
		}
		return valid;
	}
	
	$scope.selectCurrentQuestion = function(q) {
		$scope.edit_question = q;
		$scope.is_deactivate = false;
		$scope.is_reactivate = false;
	}
	
	//update question data
	$scope.updateQuestionsData = function() {
		$scope.updateQuestionCount();
		//update all views for question
		var curPage = $scope.currentQuestionPage;		
		$scope.searchQuestions();
		$scope.currentQuestionPage = curPage;
		$scope.selectQuestionPage($scope.currentQuestionPage);		
	}

    $scope.openActivateModal = function(q) {
        $scope.selectCurrentQuestion(q);
        var modalInstance = $modal.open({
          templateUrl: 'testActivateModal.html',
          controller: 'testActivateModalInstanceCtrl',
        });
        modalInstance.result.then(function (activate) {
          $scope.is_reactivate = true;
          $scope.activateQuestion(true);
        });
    }

    $scope.openDeactivateModal = function(q) {
        $scope.selectCurrentQuestion(q);
        var modalInstance = $modal.open({
          templateUrl: 'testDeactivateModal.html',
          controller: 'testDeactivateModalInstanceCtrl',
        });
        modalInstance.result.then(function (activate) {
          $scope.is_deactivate = true;
          $scope.activateQuestion(false);
        });
    }
	
	//Activate Question
    $scope.activateQuestion = function (activate) {
    	if (activate == false) {
    		if ( $scope.is_deactivate == true ) {
    			testFactory.APIChangeTestQuestion({'method': 'activate', 'question': $scope.edit_question, 'is_active':false}).then(function(data) {
					if (data.status == 'success') {
						$scope.edit_question.is_active = false;  				
        				$scope.updateQuestionsData();       				
						logger.logSuccess("Question changes saved Successfully!");
					} else {
						alert(data.message);
					}
				});
    		}
    	} else {
    		if ( $scope.is_reactivate == true ) {
    			testFactory.APIChangeTestQuestion({'method': 'activate', 'question': $scope.edit_question, 'is_active':true}).then(function(data) {
					if (data.status == 'success') {					
						$scope.edit_question.is_active = true;
        				$scope.updateQuestionsData();       				
						logger.logSuccess("Question changes saved Successfully!");
					} else {
						alert(data.message);
					}
				});
    		}
    	}
    	return true;
    }
	
	//load question meta data
	$scope.loadTestData = function() {
		var testCodeEncrypted = document.URL.split('/');
		var method = testCodeEncrypted[5];
    	var test_id = testCodeEncrypted[6].split("#")[0];    	    	
    	//var test_id = testCodeDecrypted;//$base64.decode(testCodeDecrypted);    	
    	if (method=="add" || isNaN(test_id) || test_id == "") test_id = -1;
		try {
			testFactory.APIGetTestData({'method': 'meta', 'test_id': test_id}).then(function(data) {
				if (data.status == 'success') {					
					//init test data
					$scope.test_types = data.test_types;		
					$scope.courses = data.courses;
					if (data.test != null) {						
						$scope.test_id = data.test.id;
						$scope.course_id = data.test.course.number;
						$scope.course_name = data.test.course.name;
						$scope.questions_count = data.test.course.number_test_questions;
						$scope.type_id = data.test.type.id;
						$scope.is_active = data.test.is_active;
						$scope.questions_tab = true;
					}
					else {
						if ($scope.test_types.length > 0) {
							$scope.type_id = $scope.test_types[0].id;
						} else {
							$scope.type_id = -1
						}
						if ($scope.courses.length > 0) {						
							$scope.course_id = -1
						}
					}					
					
					//initialize questions related data
					$scope.questions = data.questions;
					if ($scope.questions.length > 0) {						
						$scope.updateQuestionsData();
					} else {
						$scope.questions = [];
					}				
					$scope.question_types = data.question_types;
					$scope.converted_question_types = new Array();
					//conver test types for associated array
					for (var i = 0; i < data.question_types.length; i++) {
						$scope.converted_question_types[data.question_types[i].id] = data.question_types[i].name; 	
					}
					$scope.accreditation_agencies = data.accreditation_agencies;
					$scope.states = data.states;
					//$scope.county_fips = data.county_fips;
				} else {
					alert(data.message);
				}
			});
		} catch (err) {
			alert(err);	
		}
	}
	
	$scope.loadTestData();
	
	return $scope.questions_tab;
	
}]);

angular.module('tests').controller('testCourseNoteModalInstanceCtrl', function ($scope, $modalInstance, courseFactory, courseData, courseNotesLimit ) {

    $scope.courseData = courseData;
    $scope.courseNotesLimit = courseNotesLimit;

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };
    /**
     This will save user notes for course.
     */
    $scope.saveUserNote = function (note) {
        try {
	        courseFactory.APISaveFontSize({
	        	"course_id": $scope.courseData.id,
	            "note": $scope.courseData.user_notes ,
	        }).then(function (data) {
	            $scope.apiResponse = data;
	            if (_.isUndefined($scope.apiResponse.response)) {
	                alert("error");
	            } else if ($scope.apiResponse.status == 'fail') {
	            	alert($scope.apiResponse.response);
	            }
	        });
            $modalInstance.dismiss('cancel');
        }
        catch (err) {

        }
    };


});


angular.module('tests').controller('testTextSizeModalInstanceCtrl', function ($scope, $modalInstance, courseFactory, courseData, fontSize) {

    $scope.courseData = courseData;
    $scope.fontSizeSlider = 14;
    $scope.fontSize = fontSize;

    //$('#font_slider').slider('setValue', $scope.fontSize);

    $scope.ok = function () {
        $modalInstance.close($scope.fontSize);
    };

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };

    $scope.changeDemoFontSize = function () {
    	size = $('#font_slider').val();
    	$scope.$apply(function(){
	    	if (size == 1) {
	    		$scope.fontSizeSlider = 12;
	    	} else if (size == 3) {
	    		$scope.fontSizeSlider = 18;
	    	} else {
	    		$scope.fontSizeSlider = 14;
	    	}
    	});
    };

    $scope.saveTextSize = function (fontSize) {
        try {
            $scope.fontSize = parseInt($('#font_slider').val());
            $scope.ok();

	        courseFactory.APISaveFontSize({
	            'course_id': $scope.courseData.id,
	            "fontsize": $scope.fontSize
	        }).then(function (data) {
	            /**
	             * storing response form api.
	             */
	            $scope.apiResponse = data;
	            if (!_.isUndefined($scope.apiResponse.response)) {
	                /**
	                 * log message and show notification on screen.
	                 */
	                //$scope.logger.logCustom($scope.apiResponse.response.message, $scope.apiResponse.response.status)
	            }
	        });

            /*$scope.alerts.push({ type: 'success', msg: 'Your default course text size is set to ' + fontSize + 'px.' });
            $timeout(utilServices.closeAlert, 5000);
            $("html, body").animate({ scrollTop: 0 }, "slow");*/
        }
        catch (err) {

        }
    };
});


angular.module('tests').controller('questionAddModalInstanceCtrl', function ($scope, $modalInstance, filterFilter, logger, $filter, testFactory, current_question, county_fips, question_types, accreditation_agencies, states ) {

    $scope.current_question = current_question;
    $scope.question_types = question_types;
    $scope.county_fips = county_fips;
	$scope.states = states;
    $scope.accreditation_agencies = accreditation_agencies;

    //variables for validation
    $scope.topic_validation_msg = '';
    $scope.question_validation_msg = '';
    $scope.answer_text_validation_msg = [];
    $scope.whythis_validation_msg = [];
    $scope.accreditation_validation_msg = '';
    $scope.state_validation_msg = '';
    $scope.county_validation_msg = '';

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };

    $scope.initAnswers = function() {
		//$scope.current_question.type_id = $scope.current_question_type.id;
		$scope.current_question.answers = [];
		if ($scope.current_question.type_id == 1) {
			$scope.current_question.answers.push({is_correct: true, text:"True", why_this_choice:'', is_active: true,});
			$scope.current_question.answers.push({is_correct: false, text:"False", why_this_choice:'', is_active: true,});
		} else if ($scope.current_question.type_id == 3) {
			$scope.current_question.answers.push({is_correct: true, text:"Yes", why_this_choice:'', is_active: true,});
			$scope.current_question.answers.push({is_correct: false, text:"No", why_this_choice:'', is_active: true,});
		} else {
			$scope.current_question.answers.push({is_correct: true, text:"", why_this_choice:'', is_active: true,});
		}
	}

	$scope.addAnswer = function() {
		$scope.current_question.answers.push({is_correct: false, text:"", why_this_choice:'', is_active: true,});
	}

	$scope.removeAnswer = function(index) {
		if ($scope.current_question.answers.length == 1) {
			alert("You can not remove this answer");
		} else {
			$scope.current_question.answers.splice(index, 1);
			return;
		}
	}

	//adjust one one answer of question is correct
	$scope.validateAnswer = function(index) {
		var correct_length = filterFilter($scope.current_question.answers, {
	        is_correct: true,
	    }).length;
	    if ( correct_length != 1) {
	    	if ($scope.current_question.answers[index].is_correct == false) {
	    		$scope.current_question.answers[index].is_correct = true;
	    	} else {
		    	var i = 0;
		    	for ( i = 0; i < $scope.current_question.answers.length; i++) {
		    		if (i != index) $scope.current_question.answers[i].is_correct = false;
		    	}
		    }
	    }
	}

    $scope.loadCountyFips = function() {
		if ($scope.current_question.state_id == 0) return;
		try {
			state = filterFilter($scope.states, {
		        id: Number($scope.current_question.state_id),
		    }, true);
		    state = state[0];
			testFactory.APIGetCountyFips({'state': state.abbreviation}).then(function(data) {
				if (data.status == 'success') {
					$scope.county_fips = data.county_fips;
					$scope.current_question.county_fips = 0;
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
		if ($.isEmptyObject($scope.current_question)) return false;
		if ($scope.current_question.is_state == true && $scope.current_question.state_id == 0) {
			$scope.state_validation_msg = 'You have to select state!';
			valid = false;
		} else {
			$scope.state_validation_msg = '';
		}
		if ($scope.current_question.is_accredited == true && $scope.current_question.accredited_agency_id == 0) {
			$scope.accreditation_validation_msg = 'You have to select accreditation!';
			valid = false;
		} else {
			$scope.accreditation_validation_msg = '';
		}
		if ($scope.current_question.is_county == true && $scope.current_question.county_fips == 0) {
			$scope.county_validation_msg = 'You have to select county!';
			valid = false;
		} else {
			$scope.county_validation_msg = '';
		}
		if ($scope.current_question.text == '') {
			$scope.question_validation_msg = 'This filed is required!';
			valid = false;
		} else if ($scope.current_question.text.length > 500) {
			$scope.question_validation_msg = 'String length overflow!';
			valid = false;
		} else {
			$scope.question_validation_msg = '';
		}
		if ($scope.current_question.topic == '') {
			$scope.topic_validation_msg = 'This field is required!';
			valid = false;
		}else if ($scope.current_question.topic.length > 255){
			$scope.question_validation_msg = 'String length overflow!';
			valid = false;
		} else {
			$scope.topic_validation_msg = '';
		}
		if ($scope.current_question.answers) {
			var is_first = false;
			if ($scope.answer_text_validation_msg.length == 0 ) is_first = true;
			for (var i = 0; i < $scope.current_question.answers.length; i++) {
				answer = $scope.current_question.answers[i]
				if (is_first == true) {
					$scope.answer_text_validation_msg.push('');
					$scope.whythis_validation_msg.push('');
				}
				if (answer.text == '' || answer.text == undefined) {
					$scope.answer_text_validation_msg[i] = 'You need to input answer text!';
					valid = false;
				} else {
					$scope.answer_text_validation_msg[i] = '';
				}
				if (answer.is_correct == false && (answer.why_this_choice == '' || answer.why_this_choice == undefined)) {
					$scope.whythis_validation_msg[i] = 'You need to input this field!';
					valid = false;
				} else {
					$scope.whythis_validation_msg[i] = '';
				}
			}
		}
		return valid;
	}

    $scope.saveQuestion = function() {
        $modalInstance.close($scope.current_question);
    }

});

angular.module('tests').controller('testActivateModalInstanceCtrl', function ($scope, $modalInstance) {
    $scope.data = {
        is_reactivate:  false
    };

    $scope.ok = function () {
        if ($scope.data.is_reactivate == true) {
            $modalInstance.close(true);
        } else {
            $modalInstance.dismiss('cancel');
        }
    };

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };

});

angular.module('tests').controller('testDeactivateModalInstanceCtrl', function ($scope, $modalInstance) {

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