
from django.forms import widgets
from rest_framework import serializers
from apps.models import *
from cafee.settings import * 
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import *

class StateSerializer(serializers.ModelSerializer):

	class Meta:
		model = State
		fields = ('stateID','stateName')


class SupplierSerializer(serializers.ModelSerializer):

	class Meta:
		model = Supplier
		fields = ('supplierID','supplierName','supplierPhone','supplierEmail','supplierAdress')
		read_only_fields = ('pur_sup')

class PurchaseSerializer(serializers.ModelSerializer):

	class Meta:
		model = Purchase
		fields = ('purchaseID','purchaseName','purchaseSum','purchaseDate','purchaseState','purchaseSupplier')

class PurchaseTempSerializer(serializers.ModelSerializer):
	purchaseSupplier = SupplierSerializer()
	class Meta:
		model = Purchase
		fields = ('purchaseID','purchaseName','purchaseSum','purchaseDate','purchaseState','purchaseSupplier')

class ProductSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Product
		fields = ('productID','productName','productQuantity','productPrice')

class MaterialSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Material
		fields = ('materialID','materialName','materialQuantity','materialPrice')	

class BomSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Bom
		fields = ('bomID','bomName','bomProduct','bomMaterial','bomQuantity')

class BomTempSerializer(serializers.ModelSerializer):
	bomProduct = ProductSerializer()

	class Meta:
		model = Bom
		fields = ('bomID','bomName','bomProduct','bomMaterial','bomQuantity')

class BomDetSerializer(serializers.ModelSerializer):
	class Meta:
		model = BomDet
		fields = ('bomDetID','bomDetMaterial','bomDetQuantity','bomDetBom')

class BomDetTempSerializer(serializers.ModelSerializer):
	bomDetMaterial = MaterialSerializer()
	bomDetBom = BomTempSerializer()
	class Meta:
		model = BomDet
		fields = ('bomDetID','bomDetMaterial','bomDetQuantity','bomDetBom')

class PurchaseDetSerializer(serializers.ModelSerializer):

	class Meta:
		model = PurchaseDet
		fields = ('purchaseDetlID','purchaseDetMaterial','purchaseDetQuantity','purchaseDetPur')

class PurchaseDetDeSerializer(serializers.ModelSerializer):
	purchaseDetMaterial = MaterialSerializer()
	class Meta:
		model = PurchaseDet
		fields = ('purchaseDetlID','purchaseDate','purchaseDetMaterial','purchaseDetQuantity','purchaseDetPur')


class CustomerSerializer(serializers.ModelSerializer):

	class Meta:
		model = Customer 
		fields = ('customerID','customerName','customerPhone','customerEmail','customerAdress','customerDebt')

class BillSerializer(serializers.ModelSerializer):

	class Meta:
		model = Bill 
		fields = ('billID','billState','billCus','billDate','billSum')

class BillTempSerializer(serializers.ModelSerializer):
	billCus = CustomerSerializer()
	billState = StateSerializer()
	class Meta:
		model = Bill 
		fields = ('billID','billCus','billState','billDate','billSum')

class BillDetSerializer(serializers.ModelSerializer):

	class Meta:
		model = BillDet
		fields = ('billDetID','billDetBill','billDetProduct','billDetQuantity')

class ReceiptSerializer(serializers.ModelSerializer):

	class Meta:
		model = Receipt
		fields = ('receiptID','receiptCustomer','receiptDate','receiptMoney')

class ManufacturingSerializer(serializers.ModelSerializer):

	class Meta:
		model = Manufacturing
		fields = ('manufacturingID','manufacturingID','manufacturingDate','manufacturingBom','manufacturingState','manufacturingQuantity','manufacturingCreated')

class ManufacturingTempSerializer(serializers.ModelSerializer):
	manufacturingBom = BomTempSerializer()
	manufacturingState = StateSerializer()

	class Meta:
		model = Manufacturing
		fields = ('manufacturingID','manufacturingID','manufacturingDate','manufacturingBom','manufacturingState','manufacturingQuantity','manufacturingCreated')


class DebtTempSerializer(serializers.ModelSerializer):
	debtCustomer = CustomerSerializer()
	class Meta:
		model = Debt
		fields = ('debtID','debtMonthYear','debtCustomer','debtInput','debtOutput','debtRemain','debtPop')

class InventoryTempSerializer(serializers.ModelSerializer):
	inventoryProduct = ProductSerializer()
	class Meta:
		model = Inventory
		fields = ('inventoryID','inventoryMonthYear','inventoryProduct','inventoryInput','inventoryOutput','inventoryRemain','inventoryPop')

class DebtSerializer(serializers.ModelSerializer):

	class Meta:
		model = Debt
		fields = ('debtID','debtMonthYear','debtCustomer','debtInput','debtOutput','debtRemain','debtPop')

class InventorySerializer(serializers.ModelSerializer):

	class Meta:
		model = Inventory
		fields = ('inventoryID','inventoryMonthYear','inventoryProduct','inventoryInput','inventoryOutput','inventoryRemain','inventoryPop')

class AccountSerializer(serializers.ModelSerializer):

	class Meta:
		model = Account
		fields = ('accountID','username','password','name','email')