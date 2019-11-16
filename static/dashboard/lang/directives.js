angular.module('langApp').directive('i18n', ['langFactory', function (langFactory) {

        var i18nDirective;
        i18nDirective = {
            restrict: "EA",
            updateText: function (ele, input, placeholder) {
                var result;
                result = void 0;
                if (input === 'i18n-placeholder') {
                    result = langFactory.getLocalizedString(placeholder);
                    return ele.attr('placeholder', result);
                } else if (input.length >= 1) {
                    result = langFactory.getLocalizedString(input);
                    return ele.text(result);
                }
            },
            link: function (scope, ele, attrs) {
                scope.$on('localizeResourcesUpdated', function () {
                    return i18nDirective.updateText(ele, attrs.i18n, attrs.placeholder);
                });
                return attrs.$observe('i18n', function (value) {
                    return i18nDirective.updateText(ele, value, attrs.placeholder);
                });
            }
        };
        return i18nDirective;
    }
]);