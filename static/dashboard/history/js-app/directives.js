angular.module("tests").directive('collapseNavMenu', [
    function() {
      return {
        restrict: 'A',
        link: function(scope, ele, attrs) {
          var $a, $aRest, $lists, $listsRest, app;
          $lists = ele.find('ul').parent('li');
          $lists.append('<i class="fa fa-caret-right icon-has-ul"></i>');
          $a = $lists.children('a');
          $listsRest = ele.children('li').not($lists);
          $aRest = $listsRest.children('a');
          app = $('#app');
          $a.on('click', function(event) {
            var $parent, $this;            
            $this = $(this);
            $parent = $this.parent('li');
            $lists.not($parent).removeClass('open').find('ul').slideUp();
            $parent.toggleClass('open').find('ul').slideToggle();
            return event.preventDefault();
          });
          $aRest.on('click', function(event) {
            return $lists.removeClass('open').find('ul').slideUp();
          });          
        }
      };
    }
 ]);/*.directive('dynamic', function ($compile) {
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
    }).directive('ngHtmlCompile', function($compile) {
        return {
            restrict: 'A',
            link: function(scope, element, attrs) {
                scope.$watch(attrs.ngHtmlCompile, function(newValue, oldValue) {
                    element.html(newValue);
                    $compile(element.contents())(scope);
                });
            }
        }
    });*/