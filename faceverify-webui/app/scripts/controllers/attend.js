'use strict';

/**
 * @ngdoc function
 * @name faceverifyWebuiApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the faceverifyWebuiApp
 */
angular.module('faceverifyApp')
  .controller('AttendCtrl', ['$rootScope', '$scope', function ($rootScope, $scope) {
    $rootScope.active = 'attend';

    $scope.vm = {};
    $scope.vm.config = {
      delay: 2,
      shots: 1,
      countdown: 3,
      flashFallbackUrl: 'vendors/webcamjs/webcam.swf',
      flashNotDetectedText: 'Your browser has no flash plugin installed!'
    };

    $scope.vm.captureButtonEnable = false;

    $scope.vm.onCaptureComplete = function(src) {
      $scope.picture = src[0];
      $scope.vm.off();
      // TODO add verification call here
      $scope.verifystatus = 'verified';
    };

    $scope.vm.onError = function() {
      $scope.vm.showButtons = false;
    };

    $scope.vm.onLive = function() {
      $scope.vm.captureButtonEnable = true;
    };

    $scope.vm.capture = function() {
      $scope.$broadcast('ngWebcam_capture');
    };

    $scope.vm.on = function() {
      $scope.$broadcast('ngWebcam_on');
    };

    $scope.vm.off = function() {
      $scope.$broadcast('ngWebcam_off');
      $scope.vm.captureButtonEnable = false;
    };

    $scope.startAgain = function () {
        $scope.vm.on();
        delete $scope.verifystatus;
    };

  }]);
