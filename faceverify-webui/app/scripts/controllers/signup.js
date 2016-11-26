'use strict';

angular.module('faceverifyApp')
  .controller('SignupCtrl', ['$rootScope', '$scope', '$log', '$http', 'ConfigService', function ($rootScope, $scope, $log, $http, ConfigService) {
    $rootScope.active = 'signup';
    $scope.mode = 'currentpicture';

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
      $log.log('webcamController.onCaptureComplete : ', src);
      $scope.picture = src[0];
      $scope.vm.off();
      $scope.mode = 'currentpicture';
    };

    $scope.vm.onError = function(err) {
      $log.error('webcamController.onError : ', err);
      $scope.vm.showButtons = false;
    };

    $scope.vm.onLoad = function() {
      $log.info('webcamController.onLoad');
    };

    $scope.vm.onLive = function() {
      $log.info('webcamController.onLive');
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

    $scope.takeNewPicture = function () {
        $scope.vm.on();
        $scope.mode = 'newpicture';
    };

    $scope.cancelNewPicture = function () {
        $scope.vm.off();
        $scope.mode = 'currentpicture';
    };

    $scope.signUp = function () {
      $scope.saving = true;
      var postData = {
        image: $scope.picture.replace(/^data:image\/[a-z]+;base64,/, '')
      };

      $http.post(ConfigService.apihost + '/users', postData)
        .then(function () {
          $scope.signupstatus = 'success';
          $scope.saving = false;
        }, function (response) {
          $log.log(response);
          $scope.saving = false;
        });
    };

  }]);
