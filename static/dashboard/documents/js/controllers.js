angular.module("documents").controller('documentsController', ['$modal', '$scope', '$sce', '$filter', '$location', '$base64', '$timeout', 'documentsFactory', 'utilServices', function ($modal, $scope, $sce, $filter, $location, $base64, $timeout, documentsFactory, utilServices) {
	
	$scope.currentResource = {};
    
    /** 
     * variables for epostings
     */
    $scope.ePostings = {};    
    $scope.perPage = 10;
    
    $scope.ePostingsSearchKeywords = '';
	$scope.currentEPosting = {};	 
    
    $scope.currentEPostingPage = 1;
    $scope.filteredEPostings = [];    
    
    $scope.ePostingSort = 'electronically_posted_official_description';
    
    /** 
     * variables for frequents
     */
    $scope.frequents = {};
    
    $scope.frequentsSearchKeywords = '';
	$scope.currentFrequent = {};	 
    
    $scope.currentFrequentPage = 1;
    $scope.filteredFrequents = [];    
    
    $scope.frequentSort = '';
    
    /** 
     * variables for custom forms
     */
    $scope.forms = 0;
    
    $scope.formsSearchKeywords = '';
	$scope.currentForm = {};	 
    
    $scope.currentFormPage = 1;
    $scope.filteredForms = [];    
    
    $scope.formSort = 'resource_name';
    
    /** 
     * variables for custom publications
     */
    $scope.publications = 0;
    
    $scope.publicationsSearchKeywords = '';
	$scope.currentPublication = {};	 
    
    $scope.currentPublicationPage = 1;
    $scope.filteredPublications = [];    
    
    $scope.publicationSort = 'resource_name';
    
    /** 
     * variables for custom videos
     */
    $scope.videos = 0;
    
    $scope.videosSearchKeywords = '';
	$scope.currentVideo = {};	 
    
    $scope.currentVideoPage = 1;
    $scope.filteredVideos = [];    
    
    $scope.videoSort = 'resource_name';
    
    $scope.Math = Math;
        
    
    $scope.to_trusted = function (html_code) {
        return utilServices.to_trusted(html_code);
    }
    
    $scope.encode = function (code) {

        return $base64.encode(code);
    }
    
    /**
     * Electronic Posting Filter functions
     */   
	$scope.onEPFilterChange = function() {
	    $scope.selectEPostingPage(1);
	    $scope.currentEPostingPage = 1;
	    return $scope.row = '';
	};
	
	$scope.onEPNumPerPageChange = function() {
	    $scope.selectEPostingPage(1);
	    return $scope.currentEPostingPage = 1;
	};
	
	$scope.onEPOrderChange = function() {
	    $scope.selectEPostingPage(1);
	    return $scope.currentEPostingPage = 1;
	};
	
	$scope.searchEPostings = function() {
		$scope.ePostingsSearchKeywords = $('#ep_search').val();
	    $scope.filteredEPostings = $filter('filter')($scope.ePostings, $scope.ePostingsSearchKeywords);
	    return $scope.onEPFilterChange();	    
	};
	
	/*$scope.order = function(rowName) {
	    if ($scope.row === rowName) return;
	    $scope.row = rowName;
	    $scope.currentFilteredHistories = $filter('orderBy')($scope.testHistory, rowName);
	    return $scope.onOrderChange();
	};*/
    

    $scope.selectEPostingPage = function (page) {
        var end, start;
        start = (page - 1) * $scope.perPage;
        end = start + $scope.perPage;
        return $scope.currentFilteredEPostings = $scope.filteredEPostings.slice(start, end);        
    };
    
  
  	$scope.setCurrentEPosting = function (obj) {
  		$scope.currentEPosting = obj;
  		$scope.currentResource = obj;

        var modalInstance = $modal.open({
          templateUrl: 'my.html',
          controller: 'documentsModalInstanceCtrl',
          resolve: {
            currentResource: function () {
              return $scope.currentResource;
            }
          }
        });

  		return true;
  	}
  	
  	/**
     * Frequents Filter functions
     */   
	$scope.onFrequentFilterChange = function() {
	    $scope.selectFrequentPage(1);
	    return $scope.currentFrequentPage = 1;	    
	};
	
	$scope.onFrequentNumPerPageChange = function() {
	    $scope.selectFrequentPage(1);
	    return $scope.currentFrequentPage = 1;	    
	};
	
	$scope.onFrequentOrderChange = function() {
	    $scope.selectFrequentPage(1);
	    return $scope.currentFrequentPage = 1;
	};
	
	$scope.searchFrequents = function() {
		$scope.frequentsSearchKeywords = $('#frequent_search').val();
	    $scope.filteredFrequents = $filter('filter')($scope.frequents, $scope.frequentsSearchKeywords);
	    return $scope.onFrequentFilterChange();	    
	};
	
    $scope.selectFrequentPage = function (page) {
        var end, start;
        start = (page - 1) * $scope.perPage;
        end = start + $scope.perPage;
        return $scope.currentFilteredFrequents = $scope.filteredFrequents.slice(start, end);        
    };
    
  
  	$scope.setCurrentFrequent = function (obj) {
  		$scope.currentFrequent = obj;
  		$scope.currentResource = obj;

        var modalInstance = $modal.open({
          templateUrl: 'my.html',
          controller: 'documentsModalInstanceCtrl',
          resolve: {
            currentResource: function () {
              return $scope.currentResource;
            }
          }
        });
  		return true;
  	}

  	
  	/**
     * Custom Forms Filter functions
     */   
	$scope.onFormFilterChange = function() {
	    $scope.selectFormPage(1);
	    $scope.currentFormPage = 1;
	    return $scope.row = '';
	};
	
	$scope.onFormNumPerPageChange = function() {
	    $scope.selectFormPage(1);
	    return $scope.currentFormPage = 1;
	};
	
	$scope.onFormOrderChange = function() {
	    $scope.selectFormPage(1);
	    return $scope.currentFormPage = 1;
	};
	
	$scope.searchForms = function() {
		$scope.formsSearchKeywords = $('#form_search').val();
	    $scope.filteredForms = $filter('filter')($scope.forms, $scope.formsSearchKeywords);
	    return $scope.onFormFilterChange();	    
	};
	
    $scope.selectFormPage = function (page) {
        var end, start;
        start = (page - 1) * $scope.perPage;
        end = start + $scope.perPage;
        return $scope.currentFilteredForms = $scope.filteredForms.slice(start, end);        
    };
    
  
  	$scope.setCurrentForm = function (obj) {
  		$scope.currentForm = obj;
  		$scope.currentResource = obj;

        var modalInstance = $modal.open({
          templateUrl: 'my.html',
          controller: 'documentsModalInstanceCtrl',
          resolve: {
            currentResource: function () {
              return $scope.currentResource;
            }
          }
        });

  		return true;
  	}

  	/**
     * Custom Publications Filter functions
     */   
	$scope.onPublicationFilterChange = function() {
	    $scope.selectPublicationPage(1);
	    return $scope.currentPublicationPage = 1;	    
	};
	
	$scope.onPublicationNumPerPageChange = function() {
	    $scope.selectPublicationPage(1);
	    return $scope.currentPublicationPage = 1;
	};
	
	$scope.onPublicationOrderChange = function() {
	    $scope.selectPublicationPage(1);
	    return $scope.currentPublicationPage = 1;
	};
	
	$scope.searchPublications = function() {
		$scope.publicationsSearchKeywords = $('#publication_search').val();
	    $scope.filteredPublications = $filter('filter')($scope.publications, $scope.publicationsSearchKeywords);
	    return $scope.onPublicationFilterChange();	    
	};
	
    $scope.selectPublicationPage = function (page) {
        var end, start;
        start = (page - 1) * $scope.perPage;
        end = start + $scope.perPage;
        return $scope.currentFilteredPublications = $scope.filteredPublications.slice(start, end);        
    };
    
  
  	$scope.setCurrentPublication = function (obj) {
  		$scope.currentPublication = obj;
  		$scope.currentResource = obj;

        var modalInstance = $modal.open({
          templateUrl: 'my.html',
          controller: 'documentsModalInstanceCtrl',
          resolve: {
            currentResource: function () {
              return $scope.currentResource;
            }
          }
        });

  		return true;
  	}
  	
  	/**
     * Custom Videos Filter functions
     */   
	$scope.onVideoFilterChange = function() {
	    $scope.selectVideoPage(1);
	    return $scope.currentVideoPage = 1;	    
	};
	
	$scope.onVideoNumPerPageChange = function() {
	    $scope.selectVideoPage(1);
	    return $scope.currentVideoPage = 1;	 
	};
	
	$scope.onVideoOrderChange = function() {
	    $scope.selectVideoPage(1);
	    return $scope.currentVideoPage = 1;	 
	};
	
	$scope.searchVideos = function() {
		$scope.videosSearchKeywords = $('#video_search').val();
	    $scope.filteredVideos = $filter('filter')($scope.videos, $scope.videosSearchKeywords);
	    return $scope.onVideoFilterChange();	    
	};
	
    $scope.selectVideoPage = function (page) {
        var end, start;
        start = (page - 1) * $scope.perPage;
        end = start + $scope.perPage;
        return $scope.currentFilteredVideos = $scope.filteredVideos.slice(start, end);        
    };
    
  
  	$scope.setCurrentVideo = function (obj) {
  		$scope.currentVideo = obj;
  		$scope.currentResource = obj;

        var modalInstance = $modal.open({
          templateUrl: 'my.html',
          controller: 'documentsModalInstanceCtrl',
          resolve: {
            currentResource: function () {
              return $scope.currentResource;
            }
          }
        });

  		return true;
  	}

    /*
     Load Documents - This is our main method will be called on page load.
     */
    $scope.loadDocuments = function () {
        /*
         This will split the URL into array.
         sample: http://hhlearn.dev.oddovo.net:8081/dashboard/courses/TVMwMTA5/
         */
        var courseCodeEncypted = document.URL.split('/')

        try {
            
            documentsFactory.APIGetDocuments({}).then(function (response) {
                
                if (response.status == "success") {
                	
                	$scope.ePostings = response.data.e_postings;
                	$scope.searchEPostings();
                	$scope.selectEPostingPage($scope.currentEPostingPage);
                	
                	$scope.frequents = response.data.frequents;
                	$scope.searchFrequents();
                	$scope.selectFrequentPage($scope.currentFrequentPage);
                	                	
                	$scope.forms = response.data.forms;
                	if (response.data.forms != 0) {                		
	                	$scope.searchForms();
	                	$scope.selectFormPage($scope.currentFormPage);
	                }                	
                	
                	$scope.publications = response.data.publications;
                	if (response.data.publications != 0) {                		
	                	$scope.searchPublications();
	                	$scope.selectPublicationPage($scope.currentPublicationPage);
	                }                	
                	
                	$scope.videos = response.data.videos;
                	if (response.data.videos != 0) {                		
	                	$scope.searchVideos();
	                	$scope.selectVideoPage($scope.currentVideoPage);
	                }
                		
                } else {
                	alert(response.data);
                }         
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
    
    $scope.openDocument = function(id, extension) {
    	params = id + ',' + extension;
    	params = $scope.encode(params);
    	url = '/resources/files/' + params;
    	window.open(url, '_blank');
    	window.focus();
    	return;
    };
    
    $scope.loadDocuments();    

}]);

angular.module('documents').controller('documentsModalInstanceCtrl', function ($scope, $modalInstance, currentResource) {

  $scope.currentResource = currentResource;
  $scope.cancel = function () {
    $modalInstance.dismiss('cancel');
  };
});
