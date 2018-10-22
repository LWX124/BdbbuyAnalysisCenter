from django.db import models

# Create your models here.
from Tools.model_util import CModel


class Area(CModel):
    name = models.CharField(max_length=50, blank=True, null=True)
    driver_area = models.TextField(blank=True, null=True)
    driver_id = models.IntegerField(blank=True, null=True)
    driver_time = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area'


class Invoice(CModel):
    order_id = models.IntegerField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    tax_total = models.CharField(max_length=20, blank=True, null=True)
    invoice_total = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice'


class Refunds(CModel):
    create_at = models.DateTimeField(blank=True, null=True)
    pay_type = models.IntegerField(blank=True, null=True)
    snap_order_id = models.CharField(max_length=50, blank=True, null=True)
    order_id = models.CharField(max_length=50, blank=True, null=True)
    new_order_id = models.CharField(max_length=50, blank=True, null=True)
    refund = models.IntegerField(blank=True, null=True)
    refund_products = models.CharField(max_length=200, blank=True, null=True)
    refund_shipping = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'refunds'


class Tax(CModel):
    tax_value = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tax'


class Zipcode(CModel):
    zipcode = models.CharField(max_length=50, blank=True, null=True)
    area_id = models.IntegerField(blank=True, null=True)
    free_shipping = models.IntegerField(blank=True, null=True)
    shipping_amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zipcode'