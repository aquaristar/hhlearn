angular.module("signupApp").controller('signupCtrl', ['$scope', 'logger', 'signupFactory', 'utilsHelpers', function ($scope, logger, signupFactory, utilsHelpers) {

    $scope.org_name = '';

    $scope.first_name = '';

    $scope.last_name = '';

    $scope.email = '';

    $scope.password = '';

    $scope.username = '';

    $scope.utilsHelpers = utilsHelpers;

    $scope.logger = logger;


    $scope.signupUser = function () {


        signupFactory.APIAuthSignup({"org_name": $scope.org_name, "username": $scope.username, "first_name": $scope.first_name, "last_name": $scope.last_name, "email": $scope.email, "password": $scope.password}).then(function (data) {

            /**
             * storing response form api.
             */
            $scope.apiResponse = data;

            /**
             * log message and show notification on screen.
             */
            $scope.logger.logCustom($scope.apiResponse.response.message, $scope.apiResponse.response.status);


            if ($scope.apiResponse.code == "response_signup_successful" && $scope.apiResponse.status == "success") {
                window.location = '/signup/successful'; //one level up
            }

        });

    }

}]);

