# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-16 04:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('accountID', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('billID', models.AutoField(primary_key=True, serialize=False)),
                ('billDate', models.DateField()),
                ('billSum', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='BillDet',
            fields=[
                ('billDetID', models.AutoField(primary_key=True, serialize=False)),
                ('billDetQuantity', models.IntegerField(default=0)),
                ('billDetBill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bill_det_bill', to='apps.Bill')),
            ],
        ),
        migrations.CreateModel(
            name='Bom',
            fields=[
                ('bomID', models.AutoField(primary_key=True, serialize=False)),
                ('bomName', models.CharField(max_length=250)),
                ('bomQuantity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='BomDet',
            fields=[
                ('bomDetID', models.AutoField(primary_key=True, serialize=False)),
                ('bomDetQuantity', models.IntegerField(default=0)),
                ('bomDetBom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='det_bom_bom', to='apps.Bom')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customerID', models.AutoField(primary_key=True, serialize=False)),
                ('customerName', models.CharField(max_length=250)),
                ('customerPhone', models.CharField(max_length=50)),
                ('customerEmail', models.EmailField(max_length=254)),
                ('customerAdress', models.TextField()),
                ('customerDebt', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('debtID', models.AutoField(primary_key=True, serialize=False)),
                ('debtMonthYear', models.CharField(max_length=20)),
                ('debtInput', models.IntegerField(default=0)),
                ('debtOutput', models.IntegerField(default=0)),
                ('debtRemain', models.IntegerField(default=0)),
                ('debtPop', models.IntegerField(default=0)),
                ('debtCustomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deb_cus', to='apps.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('inventoryID', models.AutoField(primary_key=True, serialize=False)),
                ('inventoryMonthYear', models.CharField(max_length=20)),
                ('inventoryInput', models.IntegerField(default=0)),
                ('inventoryOutput', models.IntegerField(default=0)),
                ('inventoryRemain', models.IntegerField(default=0)),
                ('inventoryPop', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturing',
            fields=[
                ('manufacturingID', models.AutoField(primary_key=True, serialize=False)),
                ('manufacturingCreated', models.DateField(auto_now=True)),
                ('manufacturingDate', models.DateField()),
                ('manufacturingQuantity', models.IntegerField(default=0)),
                ('manufacturingBom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Bom')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('materialID', models.AutoField(primary_key=True, serialize=False)),
                ('materialName', models.CharField(max_length=250)),
                ('materialQuantity', models.IntegerField(default=0)),
                ('materialPrice', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productID', models.AutoField(primary_key=True, serialize=False)),
                ('productName', models.CharField(max_length=250)),
                ('productQuantity', models.IntegerField(default=0)),
                ('productPrice', models.IntegerField(default=0)),
                ('productDescription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('purchaseID', models.AutoField(primary_key=True, serialize=False)),
                ('purchaseName', models.CharField(max_length=250)),
                ('purchaseSum', models.IntegerField(default=0)),
                ('purchaseDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseDet',
            fields=[
                ('purchaseDetlID', models.AutoField(primary_key=True, serialize=False)),
                ('purchaseDetQuantity', models.IntegerField(default=0)),
                ('purchaseDetMaterial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pur_det_mat', to='apps.Material')),
                ('purchaseDetPur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pur_det_pur', to='apps.Purchase')),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('receiptID', models.AutoField(primary_key=True, serialize=False)),
                ('receiptDate', models.DateField()),
                ('receiptMoney', models.IntegerField(default=0)),
                ('receiptCustomer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rec_cus', to='apps.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('stateID', models.AutoField(primary_key=True, serialize=False)),
                ('stateName', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplierID', models.AutoField(primary_key=True, serialize=False)),
                ('supplierName', models.CharField(max_length=250)),
                ('supplierPhone', models.CharField(max_length=50)),
                ('supplierEmail', models.EmailField(max_length=254)),
                ('supplierAdress', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='purchase',
            name='purchaseState',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pur_sta', to='apps.State'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='purchaseSupplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pur_sup', to='apps.Supplier'),
        ),
        migrations.AddField(
            model_name='manufacturing',
            name='manufacturingState',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.State'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='inventoryProduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inv_pro', to='apps.Product'),
        ),
        migrations.AddField(
            model_name='bomdet',
            name='bomDetMaterial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='det_bom_mat', to='apps.Material'),
        ),
        migrations.AddField(
            model_name='bom',
            name='bomMaterial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bom_mat', to='apps.Material'),
        ),
        migrations.AddField(
            model_name='bom',
            name='bomProduct',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bom_pro', to='apps.Product'),
        ),
        migrations.AddField(
            model_name='billdet',
            name='billDetProduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bill_pro', to='apps.Product'),
        ),
        migrations.AddField(
            model_name='bill',
            name='billCus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bill_cus', to='apps.Customer'),
        ),
        migrations.AddField(
            model_name='bill',
            name='billState',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bill_sta', to='apps.State'),
        ),
    ]
