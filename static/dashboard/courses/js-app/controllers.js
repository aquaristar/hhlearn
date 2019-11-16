angular.module("course").controller('courseController', ['$modal', '$scope', '$sce', '$location', '$base64', '$timeout', 'logger', 'courseFactory', 'utilServices', 'courseServices', function ($modal, $scope, $sce, $location, $base64, logger, $timeout, courseFactory, utilServices, courseServices) {

	$scope.logger = logger;
	
	$scope.apiResponse = {};
    /*
     This will hold data for course node.
     */
    $scope.courseData = {};
    
    $scope.fontsize = 0;


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
    $scope.currentResource = {};    
    $scope.rawTextContent = '';    
    $scope.validHTMLTags  =/^(?:a|abbr|acronym|address|applet|area|article|aside|audio|b|base|basefont|bdi|bdo|bgsound|big|blink|blockquote|body|br|button|canvas|caption|center|cite|code|col|colgroup|data|datalist|dd|del|details|dfn|dir|div|dl|dt|em|embed|fieldset|figcaption|figure|font|footer|form|frame|frameset|h1|h2|h3|h4|h5|h6|head|header|hgroup|hr|html|i|iframe|img|input|ins|isindex|kbd|keygen|label|legend|li|link|listing|main|map|mark|marquee|menu|menuitem|meta|meter|nav|nobr|noframes|noscript|object|ol|optgroup|option|output|p|param|plaintext|pre|progress|q|rp|rt|ruby|s|samp|script|section|select|small|source|spacer|span|strike|strong|style|sub|summary|sup|table|tbody|td|textarea|tfoot|th|thead|time|title|tr|track|tt|u|ul|var|video|wbr|xmp)$/i;    
    $scope.currentUrl = '';
    $scope.canNextPage = false;

	/**
     * Encode String
     * @param course_code
     * @returns {*}
     */
    
    $scope.scrollToTop = function() {
    	//alert("sfd");    	
    	$('#content')[0].scrollTop = 0;
    	$('.page').scrollTop = 0;
    	return;
    }
    
    $scope.onViewLoad = function(){
      console.log('view changed1');  
    };

    $scope.encode = function (course_code) {

        return $base64.encode(course_code);
    }

    /*
     Toggle course toolbar.
     */
    $scope.toggleTools = function () {
        $scope.tools = $scope.tools === false ? true : false;
    };

    /*
     Toggle course toolbar.
     */
    $scope.to_trusted = function (html_code) {
        return utilServices.to_trusted(html_code);
    }
    
    /**
     * convert html to text 
     */   

	$scope.convert_html = function (txt) {
		var protos = document.body.constructor === window.HTMLBodyElement;
	    var // This regex normalises anything between quotes
	        normaliseQuotes = /=(["'])(?=[^\1]*[<>])[^\1]*\1/g,
	        normaliseFn = function ($0, q, sym) { 
	            return $0.replace(/</g, '&lt;').replace(/>/g, '&gt;'); 
	        },
	        replaceInvalid = function ($0, tag, off, txt) {
	            var 
	                // Is it a valid tag?
	                invalidTag = protos && 
	                    document.createElement(tag) instanceof HTMLUnknownElement
	                    || !$scope.validHTMLTags.test(tag),
	
	                // Is the tag complete?
	                isComplete = txt.slice(off+1).search(/^[^<]+>/) > -1;
	
	            return invalidTag || !isComplete ? '&lt;' + tag : $0;
	        };
	
	    txt = txt.replace(normaliseQuotes, normaliseFn)
	             .replace(/<(\w+)/g, replaceInvalid);
	
	    var tmp = document.createElement("DIV");
	    tmp.innerHTML = txt;
	
	    return "textContent" in tmp ? tmp.textContent : tmp.innerHTML;
	}

    /*
     Load course - This is our main method will be called on page load.
     */
    $scope.loadCourse = function (pageNumber) {

        /*
         This will split the URL into array.
         sample: http://hhlearn.dev.oddovo.net:8081/dashboard/courses/TVMwMTA5/
         */
        var courseCodeEncypted = document.URL.split('/');
        $scope.currentUrl = document.URL;

        try {
            /*
             Encrypted course ID is stored at location 5. We will get it using courseCodeEncypted[courseCodeEncypted.length - 2]
             it's just doing base64 decoding.
             */
            //var courseCodeDecypted = courseCodeEncypted[courseCodeEncypted.length - 1];
            var courseCodeDecypted = courseCodeEncypted[5];
            if (courseCodeDecypted.slice(-1) == "#") {
            	courseCodeDecypted = courseCodeDecypted.substr(0, courseCodeDecypted.length-1);
            }            

            var courseCodeDecyptedArray = courseCodeDecypted.split(":");

            var course_id = $base64.decode(courseCodeDecyptedArray[0]);

            var is_monthly_saftey = $base64.decode(courseCodeDecyptedArray[1]);

            var assignment_id = $base64.decode(courseCodeDecyptedArray[2]);


            /*
             now we have decrypted course ID so lets get the course content.
             We will call our Factory....
             We are also passing params which will override the default params in factory method.
             */
            courseFactory.APIGetCourse({"courseID": course_id, "isMonthlySafety": is_monthly_saftey, "assignmentID": assignment_id, "pageNumber": pageNumber}).then(function (data) {

                // if test type is Competency, then it will be redirected test start page
                if (data.courseData.type == 3) {
                	$scope.startTest();
                	return;
                }
                
                $scope.courseData = data.courseData;
                $scope.orgData = data.orgData;
                $scope.utilData = data.utilData;
                $scope.userData = data.userData;
                /*
                 * Assigning resources data 
                 */
                if ($scope.courseData.page.length > 0 && 'resources' in $scope.courseData.page[0]) {
                	$scope.resourceData = $scope.courseData.page[0].resources;
                }
                
                /*
                 * Assigning font size
                 */
                $scope.fontsize = $scope.userData.fontsize.id;                
                
                /*$('#font_slider').slider('setValue', $scope.fontsize);
                $('#font_slider').slider().on('slideStop', function(ev){
				    $scope.changeDemoFontSize();
				});*/
                
                $scope.courseNotes = $scope.courseData.user_notes;

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

                    $scope.pageHTML = courseServices.replaceMediaTags(raw_html, data, $scope.resourceData);
                    
                    $scope.rawTextContent = $scope.convert_html($scope.pageHTML);

                }                
				
                /*
                 Just scroll the page to top :)
                 */
                //utilServices.scrollToTop();
                $scope.scrollToTop();
                
                // set font size
                $scope.$apply($scope.changeFontSize());                

                clearInterval($scope.refreshIntervalId);
                // if course type is 2 then we need to set the time to enable next button
                $scope.canNextPage = true;
                if (($scope.courseData.type == 2 || $scope.courseData.type == 4) && $scope.courseData.currentPage > 0) {
                	$scope.canNextPage = false;
                	$scope.duration = $scope.courseData.page[0].required_time;
                    $scope.refreshIntervalId = setInterval(function(){
                		$scope.$apply(function () {
                			if (--$scope.duration <= 1) {	                						            
					            $scope.canNextPage = true;
					        	clearInterval($scope.refreshIntervalId);
					        	$scope.duration = 0;
					        }
					    });
	                },  1000);					
                }
            });
        }
        /*
         If something goes wrong... then just set Course Data to false and we will take care of rest on HTML side.
         */
        catch (err) {
            $scope.courseData = false;
        }

    };
    
    $scope.setCurrentResource = function (id) {
    	$scope.currentResource = _.findWhere($scope.resourceData, {id: id});
        var modalInstance = $modal.open({
          templateUrl: 'currentResource.html',
          controller: 'currentResourceModalInstanceCtrl',
          resolve: {
            currentResource: function () {
              return $scope.currentResource;
            }
          }
        });
    	return true;
    };
    
    $scope.openDocument = function(id, extension) {
    	params = id + ',' + extension;
    	params = $scope.encode(params);
    	url = '/resources/files/' + params;
    	window.open(url, '_blank');
    	window.focus();
    	return;
    };

    /*	
     Load next page.
     */
    $scope.loadNextPage = function (pageNumber) {

        $scope.loadCourse(parseInt(pageNumber) + parseInt(1));


    };

    /*
     Load previous page.
     */
    $scope.loadPreviousPage = function (pageNumber) {

        $scope.loadCourse(parseInt(pageNumber) - parseInt(1));
        //clearInterval(refreshIntervalId);


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
	                /*$scope.logger.logCustom($scope.apiResponse.response.message, $scope.apiResponse.response.status)*/
	            }
	        });
	        
	        $scope.changeFontSize();
	        
            $scope.alerts.push({ type: 'success', msg: 'Your default course text size is set to ' + fontSize + 'px.' });
            $timeout(utilServices.closeAlert, 5000);
            $("html, body").animate({ scrollTop: 0 }, "slow");

        }
        catch (err) {

        }
    };
    
    /**
     * Change Font size 
     */
    $scope.changeFontSize = function () {
    	
    	size = $scope.fontsize;
    	    	
    	$('.course_content').removeClass('large');
    	$('.course_content').removeClass('small');
    	if (size == 1) {
    		$('.course_content').addClass('small');
    	} else if (size == 3) {
    		$('.course_content').addClass('large');
    	}
    }
    
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
    }
    
    
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
    
    /**
     * Start Test
     */
    
    $scope.startTest = function () {
    	
    	var courseCodeEncypted = document.URL.split('/')


        try {
            /*
             Encrypted course ID is stored at location 5. We will get it using courseCodeEncypted[courseCodeEncypted.length - 2]
             it's just doing base64 decoding.
             */
            var courseCodeDecypted = courseCodeEncypted[5];
            if (courseCodeDecypted.slice(-1) == "#") {
            	courseCodeDecypted = courseCodeDecypted.substr(0, courseCodeDecypted.length-1);
            }
            var courseCodeDecyptedArray = courseCodeDecypted.split(":");
            var course_id = $base64.decode(courseCodeDecyptedArray[0]);
            var is_monthly_saftey = $base64.decode(courseCodeDecyptedArray[1]);
            var assignment_id = $base64.decode(courseCodeDecyptedArray[2]);
            		
	    	/**
	         * assignment start API
	         */
	        courseFactory.APITestStart({assignmentID:assignment_id, courseID:course_id, monthlySafetyCourse:is_monthly_saftey}).then(function (data) {
	
	            /**
	             * storing response form api.
	             */
	            $scope.apiResponse = data;
				
				test_attempt_id = $scope.apiResponse.response.testAttemptID;				
									
	             if (!_.isUndefined($scope.apiResponse.response)) {
	                /**
	                 * log message and show notification on screen.
	                 */
	                //$scope.logger.logCustom($scope.apiResponse.response.message, $scope.apiResponse.response.status)
	
	                if ($scope.apiResponse.response.status == "success" ) {	
	                	window.location = '/dashboard/test/'+$scope.encode(test_attempt_id)+':'+$scope.encode(course_id)+':'+$scope.encode(is_monthly_saftey)+':'+$scope.encode(assignment_id);	                    
	                } else {
	                	alert($scope.apiResponse.response.message);
	                }
	            }
	        });
	    }
	    catch (err) {

        }    	   	
    };
    
    $scope.speakCourseWord = function () {
    	soundManager.setup({
	        url: '/',
	        preferFlash: false,
	        onready: function() {
	          if (!window.GoogleTTS) {
	            $("#error").text("Sorry, the google-tts script couldn't be loaded.");
	            return;
	          }
	          $scope.googleTTS = new window.GoogleTTS();
	                    
	          $scope.googleTTS.getPlayer(function (err, player) {
	            if (err) {
	              console.log(err.toString());
	            }	            
	          });
	          var text = "This course is written for personnel that provide care to homecare and hospice.";
	          if ($scope.googleTTS) {    		
			    	$scope.googleTTS.play(text, 'en', function(err) {
			          if (err) {
			            $("#error").text(err.toString());
			          }
			          console.log('Finished playing');
			        });	        
			    } 
	        }
	      });    	
    	
    	return;
    };


    /* $scope.$watch('pageHTML', function (n, o) {
     $("[data-toggle=tooltip]").tooltip();
     });  */

    $scope.loadCourse();

    $scope.openCourseNotesModal = function() {
        var modalInstance = $modal.open({
          templateUrl: 'courseNotes.html',
          controller: 'courseNoteModalInstanceCtrl',
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
          controller: 'textSizeModalInstanceCtrl',
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
          $scope.changeFontSize();
        });
    };

    $scope.openGlossaryWordsModal = function() {
        var modalInstance = $modal.open({
          templateUrl: 'glossaryWords.html',
          controller: 'glossaryWordsModalInstanceCtrl',
          resolve: {
            courseData: function () {
              return $scope.courseData;
            }
          }
        });
    };

    $scope.openReferralAgenciesModal = function() {
        var modalInstance = $modal.open({
          templateUrl: 'referralAgencies.html',
          controller: 'referralAgenciesModalInstanceCtrl',
          resolve: {
            courseData: function () {
              return $scope.courseData;
            }
          }
        });
    };

    $scope.openAppendixModal = function() {
        var modalInstance = $modal.open({
          templateUrl: 'appendix.html',
          controller: 'appendixModalInstanceCtrl',
          resolve: {
            courseData: function () {
              return $scope.courseData;
            }
          }
        });
    };

}]);

