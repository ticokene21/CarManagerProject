var FirstController = angular.module('FirstController',['ngCookies','ngResource','ngRoute','ngSanitize']);

FirstController.config(function($interpolateProvider,$routeProvider,$locationProvider) {
	// body...
	$routeProvider.when('/CR_purchase/',
	{
		controller: 'PurchaseController',
		templateUrl: '/CR_purchase'
	}).when('/Home/',
	{
		controller: 'HomeController',
		templateUrl: '/Home'
	}).when('/Struct/',
	{
		controller: 'BomController',
		templateUrl: '/Struct'
	}).when('/ManuOrder/',
	{
		controller: 'ManufacturingController',
		templateUrl: '/ManuOrder'
	}).when('/WareHouse/',
	{
		controller: 'WareHouseController',
		templateUrl: '/WareHouse'
	}).when('/SaleOrder/',
	{	
		controller: 'SaleOrderController',
		templateUrl: '/SaleOrder'
	}).when('/Receipt/',
	{
		controller: 'ReceiptController',
		templateUrl: '/Receipt'
	}).when('/CustomerManager/',
	{
		controller: 'CustomerController',
		templateUrl: '/CustomerManager'
	}).when('/Report/',
	{
		controller: 'ReportController',
		templateUrl: '/Report'
	}).when('/OrderList/',
	{
		controller: 'OrderListController',
		templateUrl: '/OrderList'
	}).otherwise({
		redirectTo: '/Home/'
	});
	$interpolateProvider.startSymbol('{$');
	$interpolateProvider.endSymbol('$}');
});

FirstController.run(function($rootScope,$log,$http,$cookies){
	$http.defaults.headers.common['X_CSRFToken'] = $cookies['csrktoken'];
});

FirstController.filter('range', function() {
  return function(input, min, max) {
    min = parseInt(min); //Make string input int
    max = parseInt(max);
    for (var i=min; i<max; i++)
      input.push(i);
    return input;
  };
});

