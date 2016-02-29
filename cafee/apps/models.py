from django.db import models
from django.db import models
from cafee import settings
from django.utils import timezone
from django.contrib.auth.models import User
from time import time

import os

# Create your models here.
class State(models.Model):
	stateID = models.AutoField(primary_key = True)
	stateName = models.CharField(max_length=250)
	
	def __unicode__(self):
		return self.stateName

class Supplier(models.Model):
	supplierID = models.AutoField(primary_key = True)
	supplierName = models.CharField(max_length = 250)
	supplierPhone = models.CharField(max_length = 50)
	supplierEmail = models.EmailField()
	supplierAdress = models.TextField()

	def __unicode__(self):
		return self.supplierName

class Purchase(models.Model):
	purchaseID = models.AutoField(primary_key = True)
	purchaseName = models.CharField(max_length = 250)
	purchaseSum = models.IntegerField(default = 0)
	purchaseDate = models.DateField()
	purchaseState = models.ForeignKey(State,related_name='pur_sta')
	purchaseSupplier = models.ForeignKey(Supplier,related_name='pur_sup')
	
	def __unicode__(self):
		return self.purchaseName

class Product(models.Model):
	productID = models.AutoField(primary_key = True)
	productName = models.CharField(max_length = 250)
	productQuantity = models.IntegerField(default = 0)
	productPrice = models.IntegerField(default = 0)
	productDescription = models.TextField()

	def __unicode__(self):
		return self.productName

class Material(models.Model):
	materialID = models.AutoField(primary_key = True)
	materialName = models.CharField(max_length = 250)
	materialQuantity = models.IntegerField(default = 0)
	materialPrice = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.materialName

class Bom(models.Model):
	bomID = models.AutoField(primary_key = True)
	bomName = models.CharField(max_length = 250)
	bomProduct = models.ForeignKey(Product,related_name='bom_pro',null = True, blank = True)
	bomMaterial = models.ForeignKey(Material,related_name='bom_mat',null = True, blank = True)
	bomQuantity = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.bomName

class BomDet(models.Model):
	bomDetID = models.AutoField(primary_key = True)
	bomDetMaterial = models.ForeignKey(Material,related_name='det_bom_mat')
	bomDetQuantity = models.IntegerField(default = 0)
	bomDetBom = models.ForeignKey(Bom,related_name='det_bom_bom')

	def  __unicode__(self):
		return u"%s" % self.bomDetID

class PurchaseDet(models.Model):
	purchaseDetlID = models.AutoField(primary_key = True)
	purchaseDetMaterial = models.ForeignKey(Material,related_name = 'pur_det_mat')
	purchaseDetQuantity = models.IntegerField(default = 0)
	purchaseDetPur = models.ForeignKey(Purchase, related_name="pur_det_pur")
	
	def __unicode__(self):
		return u"%s" % self.purchaseDetlID	

class Customer(models.Model):
	customerID = models.AutoField(primary_key = True)
	customerName = models.CharField(max_length = 250)
	customerPhone = models.CharField(max_length = 50)
	customerEmail = models.EmailField()
	customerAdress = models.TextField()
	customerDebt = models.IntegerField(default = 0)

	def __unicode__(self):
		return self.customerName

class Bill(models.Model):
	billID = models.AutoField(primary_key = True)
	billCus = models.ForeignKey(Customer, related_name = 'bill_cus')
	billDate = models.DateField()
	billSum = models.IntegerField(default = 0)
	billState = models.ForeignKey(State, related_name = 'bill_sta')
	def __unicode__(self):
		return u"%s" % self.billID

class BillDet(models.Model):
	billDetID = models.AutoField(primary_key = True)
	billDetBill = models.ForeignKey(Bill, related_name = 'bill_det_bill')
	billDetProduct = models.ForeignKey(Product,related_name = 'bill_pro')
	billDetQuantity = models.IntegerField(default = 0)

class Receipt(models.Model):
	receiptID = models.AutoField(primary_key = True)
	receiptCustomer = models.ForeignKey(Customer, related_name = 'rec_cus')
	receiptDate = models.DateField()
	receiptMoney = models.IntegerField(default = 0)

	def  __unicode__(self):
		return u"%s" % self.receiptID

class Manufacturing(models.Model):
	manufacturingID = models.AutoField(primary_key = True)
	manufacturingCreated = models.DateField(auto_now = True)
	manufacturingDate = models.DateField()
	manufacturingBom = models.ForeignKey(Bom)
	manufacturingState = models.ForeignKey(State)
	manufacturingQuantity = models.IntegerField(default = 0)

	def __unicode__(self):
		return u"%s" % self.manufacturingID

class Inventory(models.Model):
	inventoryID = models.AutoField(primary_key = True)
	inventoryMonthYear = models.CharField(max_length =20)
	inventoryProduct = models.ForeignKey(Product, related_name = 'inv_pro')
	inventoryInput = models.IntegerField(default = 0)
	inventoryOutput = models.IntegerField(default = 0)
	inventoryRemain = models.IntegerField(default = 0)
	inventoryPop = models.IntegerField(default =0)

	def __unicode__(self):
		return u"%s" % self.inventoryID

class Debt(models.Model):
	debtID = models.AutoField(primary_key = True)
	debtMonthYear = models.CharField(max_length = 20)
	debtCustomer = models.ForeignKey(Customer, related_name ='deb_cus')
	debtInput = models.IntegerField(default = 0)
	debtOutput = models.IntegerField(default = 0)
	debtRemain = models.IntegerField(default = 0)
	debtPop = models.IntegerField(default = 0)

	def __unicode__(self):
		return u"%s" % self.debtID

class Account(models.Model):
	accountID = models.AutoField(primary_key = True)
	username = models.CharField(max_length = 20)
	password = models.CharField(max_length = 20)
	email = models.CharField(max_length = 200)
	name = models.CharField(max_length = 200)

	def __unicode__(self):
		return u"%s" % self.accountID 