angular.module('course').controller('courseNoteModalInstanceCtrl', function ($scope, $modalInstance, courseFactory, courseData, courseNotesLimit ) {

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


angular.module('course').controller('textSizeModalInstanceCtrl', function ($scope, $modalInstance, courseFactory, courseData, fontSize) {

    $scope.courseData = courseData;
    $scope.fontSizeSlider = 14;
    $scope.fontSize = fontSize;

    //$('#font_slider').slider('setValue', $scope.fontsize);
    //$('#font_slider').slider().on('slideStop', function(ev){
    //    $scope.changeDemoFontSize();
    //});

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

angular.module('course').controller('glossaryWordsModalInstanceCtrl', function ($scope, $modalInstance, courseData ) {

    $scope.courseData = courseData;

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };

    $scope.print = function () {
        printWindow($('.modal-content'));
    }

});

angular.module('course').controller('appendixModalInstanceCtrl', function ($scope, $modalInstance, courseData ) {

    $scope.courseData = courseData;

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };

});

angular.module('course').controller('referralAgenciesModalInstanceCtrl', function ($scope, $modalInstance, courseData ) {

    $scope.courseData = courseData;

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };

});


angular.module('course').controller('currentResourceModalInstanceCtrl', function ($scope, $base64, $modalInstance, currentResource ) {

    $scope.currentResource = currentResource;

    $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
    };

    $scope.encode = function (course_code) {
        return $base64.encode(course_code);
    }

    $scope.openDocument = function(id, extension) {
    	params = id + ',' + extension;
    	params = $scope.encode(params);
    	url = '/resources/files/' + params;
    	window.open(url, '_blank');
    	window.focus();
    	return;
    };

});
