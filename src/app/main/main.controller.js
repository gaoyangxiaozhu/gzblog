(function () {
   'use strict';

   angular.module('gzblog')
     .controller('MainCtrl', function ($scope,Blog,$log,Tags) {
        //获取标签列表
        Tags.getFrontTagList().then(function (result) {
            $scope.tagList = result.data;
        });
        //初始数据
        $scope.options = {
            currentPage:1,              //当前页数
            itemsPerPage:5,            //每页显示的条数
            sortName:'publish_time',    //排序项
            tagId: ''
        };
         //取出存在localStorage中的选项
         if(localStorage.options){
             var initOption = JSON.parse(localStorage.options);
             $scope.options.sortName = initOption.sortName;
             $scope.options.tagId = initOption.tagId;
         }
        $scope.blogList = [];
        function doPaging(options,isReset) {
             $scope.isLoading = true;

             //数量需要过滤
             Blog.getFrontBlogCount(options).then(function(result){
                $scope.blogCount = result.count;
                $scope.numPages = Math.ceil($scope.blogCount/$scope.options.itemsPerPage);
             });
            //获取列表
            Blog.getFrontBlogList(options).then(function(result){
                $scope.isLoading = false;
                if(isReset){
                    $scope.blogList = result.data;
                }else{
                    $scope.blogList = $scope.blogList.concat(result.data);
                }
            }).catch(function(){
               $scope.isLoading = false;
                $scope.blogList = [];
            });
        }
        //初始化列表
        doPaging($scope.options, true);
        //加载更多
        $scope.loadMore = function(page){
            $scope.options.currentPage = page;

            doPaging($scope.options, true);
        };
     });
})();
