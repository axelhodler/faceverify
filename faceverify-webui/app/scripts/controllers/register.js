'use strict';

angular.module('faceverifyApp')
  .controller('RegisterCtrl', ['$rootScope', '$scope', '$http', '$log', 'ConfigService', function ($rootScope, $scope, $http, $log, ConfigService) {
    $rootScope.active = 'register';
    $scope.loading = true;

    $http.get(ConfigService.apihost + '/events').then(function (response) {
      $scope.loading = false;
      $scope.events = [];
      response.data.forEach(function (event) {
        console.log(event);
        $scope.events.push(event);
      });
    }, function (response) {
      $log.log(response);
      $scope.loading = false;
    });

    $scope.register = function(event) {
        $scope.saving = true;
        event.saving = true;
        $http.post(ConfigService.apihost + '/events/' + event.id + '/book')
          .then(function () {
            event.registered = true;
            $scope.saving = false;
            event.saving = false;
          }, function (response) {
            $log.log(response);
            $scope.saving = false;
            event.saving = false;
          });
    };

    $scope.calloff = function(event) {
        $scope.saving = true;
        event.saving = true;
        $http.post(ConfigService.apihost + '/events/' + event.id + '/cancel')
          .then(function () {
            event.registered = false;
            event.saving = false;
            $scope.saving = false;
          }, function (response) {
            $log.log(response);
            $scope.saving = false;
            event.saving = false;
          });
        };

  }]);
