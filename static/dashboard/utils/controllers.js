/**
 The default controller for Util.

 @dependency: $scope              - the main scope
 */

angular.module("utilsApp").controller("notifyCtrl", ["$scope", "logger", function ($scope, logger) {


    /*
     triggered when we initiate a Ajax call.
     */
    $scope.$on('request', function (event, config) {

        $scope.alerts = [];

        /**
         No need to show user that we are making request because they will see loading spinner.
         */
        //$scope.alerts.push({ type: 'success', msg: 'requesting...' });


    });


    /*
     triggered when we initiate a Ajax call and it fails from our side and never reaches end-point
     */
    $scope.$on('requestError', function (event, rejection) {

        $scope.alerts = [];

        $scope.alerts.push({ type: 'danger', msg: 'Request failed. Please try again.' });


    });


    /*
     triggered when we initiate a Ajax call and we get response(HTTP 200)
     */
    $scope.$on('response', function (event, response) {

        $scope.alerts = [];

        /**
         No need to show user that we got response back.
         */
        // $scope.apiMessages.push({ type: 'success', msg: 'We got response back.' });


    });


    /*
     triggered when we initiate a Ajax call and we get error in response.
     */
    $scope.$on('responseError', function (event, rejection) {

        $scope.alerts = [];

        $scope.alerts.push({ type: 'danger', msg: 'Server error. Please try again.' });


    });


}]).controller("utilsCtrl", ["$scope", "utilsFactory", "profileFactory", function ($scope, utilsFactory, profileFactory) {

    $scope.utilsFactory = utilsFactory;

    $scope.profileFactory = profileFactory;

    $scope.profile = {};

    /**
     * method to login user.
     */
    $scope.toggleMenu = function () {

        $scope.utilsFactory.APIToggleMenu({


        }).then(function (data) {

        });


        return true;

    };

     /**
     * method to login user.
     */
    $scope.loadProfileMin = function () {

        /**
         * calling method in factory to make API call.
         */
        $scope.profileFactory.APIProfileMin().then(function (data) {

            /**
             * storing response form api.
             */
            $scope.profile = data.profile;


        });

    };

    $scope.loadProfileMin();

}]);
