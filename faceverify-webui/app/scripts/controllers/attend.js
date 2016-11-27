'use strict';

angular.module('faceverifyApp')
  .controller('AttendCtrl', ['$rootScope', '$scope', '$http', '$routeParams', '$log', 'ConfigService', function ($rootScope, $scope, $http, $routeParams, $log, ConfigService) {
    $rootScope.active = 'attend';
    $scope.eventid = $routeParams.eventid;
    $scope.loading = true;

    $http.get(ConfigService.apihost + '/events/' + $scope.eventid)
        .then(function (response) {
          $log.log(response.data);
          $scope.event = response.data;
          $scope.loading = false;
        }, function (response) {
          $log.log(response);
          $scope.loading = false;
        });

    $scope.vm = {};
    $scope.vm.config = {
      shots: 1,
      flashFallbackUrl: 'vendors/webcamjs/webcam.swf',
      flashNotDetectedText: 'Your browser has no flash plugin installed!'
    };

    $scope.vm.captureButtonEnable = false;

    $scope.vm.onCaptureComplete = function(src) {
      $scope.picture = src[0].replace(/^data:image\/[a-z]+;base64,/, '');
      $log.log($scope.picture);
      $scope.vm.off();
      $scope.verifying = true;
      var verifyData = {
        image: $scope.picture
      };

      $http.post(ConfigService.apihost + '/events/' + $scope.eventid + '/verify', verifyData)
          .then(function (response) {
            if (response.data === 'true') {
              $scope.verifystatus = 'verified';
            } else {
              $scope.verifystatus = 'failed';
            }
            $scope.verifying = false;
          }, function (response) {
            $log.log(response);
            $scope.verifystatus = 'failed';
            $scope.verifying = false;
          });
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
