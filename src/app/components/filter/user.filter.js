(function () {
  'use strict';

  angular.module('jackblog.filter',[])
    .filter('userStatus',function(){
      return function(item){
        var statusName;
        switch(item){
          case 0:
            statusName = '未验证';
          break;
          case 1:
          statusName = '已验证';
          break;
          case 2:
          statusName = '被阻止';
          break;
          default:
          statusName = '未知状态';
        }
        return statusName;
      };
    })
    .filter('customTime',function(){
      var nowTime = new Date().getTime();
      var minuteTime = 60*1000;
      var hourTime = 60*minuteTime;
      var dayTime = 24*hourTime;
      var monthTime = dayTime * 30;
      var yearTime = monthTime * 12;
      return function(item){
        var publishTime = new Date(item).getTime();
        var historyTime = parseInt(nowTime) - parseInt(publishTime);
        var descTime;
        if(historyTime >= yearTime){
          //按年算
          descTime = parseInt(historyTime/yearTime) + '年前';
        }else if(historyTime< yearTime && historyTime >= monthTime){
          //按月算
          descTime = parseInt(historyTime/monthTime) + '月前';
        }else if(historyTime< monthTime && historyTime>= dayTime){
          //按天算
          descTime = parseInt(historyTime/dayTime) + '天前';
        }else if(historyTime< dayTime && historyTime>= hourTime){
          //按小时算
          descTime = parseInt(historyTime/hourTime) + '小时前';
        }else if(historyTime< hourTime && historyTime>= minuteTime){
          //按分钟算
          descTime = parseInt(historyTime/minuteTime) + '分钟前';
        }else{
          descTime = '刚刚';
        }
        return descTime;
      };
    });
})();

