angular.module("dashboardApp").service("utilServices", ['$http', '$sce', function ($http, $sce) {

    /*
     ============================================================================
     HELPER FUNCTIONS
     ============================================================================
     */

    /*
     Get parameter value from from URL.
     */
    this.getUrlVar = function (key) {
        var result = new RegExp(key + "=([^&]*)", "i").exec(window.location.search);
        return result && unescape(result[1]) || "";
    }

    /*
     Check if string starts with a specific character
     */
    this.startsWith = function (str, prefix) {

        return str.lastIndexOf(prefix, 0) === 0;

    }

    /*
     Check if string ends with a specific character
     */
    this.endsWith = function (str, suffix) {

        return str.indexOf(suffix, str.length - suffix.length) !== -1;
    }

    /*
     Parse Raw HTML
     */
    this.to_trusted = function (html_code) {
        return $sce.trustAsHtml(html_code);
    }

    /*
     Parse Raw HTML
     */
    this.scrollToTop = function () {
        $("html, body").animate({ scrollTop: 0 }, "slow");
    }


    /*
     ============================================================================
     NOTIFICATION MODULE
     ============================================================================
     */

    /*
     Array which will hold list of alert messages.
     */
    this.alerts = [];

    /*
     Method to add new alert notification.
     */
    this.addAlert = function () {
        $rootScope.alerts.push({msg: "Another alert!"});
    };

    /*
     Method to close alert notification.
     */
    this.closeAlert = function (index) {
        $rootScope.alerts.splice(index, 1);
    };


}]);