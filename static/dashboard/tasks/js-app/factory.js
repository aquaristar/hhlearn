/*angular.module("tasks").factory('taskStorage', function() {
    var DEMO_TASKS, STORAGE_ID;
    STORAGE_ID = 'tasks';
    DEMO_TASKS = '[\
        {"title": "Finish homework", "completed": true, "overdue": true, "assigned_by": "Robert Tompson", "due_date": "09/12/2014"},\
        {"title": "Make a call", "completed": true, "overdue": false, "assigned_by": "Robert Tompson", "due_date": "09/12/2014"},\
        {"title": "Build a snowman!", "completed": false, "overdue": true, "assigned_by": "Robert Tompson", "due_date": "09/12/2014"},\
        {"title": "Tango! Tango! Tango!", "completed": false, "overdue": false, "assigned_by": "Robert Tompson", "due_date": "09/12/2014"},\
        {"title": "Play games with friends", "completed": false, "overdue": false, "assigned_by": "Robert Tompson", "due_date": "09/12/2014"},\
        {"title": "Shopping", "completed": false, "overdue": false, "assigned_by": "Robert Tompson", "due_date": "09/12/2014"}\
\
    ]';
    return {
      get: function() {
        //return JSON.parse(localStorage.getItem(STORAGE_ID) || DEMO_TASKS);
        return JSON.parse(DEMO_TASKS);
      },
      put: function(tasks) {
        return localStorage.setItem(STORAGE_ID, JSON.stringify(tasks));
      }    
}});*/

angular.module("tasks").factory("tasksFactory", ['$http', '$q', function ($http, $q) {

    var factory = {};


    factory.APIGetTasks = function (options) {

        var d = $q.defer();

        var defaults = {
           "format": "json"
           // "SORT": "name",
           // "PAGENUMBER": "1"
        };

        $http.get("/api/v1/tasks", { params: _.extend(defaults, options)}).success(function (data) {

            d.resolve(data);
        });

        return d.promise;
    };
    
    factory.APITaskChange = function (options) {

        var d = $q.defer();

        var defaults = {
           "format": "json"
           // "SORT": "name",
           // "PAGENUMBER": "1"
        };

        $http.post("/api/v1/tasks", _.extend(defaults, options)).success(function (data, status, headers, config) {

            d.resolve(data, status, headers, config);

        }).error(function (data, status, headers, config) {

            d.resolve(data, status, headers, config);

        }).finally(function (data, status, headers, config) {

            d.resolve(data, status, headers, config);

        });

        return d.promise;
    };
   
    return factory;
}]);