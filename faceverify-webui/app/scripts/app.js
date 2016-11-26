'use strict';

/**
 * @ngdoc overview
 * @name faceverifyWebuiApp
 * @description
 * # faceverifyWebuiApp
 *
 * Main module of the application.
 */
angular
  .module('faceverifyApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch',
    'ng-webcam'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl',
        controllerAs: 'main'
      })
      .when('/signup', {
        templateUrl: 'views/signup.html',
        controller: 'SignupCtrl'
      })
      .when('/register', {
          templateUrl: 'views/register.html',
          controller: 'RegisterCtrl'
        })
    .when('/attend', {
              templateUrl: 'views/attend.html',
              controller: 'AttendCtrl'
            })
      .otherwise({
        redirectTo: '/'
      });
  });
