'use strict';

/**
 * @ngdoc function
 * @name faceverifyWebuiApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the faceverifyWebuiApp
 */
angular.module('faceverifyApp')
  .controller('MainCtrl', ['$rootScope', function ($rootScope) {
    $rootScope.active = 'home';
  }]);
