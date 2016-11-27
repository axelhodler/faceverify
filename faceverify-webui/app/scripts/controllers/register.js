'use strict';

angular.module('faceverifyApp')
  .controller('RegisterCtrl', ['$rootScope', '$scope', '$http', '$log', '$timeout', 'ConfigService', function ($rootScope, $scope, $http, $log, $timeout, ConfigService) {
    $rootScope.active = 'register';
    $scope.loading = true;

    $http.get(ConfigService.apihost + '/events').then(function (response) {
      $scope.loading = false;
      $scope.events = [];
      response.data.forEach(function (event) {
        $scope.events.push(event);
      });
      $timeout(function () {
        Array.prototype.forEach.call(document.getElementsByClassName('satoshi'), function (element, index) {
          var satoshiElement = angular.copy(document.getElementById('satoshipay' + index));
          if (!$scope.events[index].registered) {
            element.appendChild(satoshiElement);
            $scope.events[index].satoshi = satoshiElement;
          }
        });
      }, 0);
    }, function (response) {
      $log.log(response);
      $scope.loading = false;
    });

    $scope.register = function(event) {
        $scope.registering = event;
    };

    $scope.confirmRegistration = function() {
        $scope.saving = true;
        var userData = {
          username: $scope.username,
          password: $scope.password
        };
        $http.post(ConfigService.apihost + '/events/' + $scope.registering.id + '/book', userData)
          .then(function () {
            event.registered = true;
            $scope.saving = false;
            angular.element('#postbank').modal('hide');
          }, function (response) {
            $log.log(response);
            $scope.saving = false;
          });
    };

    $scope.registerSatoshi = function(event, index) {
      $log.log('register with satoshi!');
      angular.element(document.getElementById('satoshipay' + index)).triggerHandler('click');
      event.satoshi.remove();
      event.registered = true;
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
