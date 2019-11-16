angular.module("metrics").controller('metricsController', ['$scope', '$sce', '$filter', '$location', '$base64', '$timeout', 'metricsFactory', 'utilServices', function ($scope, $sce, $filter, $location, $base64, $timeout, metricsFactory, utilServices) {

    $scope.metrics = {};
    $scope.Math = Math;
    $scope.safety_course_history = {};
    $scope.gpa_chart = {};
    $scope.gpa_chart.data = {};
    $scope.gpa_chart.options = {};
    
    
    $scope.to_trusted = function (html_code) {
        return utilServices.to_trusted(html_code);
    }
    
    
    $scope.encode = function (code) {

        return $base64.encode(code);
    }
    
    $scope.prepareGpaChart = function(data) {
    	
    	months = [];
    	my_gpas = [];
    	location_gpas = [];
    	for (i = 0; i < 12; i ++) {
    		months[i] = [i+1, data.my_gpas[i].month];
    		my_gpas[i] = [i+1, data.my_gpas[i].value];
    		location_gpas[i] = [i+1, data.location_gpas[i].value];
    	}
    	    	
    	$scope.gpa_chart.data = [
	        {
	          data: my_gpas,
	          label: 'My GPA'
	        }, {
	          data: location_gpas,
	          label: 'Location GPA',
	          lines: {
	            fill: false
	          }
	        }
	    ];
	    
	    $scope.gpa_chart.options = { 
		    series: {
		      lines: {
		        show: true,
		        fill: true,
		        fillColor: {
		          colors: [
		            {
		              opacity: 0
		            }, {
		              opacity: 0.3
		            }
		          ]
		        }
		      },
		      points: {
		        show: true,
		        lineWidth: 2,
		        fill: true,
		        fillColor: "#ffffff",
		        symbol: "circle",
		        radius: 5
		      }
		    },
		    colors: ["#31C0BE", "#8170CA", "#E87352"],
		    tooltip: true,
		    tooltipOpts: {
		      defaultTheme: false,
		      content: "%s | %y"
		    },
		    grid: {
		      hoverable: true,
		      clickable: true,
		      tickColor: "#f9f9f9",
		      borderWidth: 1,
		      borderColor: "#eeeeee"
		    },
		    xaxis: {
		      ticks: months,
		      tickDecimals: 0
		    },
		    yaxis: {                
			  tickDecimals: 2
			}
		};
		$.plot($("#flot-gpa"), $scope.gpa_chart.data, $scope.gpa_chart.options);
	    
    }
    /*
     Load test - This is our main method will be called on page load.
     */
    $scope.loadMetrics = function () {
        /*
         This will split the URL into array.
         sample: http://hhlearn.dev.oddovo.net:8081/dashboard/courses/TVMwMTA5/
         */
        var courseCodeEncypted = document.URL.split('/')

        try {
            
            metricsFactory.APIGetMetrics({}).then(function (response) {
                $scope.metrics = response.metrics;
                $scope.safety_course_history = response.safety_course_history;  
                $scope.prepareGpaChart(response.gpa_charts_data)            
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

    
    $scope.loadMetrics();    

}]);
