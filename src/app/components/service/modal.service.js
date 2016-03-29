(function () {
    'use strict';

    angular.module('gzblog.service')
        .factory('CustomModalService', function ($modal) {
          return {
            open: function (ctrlName,url,size) {
                $modal.open({
                    templateUrl: url,
                    controller: ctrlName,
                    size: size
                });
            }
          };
        });
})();
