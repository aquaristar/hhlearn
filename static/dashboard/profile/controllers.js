/**
 * Authentication Controller.
 *
 * @dependencies
 *     $scope           - Angular JS scope.
 *     loginFactory     - authentication factory
 *     logger           - logging and notification factory.
 */
angular.module("profileApp").controller('profileCtrl', ['$scope', 'profileFactory', 'logger', function ($scope, profileFactory, logger) {

    /**
     * variable to hold data returned from API
     * @type {{}}
     */
    $scope.apiResponse = {};

    /**
     * this will hold logged in user profile info.
     */

    $scope.profile = {};

    /**
     * notification factory.
     */
    $scope.logger = logger;

    $scope.profileFactory = profileFactory;
	
	$scope.facebookOn = true;
	$scope.twitterOn = true;
	$scope.pinterestOn = true;
	$scope.instagramOn = true;
    $scope.dt = new Date();

    /**
     * method to login user.
     */
    $scope.loadProfile = function () {

        /**
         * calling method in factory to make API call.
         */
        $scope.profileFactory.APIProfile().then(function (data) {

            /**
             * storing response form api.
             */
            $scope.apiResponse = data;

            $scope.profile = data.profile;

            if (!_.isUndefined($scope.apiResponse.response)) {
                /**
                 * log message and show notification on screen.
                 */
                $scope.logger.logCustom($scope.apiResponse.response.message, $scope.apiResponse.response.status)
            }


        });

    };
    /**
     * method to login user.
     */
    $scope.saveProfile = function () {


        $scope.profileFactory.APISaveProfile({

            "email": $scope.loggedin_user.user.email ,

            "first_name": $scope.loggedin_user.user.first_name,

            "last_name": $scope.loggedin_user.user.last_name,

            "address": $scope.loggedin_user.address,

            "city": $scope.loggedin_user.city,

            "state": $scope.loggedin_user.state,

            "postal_code": $scope.loggedin_user.postal_code,

            "country": $scope.loggedin_user.country,

            "phone": $scope.loggedin_user.phone

        }).then(function (data) {

            /**
             * storing response form api.
             */
            $scope.apiResponse = data;

            if (!_.isUndefined($scope.apiResponse.response)) {
                /**
                 * log message and show notification on screen.
                 */
                logger.logCustom($scope.apiResponse.response.message, $scope.apiResponse.response.status)
            }


        });


        return true;

    };

    /**
     * load user profile data on page load.
     */
    $scope.loadProfile();

}]);
