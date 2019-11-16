angular.module('langApp').factory('langFactory', ['$http', '$rootScope', '$window', function ($http, $rootScope, $window) {

    var localize;

    localize = {

        language: '',

        url: void 0,

        resourceFileLoaded: false,

        successCallback: function (data) {
            localize.dictionary = data;
            localize.resourceFileLoaded = true;
            return $rootScope.$broadcast('localizeResourcesUpdated');
        },

        setLanguage: function (value) {
            localize.language = value.toLowerCase().split("-")[0];
            return localize.initLocalizedResources();
        },

        setUrl: function (value) {
            localize.url = value;
            return localize.initLocalizedResources();
        },

        buildUrl: function () {
            if (!localize.language) {
                localize.language = ($window.navigator.userLanguage || $window.navigator.language).toLowerCase();
                localize.language = localize.language.split("-")[0];
            }
            return '/static/dashboard/common/i18n/resources-locale_' + localize.language + '.js';
        },

        initLocalizedResources: function () {
            var url;
            url = localize.url || localize.buildUrl();
            return $http({
                method: "GET",
                url: url,
                cache: false
            }).success(localize.successCallback).error(function () {
                return $rootScope.$broadcast('localizeResourcesUpdated');
            });
        },

        getLocalizedString: function (value) {
            var result, valueLowerCase;
            result = void 0;
            if (localize.dictionary && value) {
                valueLowerCase = value.toLowerCase();
                if (localize.dictionary[valueLowerCase] === '') {
                    result = value;
                } else {
                    result = localize.dictionary[valueLowerCase];
                }
            } else {
                result = value;
            }
            return result;
        }
    };

    return localize;
}
]);