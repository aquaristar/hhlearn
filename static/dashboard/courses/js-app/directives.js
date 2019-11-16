angular.module("course").directive('dynamic', function ($compile) {
    return {
        restrict: 'A',
        replace: true,
        scope: { dynamic: '=dynamic'},
        link: function (scope, ele, attrs) {
            scope.$watch(attrs.dynamic, function(pageHTML) {
                ele.html(pageHTML);
                $compile(ele.contents())(scope);
            });
        }
    };
}).directive('ngSparkline', function() {
    return {
        restrict: 'A',
        replace: true,
        template: '<div class="sparkline">wewrwerwerwe</div>',
        link: function (scope, ele, attrs) {
            scope.$watch(attrs.dynamic, function(pageHTML) {
                ele.html(pageHTML);
                $compile(ele.contents())(scope);
            });
        }
    }
}).directive('uiRangeSlider', [
    function() {
      return {
        restrict: 'A',
        link: function(scope, ele, attrs) {
            ele.slider(scope);
            ele.slider('setValue',scope.$parent.fontSize);
            ele.slider().on('slideStop', function(ev){
                scope.$parent.changeDemoFontSize();
            });
        }
      };
}]).directive('ngHtmlCompile', function($compile) {
    return {
        restrict: 'A',
        link: function(scope, element, attrs) {
            scope.$watch(attrs.ngHtmlCompile, function(newValue, oldValue) {
                element.html(newValue);
                $compile(element.contents())(scope);
            });
        }
    }
});
    