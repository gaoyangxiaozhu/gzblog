(function () {
   'use strict';

   angular.module('gzblog.directives')
       .directive('slideMenu',function ($window) {
           return {
               restrict:'EA',
               link:function (scope, element, attrs) {
                   var that = element;
                   that.after($('<div class="slider-box"></div>'));

                   scope.$watch(scope.isLoggedIn, function(){
                     var mainLinks = that.find('.navbar-item');
                     var slideBox = that.siblings('.slider-box');
                     var width = that.find('li:first').width();

                     mainLinks.each(function(){
                        var _ = $(this);
                        var parent = _.parents('li');
                        var left = parent.position().left +width+'px';
                        _.click(function(){
                          if(!_.hasClass('active')){
                            mainLinks.removeClass('active');
                            _.addClass('active');
                          }
                           slideBox.css({'left': left});
                        });
                     });

                   });
               },
           };
       });
})();
