angular.module("resetApp").controller('resetCtlr', ['$scope','logger', 'resetFactory','utilsHelpers', function ($scope, logger, resetFactory, utilsHelpers) {

    $scope.username = '';

    $scope.password = '';

    $scope.rememberMe = false;

    $scope.responseData = {};

    $scope.utilsHelpers = utilsHelpers;

    $scope.logger = logger;

    $scope.resetPassword = function () {


        resetFactory.APIAuthReset({"username": $scope.username, "password": $scope.password, "rememberMe": $scope.rememberMe}).then(function (data) {

            /**
             * storing response form api.
             */
            $scope.apiResponse = data;

            /**
             * log message and show notification on screen.
             */
            $scope.logger.logCustom($scope.apiResponse.response.message, $scope.apiResponse.response.status);


            if($scope.apiResponse.code == "response_login_successful" && $scope.apiResponse.status == "success" ) {
                document.location.href = '../'; //one level up
            }

        });

    }

}]).controller('resetCtlr', ['$scope','logger', 'resetFactory','utilsHelpers', function ($scope, logger, resetFactory, utilsHelpers) {

    $scope.username = '';

    $scope.password = '';

    $scope.password_confirm = '';

    $scope.password_reset_token = '';

    $scope.rememberMe = false;

    $scope.responseData = {};

    $scope.utilsHelpers = utilsHelpers;

    $scope.logger = logger;

    $scope.resetPassword = function () {


        resetFactory.APIAuthReset({"username": $scope.username, "password": $scope.password, "rememberMe": $scope.rememberMe}).then(function (data) {

            /**
             * storing response form api.
             */
            $scope.apiResponse = data;

            /**
             * log message and show notification on screen.
             */
            $scope.logger.logCustom($scope.apiResponse.response.message, $scope.apiResponse.response.status);


            if($scope.apiResponse.code == "response_login_successful" && $scope.apiResponse.status == "success" ) {
                document.location.href = '../'; //one level up
            }

        });

    };

    $scope.saveNewPassword = function () {


        resetFactory.APIAuthSaveNewPassword({"password": $scope.password, "password_confirm": $scope.password_confirm, "password_reset_token": $scope.password_reset_token}).then(function (data) {

            /**
             * storing response form api.
             */
            $scope.apiResponse = data;

            /**
             * log message and show notification on screen.
             */
            $scope.logger.logCustom($scope.apiResponse.response.message, $scope.apiResponse.response.status);


            if($scope.apiResponse.response.code == "response_password_updated" && $scope.apiResponse.response.status == "success" ) {
                document.location.href = '/'; //one level up
            }

        });

    }

}]);

