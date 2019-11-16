angular.module("tasks").controller('tasksController', ['$scope', '$sce', 'filterFilter', 'logger', '$filter', '$location', '$base64', '$timeout', 'tasksFactory', 'utilServices', function ($scope, $sce, filterFilter, logger, $filter, $location, $base64, $timeout, tasksFactory, utilServices) {
      var tasks;
      tasks = $scope.tasks = {};
      $scope.newTask = '';      
      $scope.editedTask = null;
      var editTaskTitle;
      editTaskTitle = $scope.editTaskTitle = '';
      var editTaskCompleted;
      editTaskComplete = $scope.editTaskCompleted = false;
      $scope.user = 0;
      
      $scope.perPage = 10;
    
      $scope.taskSearchKeywords = '';
      $scope.currentTaskPage = 1;
      $scope.filteredTasks = [];
      
      $scope.onFilterChange = function() {
	    $scope.selectTaskPage(1);
	    $scope.currentTaskPage = 1;
	    return $scope.row = '';
	  };
	
      $scope.searchTask = function() {
		//$scope.taskSearchKeywords = $('#alert_search').val();		
	    $scope.filteredTasks = $filter('filter')($scope.tasks, $scope.taskSearchKeywords);
	    return $scope.onFilterChange();
	  };	
	
	  $scope.selectTaskPage = function (page) {
        var end, start;
        start = (page - 1) * $scope.perPage;
        end = start + $scope.perPage;
        return $scope.currentFilteredTasks = $scope.filteredTasks.slice(start, end);        
      };
      
      $scope.statusFilter = {
        completed: false
      };
      $scope.remainingCount = 0;
      
      $scope.due_date = '';
      
      $scope.dateOptions = {
		  'year-format': "'yy'",
		  'starting-day': 1
		};
	  $scope.format = 'MM/dd/yyyy';
	  
      $scope.filter = function(filter) {
        switch (filter) {
          case 'all':
            return $scope.statusFilter = '';
          case 'active':
            return $scope.statusFilter = {
              completed: false
            };
          case 'completed':
            return $scope.statusFilter = {
              completed: true
            };
        }
      };
      
      $scope.getAllTasks = function() {
      	try {
            
            tasksFactory.APIGetTasks({}).then(function (data) {
                /*
                 Assigning test related data.
                 */
                $scope.tasks = data.tasks;
                $scope.searchTask();
            	$scope.selectTaskPage($scope.currentTaskPage);                
            	$scope.tzCode = data.tzCode;
            	$scope.user = data.user;
            	
            	$scope.remainingCount = filterFilter($scope.tasks, {
			        completed: false
			     }).length;            	                

            });
        }
        catch (err) {
            $scope.alertData = false;
        }
      };
      
      $scope.add = function() {
        var newTask;
        newTask = $scope.newTask.trim();
        if (newTask.length === 0) return;
        //if ($scope.due_date =='') return;
        tasksFactory.APITaskChange({"method": "add", "description": newTask, "due_date": $filter('date')($scope.due_date, $scope.format)}).then(function (data) {
	        $scope.tasks.push(data.task);
	        logger.logSuccess('New task: "' + newTask + '" added');	        
	        $scope.newTask = '';
	        $scope.due_date = '';
	        
	        $scope.searchTask();
	        $scope.changeTaskCount();
	        
	        return $scope.remainingCount++;	        
        });        
      };
      
      $scope.edit = function(task) {
      	if (task.assigned_by_user == $scope.user || task.assigned_by_user == undefined) {
      		task.editCompleted = task.title;
        	return $scope.editedTask = task;
        }
        return;        
      };
      
      $scope.doneEditing = function(task) {
        //$scope.editedTask = null;        
        if (task.title == '') {
        	task.title = editedTask.title;
          	return;
        } else {
        	tasksFactory.APITaskChange({"method": "change", "task_id": task.id, "description": task.tasks_description, "due_date": $filter('date')(task.date_due, $scope.format)}).then(function (data) {
        		task.tasks_description = task.tasks_description.trim();      		
        		//logger.log('Task updated');
          	});          
        }
        $scope.editedTask = null;
                
      };
      $scope.remove = function(task) {
        var index;        
        $scope.editedTask = task        
        
        tasksFactory.APITaskChange({"method": "delete", "task_id": task.id}).then(function (data) {
	        $scope.remainingCount -= $scope.editedTask.completed ? 0 : 1;
        	index = $scope.tasks.indexOf($scope.editedTask);
        	$scope.tasks.splice(index, 1);
	        logger.logSuccess('Task removed');
	        $scope.searchTask();
	        $scope.editedTask = null;
	        
	        $scope.changeTaskCount();
	        return;     
        });        
      };
      $scope.completed = function(task) {
        
        tasksFactory.APITaskChange({"method": "change", "task_id": task.id, "completed": task.completed}).then(function (data) {
        	task = data.task;
        	$scope.remainingCount += task.completed ? -1 : 1;
        	$scope.changeTaskCount();
        	if (task.completed) {
	          if ($scope.remainingCount > 0) {
	            if ($scope.remainingCount === 1) {
	              return logger.log('Almost there! Only ' + $scope.remainingCount + ' task left');
	            } else {
	              return logger.log('Good job! Only ' + $scope.remainingCount + ' tasks left');
	            }
	          } else {
	            return logger.logSuccess('Congrats! All done :)');	            
	          }
	        }
	        $scope.searchTask();	        
	        	        	        
        });
      };
      $scope.clearCompleted = function() {
      	tasksFactory.APITaskChange({"method": "clear_all_completed"}).then(function (data) {
	        $scope.tasks = tasks = $scope.tasks.filter(function(val) {
	          return !val.completed;	          
	        });	        	        
	        $scope.searchTask();
	        $scope.changeTaskCount();
	    });	    	    	            
      };
      
      $scope.markAll = function(completed) {
      	tasksFactory.APITaskChange({"method": "mark_all_as_done", "completed": completed}).then(function (data) {
	        $scope.tasks.forEach(function(task) {
	          return task.completed = completed;
	        });
        	$scope.remainingCount = completed ? 0 : $scope.tasks.length;
        	$scope.changeTaskCount();
       	});
       	$scope.searchTask();                
        if (completed) return logger.logSuccess('Congrats! All done :)');        
        
      };
      $scope.$watch('remainingCount == 0', function(val) {
        return $scope.allChecked = val;
      });
      
      $scope.changeTaskCount = function() {
      	if ($scope.remainingCount > 0) {
      		jQuery("#task_count").text($scope.remainingCount);
      	} else {
      		jQuery("#task_count").text("");
      	}
      };
      
      $scope.getAllTasks();
      
      return $scope.$watch('remainingCount', function(newVal, oldVal) {
        return true;//$rootScope.$broadcast('taskRemaining:changed', newVal);
      });

}]);
