angular.module('langApp').controller('langController', ['$scope', 'langFactory', function ($scope, langFactory) {

    $scope.lang = 'English';

    $scope.setLang = function (lang) {

        switch (lang) {
            case 'English':
                langFactory.setLanguage('EN-US');
                break;
            case 'Español':
                langFactory.setLanguage('ES-ES');
                break;
            case '日本語':
                langFactory.setLanguage('JA-JP');
                break;
            case '中文':
                langFactory.setLanguage('ZH-TW');
                break;
            case 'Deutsch':
                langFactory.setLanguage('DE-DE');
                break;
            case 'français':
                langFactory.setLanguage('FR-FR');
                break;
            case 'Italiano':
                langFactory.setLanguage('IT-IT');
                break;
            case 'Portugal':
                langFactory.setLanguage('PT-BR');
                break;
            case 'Русский язык':
                langFactory.setLanguage('RU-RU');
                break;
            case '한국어':
                langFactory.setLanguage('KO-KR');
        }
        return $scope.lang = lang;
    };

    return $scope.getFlag = function () {
        var lang;
        lang = $scope.lang;
        switch (lang) {
            case 'English':
                return 'flags-american';
            case 'Español':
                return 'flags-spain';
            case '日本語':
                return 'flags-japan';
            case '中文':
                return 'flags-china';
            case 'Deutsch':
                return 'flags-germany';
            case 'français':
                return 'flags-france';
            case 'Italiano':
                return 'flags-italy';
            case 'Portugal':
                return 'flags-portugal';
            case 'Русский язык':
                return 'flags-russia';
            case '한국어':
                return 'flags-korea';
        }
    };
}
]);