'use strict';

/**
 * @ngdoc function
 * @name faceverifyWebuiApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the faceverifyWebuiApp
 */
angular.module('faceverifyApp')
  .controller('RegisterCtrl', ['$rootScope', '$scope', function ($rootScope, $scope) {
    $rootScope.active = 'register';

    $scope.events = [
        {
            name: 'Startup Founders Get Together',
            location: 'Coworking 0711',
            date: '2016-12-13',
            start: '18:30',
            end: '21:00',
            deposit: 10.00
        },
        {
            name: '7th Stuttgart Ethereum, blockchain technology, decentralized computing meetup',
            location: 'bwcon: Geschäftsstelle, 5.Stock, Besprechungsraum',
            date: '2016-12-20',
            start: '19:00',
            end: '21:00',
            deposit: 5.00
        }
    ];

    $scope.register = function(event) {
        event.registered = true;
    };

    $scope.calloff = function(event) {
            event.registered = false;
        };

  }]);
