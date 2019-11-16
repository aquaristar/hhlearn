angular.module("loginApp").controller('loginCtlr', ['$scope','logger', 'loginFactory','utilsHelpers', function ($scope, logger, loginFactory, utilsHelpers) {

    $scope.username = '';

    $scope.password = '';

    $scope.rememberMe = false;

    $scope.responseData = {};

    $scope.utilsHelpers = utilsHelpers;

    $scope.logger = logger;

    $scope.loginUser = function () {


        loginFactory.APIAuthLogin({"username": $scope.username, "password": $scope.password, "rememberMe": $scope.rememberMe}).then(function (data) {

            /**
             * storing response form api.
             */
            $scope.apiResponse = data;

            /**
             * log message and show notification on screen.
             */
            $scope.logger.logCustom($scope.apiResponse.response.message, $scope.apiResponse.response.status);


            if($scope.apiResponse.response.code == "response_login_successful" && $scope.apiResponse.response.status == "success" ) {
                window.location = '/dashboard'; //one level up
            }

        });

    }

}]);

