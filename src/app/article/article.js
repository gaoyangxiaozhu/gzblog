(function () {
	'use strict';

	angular.module('gzblog.article',[])
	  .config(function ($stateProvider) {
	    $stateProvider
	      .state('article', {
	        url: '/article/:aid',
	        templateUrl: 'app/article/article.html',
	        controller: 'ArticleCtrl'
	      });
	  });
})();
