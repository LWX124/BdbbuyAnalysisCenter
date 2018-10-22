from django.db import models

# Create your models here.

from Tools.model_util import CModel

class Coupon(CModel):
    coupon_type = models.IntegerField(blank=True, null=True)
    coupon_code = models.CharField(max_length=32, blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    need_price = models.IntegerField(blank=True, null=True)
    coupon_price = models.IntegerField(blank=True, null=True)
    coupon_desc = models.CharField(max_length=50, blank=True, null=True)
    isuse = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coupon'


class Customer(CModel):
    customer_id = models.AutoField(unique=True, primary_key=True)
    mobile = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=32, blank=True, null=True)
    last_name = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=32, blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    default_address_id = models.IntegerField(blank=True, null=True)
    password_hash = models.CharField(max_length=90, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class CustomerAddress(CModel):
    address_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    company = models.CharField(max_length=20, blank=True, null=True)
    street = models.CharField(max_length=200, blank=True, null=True)
    post_code = models.CharField(max_length=11, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_address'


class CustomerCoupon(CModel):
    customer_id = models.IntegerField(blank=True, null=True)
    coupon_id = models.IntegerField(blank=True, null=True)
    is_used = models.IntegerField(blank=True, null=True)
    is_expire = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_coupon'


class CustomerGroup(CModel):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_group'


class CustomerInviter(CModel):
    inviter_id = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    is_coupon = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_inviter'