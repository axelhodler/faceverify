'use strict';

angular.module('faceverifyApp')
  .controller('MainCtrl', ['$rootScope', function ($rootScope) {
    $rootScope.active = 'home';
  }]);
