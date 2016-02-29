from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from apps.views import *
from django.conf import settings

urlpatterns = patterns('',
	url(r'^OrderList/$', orderlist, name="orderlist"),
	url(r'^login/$', login, name="login"),
	url(r'^$', base, name="base"),
	url(r'^Home/$', index, name="index"),
	url(r'^CR_purchase/$', form_component, name="form_component"),
	url(r'^Struct/$', struct, name="struct"),
	url(r'^ManuOrder/$', manufacturing, name="Manufacturing"),
	url(r'^WareHouse/$', warehouse, name="warehouse"),
	url(r'^SaleOrder/$', saleorder, name="saleorder"),
	url(r'^Receipt/$', receipt, name="receipt"),
	url(r'^CustomerManager/$', customer, name="customer"),
	url(r'^Report/$', report, name="report"),

	url(r'^State/$',StateList.as_view(),name="statelist"),
	url(r'^State/(?P<pk>[0-9]+)/$',StateDetail.as_view(),name="statedetail"),

	url(r'^Supplier/$',SupplierList.as_view(),name="Supplierlist"),
	url(r'^Supplier/(?P<pk>[0-9]+)/$',SupplierDetail.as_view(),name="Supplierdetail"),
	
	url(r'^Purchase/$',PurchaseList.as_view(),name="Purchaselist"),
	url(r'^Purchase/(?P<pk>[0-9]+)/$',PurchaseDetail.as_view(),name="Purchasedetail"),

	url(r'^PurchaseTemp/$',PurchaseListTemp.as_view(),name="Purchaselist"),
	url(r'^PurchaseTemp/(?P<pk>[0-9]+)/$',PurchaseDetailTemp.as_view(),name="Purchasedetail"),
	
	url(r'^Product/$',ProductList.as_view(),name="Productlist"),
	url(r'^Product/(?P<pk>[0-9]+)/$',ProductDetail.as_view(),name="Productdetail"),

	url(r'^Bom/$',BomList.as_view(),name="Bomlist"),
	url(r'^Bom/(?P<pk>[0-9]+)/$',BomDetail.as_view(),name="Bomdetail"),
	
	url(r'^BomDet/$',BomDetList.as_view(),name="Bomdetlist"),
	url(r'^BomDet/(?P<pk>[0-9]+)/$',BomDetDetail.as_view(),name="Bomdetdetail"),

	url(r'^BomDetTemp/(?P<bomID>[0-9a-zA-Z_-]+)/Bom$',BomDetTempList.as_view(),name="Bomdettemplist"),

	url(r'^DebtDate/(?P<debtMonthYear>[0-9a-zA-Z_-]+)/(?P<debtCustomer>[0-9a-zA-Z_-]+)$',DebtDate.as_view(),name="DebtDate"),

	url(r'^Material/$',MaterialList.as_view(),name="Materiallist"),
	url(r'^Material/(?P<pk>[0-9]+)/$',MaterialDetail.as_view(),name="Materialdetail"),

	url(r'^PurchaseDet/$',PurchaseDetList.as_view(),name="PurchaseDetailDelist"),
	url(r'^PurchaseDet/(?P<pk>[0-9]+)/$',PurchaseDetDetail.as_view(),name="PurchaseDetailDedetail"),

	url(r'^PurchaseDetDe/$',PurchaseDetDeList.as_view(),name="PurchaseDetaillist"),
	url(r'^PurchaseDetDe/(?P<pk>[0-9]+)/$',PurchaseDetDeDetail.as_view(),name="PurchaseDetaildetail"),

	url(r'^Customer/$',CustomerList.as_view(),name="Customerlist"),
	url(r'^Customer/(?P<pk>[0-9]+)/$',CustomerDetail.as_view(),name="Customerdetail"),

	url(r'^Bill/$',BillList.as_view(),name="Billlist"),
	url(r'^Bill/(?P<pk>[0-9]+)/$',BillDetail.as_view(),name="Billdetail"),

	url(r'^BillTemp/$',BillTempList.as_view(),name="Billlist"),
	url(r'^BillTemp/(?P<pk>[0-9]+)/$',BillTempDetail.as_view(),name="Billdetail"),	

	url(r'^BillDet/$',BillDetList.as_view(),name="BillDetlist"),
	url(r'^BillDet/(?P<pk>[0-9]+)/$',BillDetDetail.as_view(),name="BillDetdetail"),

	url(r'^ReceiptManager/$',ReceiptList.as_view(),name="Receiptlist"),
	url(r'^ReceiptManager/(?P<pk>[0-9]+)/$',ReceiptDetail.as_view(),name="Receiptdetail"),

	url(r'^Manufacturing/$',ManufacturingList.as_view(),name="Manufacturinglist"),
	url(r'^Manufacturing/(?P<pk>[0-9]+)/$',ManufacturingDetail.as_view(),name="Manufacturingdetail"),

	url(r'^ManufacturingTemp/$',ManufacturingTempList.as_view(),name="Manufacturinglist"),
	url(r'^ManufacturingTemp/(?P<pk>[0-9]+)/$',ManufacturingTempDetail.as_view(),name="Manufacturingdetail"),			

	url(r'^Debt/$',DebtList.as_view(),name="DebtList"),
	url(r'^Debt/(?P<pk>[0-9]+)/$',DebtDetail.as_view(),name="DebtDetail"),

	url(r'^Inventory/$',InventoryList.as_view(), name="InventoryList"),
	url(r'^Inventory/(?P<pk>[0-9]+)/$',InventoryDetail.as_view(), name="InventoryDetail"),	

	url(r'^InventoryDate/(?P<inventoryMonthYear>[0-9a-zA-Z_-]+)/(?P<inventoryProduct>[0-9a-zA-Z_-]+)$',InventoryDate.as_view(),name="inventoryDate"),
	url(r'^DebtDateTemp/(?P<debtMonthYear>[0-9a-zA-Z_-]+)$',DebtDateTemp.as_view(),name="DebtDate"),	
	url(r'^InventoryDateTemp/(?P<inventoryMonthYear>[0-9a-zA-Z_-]+)$',InventoryDateTemp.as_view(),name="inventoryDate"),

	url(r'^Acc/$',AccountList.as_view(),name="AccountList"),
	url(r'^Acc/(?P<pk>[0-9]+)/$',AccountDetail.as_view(),name="AccountDetail"),
	#example:
	url(r'^ExampleView/$',ExampleView.as_view(),name="ExampleView"),
)