FirstController.controller('PurchaseController',function PurchaseController($scope,$log,$http,$routeParams,$location){

	$scope.CRMaterial = {};
	$scope.listsup = [];
	$scope.pur_det_mat_list = [];
	$scope.CRPurhaseDet = {}; 
	$scope.pur_det_list = [];
	$scope.CRPurhase = {};
	var SumPricePur = 0;
	var tempindex = 0;
	$scope.PurchaseSupplier = 0;	

	$scope.CreateMaterial = function(){
		$scope.CRMaterial.materialQuantity = 0
		console.log($scope.CRMaterial)

		$http.post('/Material/',$scope.CRMaterial).success(function(data){
			console.log(data)
			$scope.CRMaterial = {};
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.LoadSupplier = function(){
		$http.get('/Supplier/').success(function(data){
			$scope.listsup = data;
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.Supplierchange = function(){
		$scope.CRPurhase.PurchaseSupplier = $scope.SP_current.supplierID;
	
	};

	$scope.LoadMaterial = function(){
		$http.get('/Material/').success(function(data){
			$scope.pur_det_mat_list = data;
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.Pur_det_matchange = function(){
		$scope.CRPurhaseDet.PurchaseDetMaterial = $scope.pur_det_mat_current.materialID;
		console.log($scope.CRPurhaseDet.PurchaseDetMaterial)
	};

	$scope.AddPurchaseDetList = function(index){
		$http.get('/Material/'+$scope.CRPurhaseDet.PurchaseDetMaterial+'/').success(function(data){
			var r
			for (var i = 0; i < $scope.pur_det_mat_list.length; i++) {
				if($scope.pur_det_mat_list[i].materialID == index)
				{
					r = i;
					break;
				}
			};
			console.log(data)
			var x = data.materialPrice;
			var y = $scope.CRPurhaseDet.PurchaseDetQuantity;
			SumPricePur = x * y;
			console.log(SumPricePur)
			$scope.CRPurhaseDet.purchaseDetPrice = data.materialPrice;
			$scope.CRPurhaseDet.materialName = data.materialName;
			$scope.pur_det_list.push($scope.CRPurhaseDet);
			tempindex = index;
			$scope.pur_det_mat_list.splice(r,1);
			$scope.CRPurhaseDet = {};
			console.log($scope.pur_det_list)			
		});
	};

	$scope.deleteitem = function(index){
		console.log(index)
		$scope.pur_det_list.splice(index,1);
		console.log($scope.pur_det_list)
	};

	$scope.CreatePurchase = function(){

		var d = {
			purchaseDate : $scope.CRPurhase.PurchaseDate,
			purchaseName: $scope.CRPurhase.PurchaseName,
			purchaseSum : SumPricePur,
			purchaseState: 1,
			purchaseSupplier: $scope.CRPurhase.PurchaseSupplier,
		};
		console.log(d)

		$http.post('/Purchase/',d).success(function(data){
			$scope.CRPurhase = data;
			console.log(data)
			for(var i =0 ; i < $scope.pur_det_list.length; i++)
			{
				var d1 = {
					purchaseDetMaterial: $scope.pur_det_list[i].PurchaseDetMaterial,
					purchaseDetQuantity: $scope.pur_det_list[i].PurchaseDetQuantity,
					purchaseDetPur: data.purchaseID,
				};
				console.log(d1)
				$http.post('/PurchaseDet/',d1).success(function(d1){
					console.log(d1)
					
					$http.get('/Material/'+d1.purchaseDetMaterial+'/').success(function(d2){
						console.log(d2)

						var d3 = {
							materialName: d2.materialName,
							materialQuantity: d2.materialQuantity + d1.purchaseDetQuantity,
							materialPrice: d2.materialPrice,
						};
						$http.put('/Material/'+d2.materialID+'/',d3).success(function(d3){
							console.log(d3)
							$scope.CRPurhase = {};
							$scope.pur_det_list = [];
							
						}).error(function(d3){
							console.log(d3)
						});
					}).error(function(d2){
						console.log(d2)
					});
				}).error(function(d1){
					console.log(d1)
				});
			}
			alert('Success');
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.LoadMaterial();
	$scope.LoadSupplier();
});

FirstController.controller('HomeController',function HomeController($scope,$log,$http,$routeParams,$location){

});

FirstController.controller('BomController', function BomController($scope,$log,$http,$routeParams,$location){
	$scope.bom_pro_list = [];
	$scope.bom_mat_list = [];
	$scope.bom_det_list = [];
	$scope.CRBom = {};
	$scope.CRBomDet = {};
	$scope.CRMaterial = {};


	$scope.CreateMaterial = function(){
		$scope.CRMaterial.materialQuantity = 0
		console.log($scope.CRMaterial)

		$http.post('/Material/',$scope.CRMaterial).success(function(data){
			console.log(data)
			$scope.CRMaterial = {};
			$scope.loadmaterial();
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.loadproduct = function(){
		$http.get('/Product/').success(function(data){
			$scope.bom_pro_list = data; 
			console.log($scope.bom_pro_list)
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.loadmaterial = function(){
		$http.get('/Material/').success(function(data){
			$scope.bom_mat_list = data;
			console.log($scope.bom_mat_list)
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.productchange = function()
	{
		$scope.CRBom.bomProduct = $scope.bom.productID;
	};

	$scope.Bom_det_matchange = function()
	{
		$scope.CRBomDet.bomDetMaterial = $scope.bom_det_mat_current.materialID;
		$scope.CRBomDet.materialName = $scope.bom_det_mat_current.materialName;
	};

	$scope.AddBomDetList = function(index)
	{
		console.log($scope.bom_mat_list)
		var x = 0;
		console.log(index)
		for(var i = 0;i < $scope.bom_mat_list.length;i++)
		{
			if($scope.bom_mat_list[i].materialID == index)
			{
				var x = i;
				break;
			}
		}

		console.log(x)

		$scope.bom_det_list.push($scope.CRBomDet);
		console.log($scope.bom_det_list)
		$scope.bom_mat_list.splice(x, 1);
		$scope.CRBomDet = {}
	};

	$scope.CreateBom = function()
	{
		$http.post('/Bom/',$scope.CRBom).success(function(data){
			console.log(data)
			for (var i = 0; i < $scope.bom_det_list.length; i++) {
				var d = {
							bomDetMaterial: $scope.bom_det_list[i].bomDetMaterial,
							bomDetQuantity: $scope.bom_det_list[i].BomDetQuantity,
							bomDetBom: data.bomID,
						};
				$http.post('/BomDet/',d).success(function(d1){
					console.log(d1)
					$scope.CRBom = {};
					$scope.bom_mat_list = [];
					$scope.bom_det_list = [];
					$scope.bom = {};
					
				}).error(function(d){
					console.log(d)
				});
			};
		}).error(function(data){
			console.log(data)
		});
		alert('Success');
	};

	$scope.loadmaterial();
	$scope.loadproduct();
});

FirstController.controller('ManufacturingController',function ManufacturingController($scope,$log,$http,$routeParams,$filter){

	$scope.man_bom_list = [];
	$scope.CRManufacturing = {};
	$scope.man_list = [];
	$scope.bom_det = [];
	$scope.mandetail = {};
	$scope.getmanuid = {};

	$scope.LoadBom = function(){
		$http.get('/Bom/').success(function(data){
			$scope.man_bom_list = data;
			console.log(data)
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.ManBomChange = function(){
		$scope.CRManufacturing.manufacturingBom = $scope.man_bom_current.bomID;
	};

	$scope.CreateManufacturing = function(){
		$scope.CRManufacturing.manufacturingState = 1;
		$http.post('/Manufacturing/',$scope.CRManufacturing).success(function(data){
			console.log(data)
			$scope.CRManufacturing = {};
			$scope.LoadManufacturing();
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.GetManuID = function(id){
		$scope.getmanuid = id;
	};

	$scope.UpdateManufacturing = function(){
		$scope.CRManufacturing.manufacturingState = 1;
		$http.put('/Manufacturing/'+$scope.getmanuid+'/',$scope.CRManufacturing).success(function(data){
			console.log(data)
			$scope.CRManufacturing = {};
			$scope.LoadManufacturing();
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.DeleteManu = function(id){
		$http.delete('/Manufacturing/'+id+'/').success(function(data){
			console.log(data)
			$scope.LoadManufacturing();
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.LoadManufacturing = function(){
		$http.get('/ManufacturingTemp/').success(function(data){
			$scope.man_list = data;
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.viewitem = function(item){

		$scope.disabledProduce = true;
		$scope.disabledFinished = true;
		$scope.buttonProduceStyle = {
			opacity: '0.5',
			cursor: 'not-allowed'
		};
		$scope.buttonFinishedStyle = {
			opacity: '0.5',
			cursor: 'not-allowed',
		};
		
		$http.get('/Manufacturing/'+item.manufacturingID+'/').success(function(d1){
			console.log(d1)
			
			
			$http.get('/BomDetTemp/'+item.manufacturingBom.bomID+'/Bom').success(function(data){
				console.log(data)
				$scope.bom_det = data;
				$scope.mandetail = item;
				var test = false;
				var x = d1.manufacturingQuantity;
				for (var i = 0; i < data.length; i++) {
					var y = data[i].bomDetQuantity;
					$scope.bom_det[i].manu_mat = x*y;
					if($scope.bom_det[i].bomDetMaterial.materialQuantity < $scope.bom_det[i].manu_mat)
					{
						test = true;
					}
				}
				//if(d1.manufacturingState == 1)
				//{	
				if(d1.manufacturingState == 1)	
				{			
					if(test == false)
					{
						d1.manufacturingState = 2;
						$http.put('/Manufacturing/'+d1.manufacturingID+'/',d1).success(function(d2){
							console.log(d2)
							$scope.LoadManufacturing();
						}).error(function(d2){
							console.log(d2)
						});	
					}else{
						$scope.disabledProduce = true;
						$scope.disabledFinished = true;
						$scope.buttonProduceStyle = {
							opacity: '0.5',
							cursor: 'not-allowed'
						};
						$scope.buttonFinishedStyle = {
							opacity: '0.5',
							cursor: 'not-allowed',
						};	
						d1.manufacturingState = 1;
						$http.put('/Manufacturing/'+d1.manufacturingID+'/',d1).success(function(d2){
							console.log(d2)
							$scope.LoadManufacturing();
						}).error(function(d2){
							console.log(d2)
						});	
					}
				}
				//}
				if(d1.manufacturingState == 2)
				{
					$scope.buttonProduceStyle = {};
					$scope.disabledProduce = false;
					
				}
				else if(d1.manufacturingState == 3)
				{
					$scope.disabledFinished = false;
					$scope.buttonFinishedStyle ={};	
					$scope.buttonProduceStyle = {
						opacity: '0.5',
						cursor: 'not-allowed'
					};
					$scope.disabledProduce = true;
				}else if(d1.manufacturingState == 4){
					console.log('aaa')
					$scope.disabledProduce = true;
					$scope.disabledFinished = true;
					$scope.buttonProduceStyle = {
						opacity: '0.5',
						cursor: 'not-allowed'
					};
					$scope.buttonFinishedStyle = {
						opacity: '0.5',
						cursor: 'not-allowed',
					};
				}
			}).error(function(data){
				console.log(data)
			});
		}).error(function(d1){
			console.log(d1)
		});


	};
	
	$scope.Produce = function(divName,item){
		
		$http.get('/Manufacturing/'+item.manufacturingID+'/').success(function(data){
			data.manufacturingState = 3
			$http.put('/Manufacturing/'+data.manufacturingID+'/',data).success(function(d1){
				console.log(d1)
				$scope.LoadManufacturing();
				$scope.disabledFinished = false;
				$scope.buttonFinishedStyle ={};	
				$scope.buttonProduceStyle = {
					opacity: '0.5',
					cursor: 'not-allowed'
				};
				$scope.disabledProduce = true;
				var printContents = document.getElementById(divName).innerHTML;
		  		var popupWin = window.open('', '_blank', 'width=700,height=900');
		  		popupWin.document.open()
		  		popupWin.document.write('<html><head></head><body onload="window.print()"><h2>Manufacturing Order</h2>' + printContents + '</html>');
		 		popupWin.document.close();
			}).error(function(d1){
				console.log(d1)
			});
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.Finished = function(item,item2){
		console.log(item2)
		
		var d = {
			productName: item.manufacturingBom.bomProduct.productName,
			productQuantity: item.manufacturingBom.bomProduct.productQuantity + item.manufacturingQuantity,
		};
	
		$http.put('/Product/'+item.manufacturingBom.bomProduct.productID+'/',d).success(function(data){
			var month = $filter('date')(item.manufacturingDate,'MM');
			var year = $filter('date')(item.manufacturingDate,'yyyy');
			var MY = month+'v'+year;
			for (var i = 0; i < item2.length; i++) {
				var b = item2[i].bomDetMaterial.materialQuantity;
				var n = item2[i].bomDetBom.bomQuantity;
				var m = b - item2[i].manu_mat;
				console.log(m)
				var d = {
					materialName: item2[i].bomDetMaterial.materialName,
					materialQuantity: m,
					materialPrice: item2[i].bomDetMaterial.materialPrice,
				};
				console.log(d)
				$http.put('/Material/'+item2[i].bomDetMaterial.materialID+'/',d).success(function(d1){
					console.log(d1)

				}).error(function(d1){
					console.log(d1)
				});
				
			};
			$http.get('InventoryDate/'+MY+'/'+data.productID).success(function(d4){
				console.log(d4)
					if(d4.length == 0)
					{
						d5 = {
							inventoryMonthYear : MY,
							inventoryProduct: data.productID,
							inventoryInput: data.productQuantity,
							inventoryOutput: 0,
							inventoryRemain:0,
							inventoryPop:data.productQuantity,
						};
						$http.post('/Inventory/',d5).success(function(d6){
							console.log(d6)
						}).error(function(d6){
							console.log(d6)
						});
					}else{
						d4[0].inventoryRemain = d4[0].inventoryRemain + item.manufacturingQuantity;
						d4[0].inventoryPop = d4[0].inventoryInput + (d4[0].inventoryRemain - d4[0].inventoryOutput);
						$http.put('/Inventory/'+d4[0].inventoryID+'/',d4[0]).success(function(d7){
							console.log(d7)
						}).error(function(d7){
							console.log(d7)
						});
					}
				}).error(function(d4){
					console.log(d4)
				});
			$http.get('/Manufacturing/'+item.manufacturingID+'/').success(function(d2){
				d2.manufacturingState = 4;
				$http.put('/Manufacturing/'+d2.manufacturingID+'/',d2).success(function(d3){
					console.log(d3)
					$scope.disabledProduce = true;
					$scope.disabledFinished = true;
					$scope.buttonProduceStyle = {
						opacity: '0.5',
						cursor: 'not-allowed'
					};
					$scope.buttonFinishedStyle = {
						opacity: '0.5',
						cursor: 'not-allowed',
					};
				}).error(function(d3){
					console.log(d3)
				});
			}).error(function(d2){
				console.log(d2)
			});

			
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.CheckProduce = function(item){
		if(item.manufacturingState.stateID == 3 && itemitem.manufacturingState.stateID)
		{
			$scope.message = 'Manufacturing Order were executed or finished';
		}else{

		}
	};

	$scope.LoadManufacturing();
	$scope.LoadBom();
});

FirstController.controller('WareHouseController', function WareHouseController($scope,$http){
	$scope.productlist = [];
	$scope.materiallist = [];
	$scope.CRProduct = {};
	$scope.CRMaterial = {};

	$scope.LoadMaterial = function(){
		$http.get('/Material/').success(function(data){
			$scope.materiallist = data;
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.LoadProduct = function(){
		$http.get('/Product/').success(function(data){
			console.log(data)
			$scope.productlist = data;
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.CreateMaterial = function(){
		$http.post('/Material/',$scope.CRMaterial).success(function(data){
			$scope.LoadMaterial();
			$scope.CRMaterial = {};
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.CreateProduct = function(){
		$http.post('/Product/',$scope.CRProduct).success(function(data){
			$scope.LoadProduct();
			$scope.CRProduct = {};
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.LoadMaterial();
	$scope.LoadProduct();	

});

FirstController.controller('SaleOrderController',function SaleOrderController($scope,$log,$http,$routeParams,$location,$filter){
	$scope.bill_cus_list = [];
	$scope.CRBill = {};
	$scope.bill_det_pro_list = [];
	$scope.CRBillDet = {};
	$scope.bill_det_list = [];
	$scope.CRCustomer = {};
	$scope.CRBillDet.SumPriceBill = 0;
	$scope.TotalBill = 0;
	$scope.message = '';
	$scope.LoadCustomer = function(){
		$http.get('/Customer/').success(function(data){
			$scope.bill_cus_list = data;
		}).error(function(data){
			console.log(data)
		});
	};	

	$scope.LoadProduct = function(){
		$http.get('/Product/').success(function(data){

			$scope.bill_det_pro_list = data;
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.BillCusChange = function(){

		if($scope.bill_cus_current.customerDebt < 5000)
		{
			$scope.CRBill.billCus = $scope.bill_cus_current.customerID;
			$scope.message = '';
		}
		else
		{
			$scope.message = 'This customer have debt more than 5000$. Please select others';
		}
	};

	$scope.BillDetProChange = function(){
		$scope.CRBillDet.billDetProduct = $scope.bill_det_pro_current.productID;
	};

	$scope.AddBillDet = function(index){
		console.log(index)
		
		$http.get('/Product/'+$scope.CRBillDet.billDetProduct+'/').success(function(data){
			var r = 0;
			for (var i = 0; i < $scope.bill_det_pro_list.length; i++) {
				if($scope.bill_det_pro_list[i].productID == index)
				{
					r = i;
					break;
				}
			};
			console.log(data)
			var x = data.productPrice;
			var y = $scope.CRBillDet.billDetQuantity;
			$scope.CRBillDet.SumPriceBill = x * y;
			$scope.TotalBill = $scope.TotalBill + $scope.CRBillDet.SumPriceBill;
			$scope.CRBillDet.billDetPrice = data.productPrice;
			$scope.CRBillDet.productName = data.productName;
			console.log($scope.CRBillDet)
			$scope.bill_det_list.push($scope.CRBillDet);
			$scope.bill_det_pro_list.splice(r,1);
			console.log($scope.bill_det_pro_list)
			$scope.CRBillDet = {};
			console.log($scope.bill_det_list)
									
		});
	};

	$scope.CreateBill = function(){
		if($scope.message == '')
		{
			var d = {
				billDate : $scope.CRBill.billDate,
				billSum : $scope.TotalBill,
				billCus: $scope.CRBill.billCus,
				billState: 1
			};
			$scope.totalprice = 0;

			$http.post('/Bill/',d).success(function(data){
				$scope.CRBill = data;
				var month = $filter('date')(data.billDate,'MM');
				var year = $filter('date')(data.billDate,'yyyy');
				var MY = month+'v'+year;

				for(var i =0 ; i < $scope.bill_det_list.length; i++)
				{
					var d1 = {
						billDetProduct: $scope.bill_det_list[i].billDetProduct,
						billDetQuantity: $scope.bill_det_list[i].billDetQuantity,
						billDetBill: data.billID,
					};
					$http.post('/BillDet/',d1).success(function(d1){
						console.log(d1) 
						$scope.CRBill = {};
						$http.get('/Product/'+d1.billDetProduct+'/').success(function(d2){
							var d3 = {
								productName: d2.productName,
								productQuantity: d2.productQuantity - d1.billDetQuantity,
								productPrice: d2.productPrice,
							};
							$http.put('/Product/'+d2.productID+'/',d3).success(function(d3){
								console.log(d3)
								$http.get('/InventoryDate/'+MY+'/'+d3.productID).success(function(d8){
									console.log(d8)
									if(d8.length == 0)
									{
										d9 = {
											inventoryMonthYear : MY,
											inventoryProduct: d3.productID,
											inventoryInput: d3.productQuantity,
											inventoryOutput: d1.billDetQuantity,
											inventoryRemain:0,
											inventoryPop: (d3.productQuantity - d1.billDetQuantity),
										};
										$http.post('/Inventory/',d9).success(function(d6){
											console.log(d6)
										}).error(function(d6){
											console.log(d6)
										});
									}else{
										d8[0].inventoryOutput = d8[0].inventoryOutput + d1.billDetQuantity;
										d8[0].inventoryPop = d8[0].inventoryInput + (d8[0].inventoryRemain - d8[0].inventoryOutput);
										$http.put('/Inventory/'+d8[0].inventoryID+'/',d8[0]).success(function(d9){
											console.log(d9)
										}).error(function(d9){
											console.log(d9)
										});
									}
								}).error(function(d8){
									console.log(d8)
								});
							}).error(function(d3){
								console.log(d3)
							});
						}).error(function(d2){
							console.log(d2)
						});
					}).error(function(d1){
						console.log(d1)
					});
				}
				$http.get('/Customer/'+$scope.CRBill.billCus+'/').success(function(d4){
					d4.customerDebt = d4.customerDebt + data.billSum;
					$http.put('/Customer/'+d4.customerID+'/',d4).success(function(d5){
						console.log(d5)
						$scope.bill_det_list = [];
						$scope.LoadCustomer();
						$scope.LoadProduct();
						$scope.TotalBill = 0;
			
						$http.get('/DebtDate/'+MY+'/'+d4.customerID).success(function(d6){
							console.log(d6)
							if(d6.length == 0){
								
								d8 = {
								debtMonthYear: MY,
								debtCustomer: d4.customerID,
								debtInput: d4.customerDebt,
								debtOutput: 0,
								debtRemain: 0,
								debtPop: d4.customerDebt
								};

								$http.post('/Debt/',d8).success(function(d9){
									console.log(d9)
								}).error(function(d9){
									console.log(d9)
								});
							}else{
								d6[0].debtRemain = d6[0].debtRemain + data.billSum;
								d6[0].debtPop = d6[0].debtInput + (d6[0].debtRemain - d6[0].debtOutput)
								$http.put('/Debt/'+d6[0].debtID+'/',d6[0]).success(function(d7){
									console.log(d7)
								}).error(function(d7){
									console.log(d7)
								});
							};
						}).error(function(d6){
							console.log(d6)						
						});
					}).error(function(d5){
						console.log(d5)
						
					});
				}).error(function(data){
					console.log(d4)
				});
			}).error(function(data){
				console.log(data)

			});
		}else{
			alert('Can not create bill please')
		}
	};

	$scope.CreateCustomer = function(){
		$http.post('/Customer/',$scope.CRCustomer).success(function(data){
			console.log(data)
			$scope.CRCustomer = {}
			$scope.LoadCustomer();
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.LoadProduct();
	$scope.LoadCustomer();
});

FirstController.controller('ReceiptController', function ReceiptController($scope,$http,$filter){
	$scope.receipt_cus_list = [];
	$scope.CRReceipt = {};
	$scope.message = {};
	$scope.cus = {};

	$scope.LoadCustomer = function(){
		$http.get('/Customer/').success(function(data){
			$scope.receipt_cus_list  = data;
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.TestDebt = function(index){
		console.log(index)
		if($scope.receipt_cus_current.customerDebt < index)
		{	
			$scope.message.debt = 'Payment is not more than the debt';
		}
		else
		{
			$scope.message.debt = null;
		}
	};

	$scope.ReceiptCusChange = function(){
		$scope.CRReceipt.receiptCustomer = $scope.receipt_cus_current.customerID;
		$scope.cus = $scope.receipt_cus_current;
	};

	$scope.CreateReceipt = function(){
		if($scope.message.debt == null)
		{
			$http.post('/ReceiptManager/',$scope.CRReceipt).success(function(data){
				var month = $filter('date')(data.receiptDate,'MM');
				var year = $filter('date')(data.receiptDate,'yyyy');
				var MY = month+'v'+year;
				var debt = $scope.cus.customerDebt  	
				$scope.cus.customerDebt = $scope.cus.customerDebt - data.receiptMoney;
				$http.put('/Customer/'+$scope.cus.customerID+'/',$scope.cus).success(function(d1){
					console.log(data)
					$scope.receipt_cus_current = {};
					$scope.CRReceipt = {};
					$http.get('DebtDate/'+MY+'/'+d1.customerID).success(function(d6){
						if(d6.length == 0){	
							d8 = {
							debtMonthYear: MY,
							debtCustomer: d1.customerID,
							debtInput: debt,
							debtOutput: data.receiptMoney,
							debtRemain: 0,
							debtPop: debt - data.receiptMoney
							};

							$http.post('/Debt/',d8).success(function(d9){
								console.log(d9)
							}).error(function(d9){
								console.log(d9)
							});
						}else{
							d6[0].debtOutput = d6[0].debtOutput + data.receiptMoney;
							d6[0].debtPop = d6[0].debtInput + (d6[0].debtRemain - d6[0].debtOutput)
							$http.put('Debt/'+d6[0].debtID+'/',d6[0]).success(function(d7){
								console.log(d7)
							}).error(function(d7){
								console.log(d7)
							});
						};	
					}).error(function(d6){
						console.log(d6)						
					});
				}).error(function(d1){
					console.log(d1)
				});
			}).error(function(data){
				console.log(data)
			});
		}else{
			$scope.message.receipt = 'Do not create receipt, please check require';
		}
	};

	$scope.LoadCustomer();
});

FirstController.controller('CustomerController',function CustomerController($scope,$http){

	$scope.saleorder = [];
	$scope.customerlist = [];
	$scope.CRCustomer = {};

	$scope.DeleteCustomer = function(id){
		$http.delete('/Customer/'+id+'/').success(function(data){
			console.log(data)
			$scope.LoadCustomer();
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.LoadBill = function(){
		$http.get('/BillTemp/').success(function(data){
			$scope.saleorder = data;
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.LoadCustomer = function(){
		$http.get('/Customer/').success(function(data){
			$scope.customerlist  = data;
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.GetCustomerID = function(index){
		$scope.CRCustomer = index;
	};

	$scope.UpdateCustomer = function(){
		$http.put('/Customer/'+$scope.CRCustomer.customerID+'/').success(function(data){
			$scope.CRCustomer = {};
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.LoadCustomer();
	$scope.LoadBill();
});

FirstController.controller('ReportController',function ReportController($scope,$http){
	$scope.month_debt = {};
	$scope.year_debt = {};
	$scope.month_inventory = {};
	$scope.year_inventory = {};
	$scope.debtlist = [];
	$scope.inventorylist = [];
	console.log('aaa')
	$scope.DebtReport = function(){
		if($scope.month_debt > 9)
			var MY = $scope.month_debt+'v'+$scope.year_debt;
		else
			var MY = '0'+$scope.month_debt+'v'+$scope.year_debt;
		console.log(MY)
		$http.get('/DebtDateTemp/'+MY).success(function(data){
			$scope.debtlist = data;

		}).error(function(data){
			console.log(data)
		});
	};
	$scope.InventoryReport = function(){
		if($scope.month_inventory > 9)
			var MY = $scope.month_inventory+'v'+$scope.year_inventory;
		else
			var MY = '0'+$scope.month_inventory+'v'+$scope.year_inventory;
		$http.get('/InventoryDateTemp/'+MY).success(function(data){
			$scope.inventorylist = data;
		}).error(function(data){
			console.log(data)
		});
	};
});

FirstController.controller('OrderListController', function OrderListController($scope,$http){
	$scope.sale_order_list = [];
	$scope.purchase_order_list = [];
	$scope.customerlist = [];
	$scope.CRCus = {};
	$scope.LoadSale = function(){
		$http.get('/BillTemp/').success(function(data){
			$scope.sale_order_list = data;
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.LoadPurchase = function(){
		$http.get('/PurchaseTemp/').success(function(data){
			$scope.purchase_order_list = data;
		}).error(function(data){
			console.log(data)
		});
	};
	$scope.LoadCustomer = function(){
		$http.get('/Customer/').success(function(data){
			$scope.customerlist = data;
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.GetCusID = function(item){
		$scope.CRCus = item;
	};

	$scope.UpdateCustomer = function(){
		$http.put(/Customer/,$scope.CRCus).success(function(data){
			$scope.CRCus = {};
		}).error(function(data){
			console.log(data)
		});
	};

	$scope.DeleteCus = function(id){
		for (var i = 0; i < $scope.sale_order_list.length; i++) {
			if($scope.sale_order_list[i].billCus.customerID == id)
			{
				$http.delete('/Bill/'+$scope.sale_order_list[i].billID).success(function(data){
					console.log(data)
				}).error(function(data){
					console.log(data)
				});
			}
		};
		$http.delete('/Customer/'+id).success(function(data){
			$scope.LoadCustomer();
			$scope.LoadSale();
			alert('Do you want to delete?');
		}).error(function(data){
			console.log(data)
		});
	};
	$scope.change_stage =function(item){
		$http.get('/Bill/'+item.billID).success(function(data){
			data.billState = 4;
			$http.put('/Bill/'+data.billID,data).success(function(d){
				$scope.LoadSale();
			}).error(function(d){
				console.log(d)
			});
		}).error(function(data){
			console.log(data)
		});
	}
	$scope.LoadCustomer();
	$scope.LoadSale();
	$scope.LoadPurchase();
});