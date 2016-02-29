from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, get_object_or_404,HttpResponseRedirect
from apps.models import *
from django.core.context_processors import csrf
import json
from django.http import HttpResponse
from django.core import serializers
import datetime
from django.core.urlresolvers import reverse
from rest_framework import status,generics
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django.contrib.auth.models import User 
from apps.serializers import *
from rest_framework.pagination import PageNumberPagination 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# Create your views here.

def orderlist(request):
	return render(request,"Theme/pur_sale_list.html",{})

def login(request):
	return render(request,"Theme/login.html",{})

def base(request):
	return render(request,"Theme/base.html",{})

def index(request):
	return render(request,"Theme/index.html",{})

def form_component(request):
	return render(request,"Theme/form_component.html",{})

def struct(request):
	return render(request,"Theme/struct.html",{})

def manufacturing(request):
	return render(request,"Theme/manufacturing.html",{})

def warehouse(request):
	return render(request,"Theme/warehouse.html",{})

def saleorder(request):
	return render(request,"Theme/saleorder.html",{})

def receipt(request):
	return render(request,"Theme/receipt.html",{})

def customer(request):
	return render(request,'Theme/customer.html',{})

def report(request):
	return render(request,'Theme/report.html',{})

class ExampleView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10

class StateList(generics.ListCreateAPIView):
	queryset = State.objects.all()
	serializer_class = StateSerializer

class StateDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = State.objects.all()
	serializer_class = StateSerializer

class SupplierList(generics.ListCreateAPIView):
	queryset = Supplier.objects.all()
	serializer_class = SupplierSerializer

class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Supplier.objects.all()
	serializer_class = SupplierSerializer

class PurchaseList(generics.ListCreateAPIView):
	queryset = Purchase.objects.all()
	serializer_class = PurchaseSerializer

class PurchaseDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Purchase.objects.all()
	serializer_class = PurchaseSerializer

class PurchaseListTemp(generics.ListCreateAPIView):
	queryset = Purchase.objects.all()
	serializer_class = PurchaseTempSerializer

class PurchaseDetailTemp(generics.RetrieveUpdateDestroyAPIView):
	queryset = Purchase.objects.all()
	serializer_class = PurchaseTempSerializer

class ProductList(generics.ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class BomList(generics.ListCreateAPIView):
	queryset = Bom.objects.all()
	serializer_class = BomSerializer

class BomDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Bom.objects.all()
	serializer_class = BomSerializer

class BomDetList(generics.ListCreateAPIView):
	queryset = BomDet.objects.all()
	serializer_class = BomDetSerializer

class BomDetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = BomDet.objects.all()
	serializer_class = BomDetSerializer

class MaterialList(generics.ListCreateAPIView):
	queryset = Material.objects.all()
	serializer_class = MaterialSerializer
	pagination_class = StandardResultsSetPagination

class MaterialDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Material.objects.all()
	serializer_class = MaterialSerializer

class PurchaseDetList(generics.ListCreateAPIView):
	queryset = PurchaseDet.objects.all()
	serializer_class = PurchaseDetSerializer

class PurchaseDetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = PurchaseDet.objects.all()
	serializer_class = PurchaseDetSerializer

class PurchaseDetDeList(generics.ListCreateAPIView):
	queryset = PurchaseDet.objects.all()
	serializer_class = PurchaseDetDeSerializer

class PurchaseDetDeDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = PurchaseDet.objects.all()
	serializer_class = PurchaseDetDeSerializer

class BillList(generics.ListCreateAPIView):
	queryset = Bill.objects.all()
	serializer_class = BillSerializer

class BillDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Bill.objects.all()
	serializer_class = BillSerializer

class BillTempList(generics.ListCreateAPIView):
	queryset = Bill.objects.all()
	serializer_class = BillTempSerializer

class BillTempDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Bill.objects.all()
	serializer_class = BillTempSerializer

class BillDetList(generics.ListCreateAPIView):
	queryset = BillDet.objects.all()
	serializer_class = BillDetSerializer

class BillDetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = BillDet.objects.all()
	serializer_class = BillDetSerializer

class ReceiptList(generics.ListCreateAPIView):
	queryset = Receipt.objects.all()
	serializer_class = ReceiptSerializer

class ReceiptDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Receipt.objects.all()
	serializer_class = ReceiptSerializer
	
class CustomerList(generics.ListCreateAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer

class ManufacturingList(generics.ListCreateAPIView):
	queryset = Manufacturing.objects.all()
	serializer_class = ManufacturingSerializer

class ManufacturingDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Manufacturing.objects.all()
	serializer_class = ManufacturingSerializer

class BomDetTempList(generics.ListAPIView):
	queryset = BomDet.objects.all()
	serializer_class = BomDetTempSerializer

	def get_queryset(self):
		queryset = super(BomDetTempList, self).get_queryset()
		return queryset.filter(bomDetBom__bomID = self.kwargs.get('bomID'))

class DebtDate(generics.ListAPIView):
	queryset = Debt.objects.all()
	serializer_class = DebtSerializer

	def get_queryset(self):
		queryset = super(DebtDate,self).get_queryset()
		return queryset.filter(debtMonthYear = self.kwargs.get('debtMonthYear'),debtCustomer = self.kwargs.get('debtCustomer'))

class ManufacturingTempList(generics.ListCreateAPIView):
	queryset = Manufacturing.objects.all()
	serializer_class = ManufacturingTempSerializer

class ManufacturingTempDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Manufacturing.objects.all()
	serializer_class = ManufacturingTempSerializer

class DebtList(generics.ListCreateAPIView):
	queryset = Debt.objects.all()
	serializer_class = DebtSerializer

class DebtDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Debt.objects.all()
	serializer_class = DebtSerializer

class InventoryList(generics.ListCreateAPIView):
	queryset = Inventory.objects.all()
	serializer_class = InventorySerializer

class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Inventory.objects.all()
	serializer_class = InventorySerializer

class InventoryDate(generics.ListAPIView):
	queryset = Inventory.objects.all()
	serializer_class = InventorySerializer

	def get_queryset(self):
		queryset = super(InventoryDate,self).get_queryset()
		return queryset.filter(inventoryMonthYear = self.kwargs.get('inventoryMonthYear'),inventoryProduct = self.kwargs.get('inventoryProduct'))

class DebtDateTemp(generics.ListAPIView):
	queryset = Debt.objects.all()
	serializer_class = DebtTempSerializer

	def get_queryset(self):
		queryset = super(DebtDateTemp,self).get_queryset()
		return queryset.filter(debtMonthYear = self.kwargs.get('debtMonthYear'))


class InventoryDateTemp(generics.ListAPIView):
	queryset = Inventory.objects.all()
	serializer_class = InventoryTempSerializer

	def get_queryset(self):
		queryset = super(InventoryDateTemp,self).get_queryset()
		return queryset.filter(inventoryMonthYear = self.kwargs.get('inventoryMonthYear'))

class AccountList(generics.ListCreateAPIView):
	queryset = Account.objects.all()
	serializer_class = AccountSerializer

class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Account.objects.all()
	serializer_class = AccountSerializer

	
# Create your views here.
