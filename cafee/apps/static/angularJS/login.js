var SecondController = angular.module('SecondController',['ngCookies','ngResource','ngRoute','ngSanitize']);

SecondController.config(function($interpolateProvider,$routeProvider,$locationProvider) {
	
	$interpolateProvider.startSymbol('({');
	$interpolateProvider.endSymbol('})');
});

SecondController.run(function($rootScope,$log,$http,$cookies){
	$http.defaults.headers.common['X_CSRFToken'] = $cookies['csrktoken'];
});

SecondController.controller('LoginController',function LoginController($scope,$log,$http,$routeParams,$location){
	$scope.message = [];
	$scope.message[0] = '';
	$scope.message[1] = '';
	$scope.mess = '';
	$scope.CRAccount = {};
	$scope.Account = [];
	$scope.messageLogin = '';
	$scope.LoadAccount = function(){
		$http.get('/Acc/').success(function(data){
			$scope.Account = data;
			console.log(data)
		}).error(function(data){
			console.log(data)
		});
	};
	$scope.TestUser = function()
	{
		for (var i = 0; i < $scope.Account.length; i++) {
		   if ($scope.CRAccount.username == $scope.Account[i].username) {
		   		$scope.message[0]='Username is valid';

		   }else
		   {
		   		$scope.message[0] = '';
		   		console.log($scope.message.length)
		   		return;
		   }
		};
   
	};
	$scope.TestPassCon = function(){

    	if ($scope.passcon != $scope.CRAccount.password) {
    		$scope.message[1] = 'Password confing is not same password';
   		}else
   		{	
   			$scope.message[1] = '';
   			console.log($scope.message.length)
    		return;    				
    	}
	};
	$scope.CreateAccount = function(){
		console.log($scope.message[0])
		console.log($scope.message[1])
		if ($scope.message[0] != '' || $scope.message[1] != '' ) {
			$scope.mess = 'Can not create account, Please check your form';
		}else{
			$http.post('/Acc/',$scope.CRAccount).success(function(data){
				$scope.LoadAccount();
				alert('Create new account success');
				$('#close').click();

			}).error(function(data){
				console.log(data)
			})
		}
	};
	$scope.LoginAccount = function(){
		
		for (var i = 0; i < $scope.Account.length; i++) {
			if($scope.username == $scope.Account[i].username )
			{

				if ($scope.password == $scope.Account[i].password) {
					
					window.location.href = 'http://localhost:8000/#/Home/';
					
				}else{
					$scope.messageLogin = 'Password is wrong'
				};
			}else{
				$scope.messageLogin = 'Username is not valid'
			};
		};
	};
	$scope.LoadAccount();
});