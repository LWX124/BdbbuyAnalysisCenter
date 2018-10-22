from django.db import models

# Create your models here.

from Tools.model_util import CModel


class Car(CModel):
    car_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField(blank=True, null=True)
    coupon_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car'


class CarProduct(CModel):
    car_id = models.IntegerField(blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    product_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car_product'