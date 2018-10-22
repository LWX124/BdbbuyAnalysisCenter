from django.db import models


#custom
from Tools.model_util import CModel

# Create your models here.

class MgOrder(CModel):
    increment_id = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, null=True)
    coupon_code = models.CharField(max_length=30, blank=True, null=True)
    shipping_description = models.CharField(max_length=30, blank=True, null=True)
    customer_id = models.CharField(max_length=30, blank=True, null=True)
    base_grand_total = models.CharField(max_length=30, blank=True, null=True)
    quote_id = models.CharField(max_length=30, blank=True, null=True)
    shipping_address = models.CharField(max_length=200, blank=True, null=True)
    detail_address = models.CharField(max_length=200, blank=True, null=True)
    customer_email = models.CharField(max_length=30, blank=True, null=True)
    firstname = models.CharField(max_length=30, blank=True, null=True)
    lastname = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    telephone = models.CharField(max_length=30, blank=True, null=True)
    postcode = models.CharField(max_length=30, blank=True, null=True)
    driver_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mg_order'


class OrderComment(CModel):
    order_id = models.IntegerField()
    customer_id = models.IntegerField(blank=True, null=True)
    comment_content = models.TextField()
    add_time = models.CharField(max_length=32, blank=True, null=True)
    customer_name = models.CharField(max_length=31, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_comment'


class OrderPay(CModel):
    create_at = models.DateTimeField(blank=True, null=True)
    pay_type = models.IntegerField(blank=True, null=True)
    snap_order_id = models.CharField(max_length=50, blank=True, null=True)
    order_id = models.CharField(max_length=50, blank=True, null=True)
    qr_code = models.CharField(max_length=50, blank=True, null=True)
    pay_status = models.IntegerField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    refund = models.IntegerField(blank=True, null=True)
    refund_msg = models.CharField(max_length=200, blank=True, null=True)
    out_trade_no = models.CharField(max_length=50, blank=True, null=True)
    new_order_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_pay'


class OrderSpecify(CModel):
    order_id = models.IntegerField(blank=True, null=True)
    driver_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_specify'


class Orders(CModel):
    order_id = models.AutoField(primary_key=True)
    area_id = models.IntegerField(blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=11, blank=True, null=True)
    product_total = models.CharField(max_length=20, blank=True, null=True)
    tax_total = models.CharField(max_length=20, blank=True, null=True)
    coupon_total = models.CharField(max_length=20, blank=True, null=True)
    sales_total = models.CharField(max_length=20, blank=True, null=True)
    shipping_total = models.CharField(max_length=20, blank=True, null=True)
    total = models.CharField(max_length=20, blank=True, null=True)
    customer_coupon_id = models.IntegerField(blank=True, null=True)
    shipping_address = models.TextField(blank=True, null=True)
    customer_name = models.CharField(max_length=30, blank=True, null=True)
    customer_mobile = models.CharField(max_length=30, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_desc = models.TextField(blank=True, null=True)
    driver_id = models.IntegerField(blank=True, null=True)
    total_pay = models.TextField(blank=True, null=True)
    order_remark = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class OrdersTest(CModel):
    order_id = models.CharField(max_length=20, blank=True, null=True)
    area_id = models.IntegerField(blank=True, null=True)
    create_at = models.DateTimeField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=11, blank=True, null=True)
    product_total = models.CharField(max_length=20, blank=True, null=True)
    tax_total = models.CharField(max_length=20, blank=True, null=True)
    coupon_total = models.CharField(max_length=20, blank=True, null=True)
    sales_total = models.CharField(max_length=20, blank=True, null=True)
    shipping_total = models.CharField(max_length=20, blank=True, null=True)
    total = models.CharField(max_length=20, blank=True, null=True)
    customer_coupon_id = models.IntegerField(blank=True, null=True)
    shipping_address = models.TextField(blank=True, null=True)
    customer_name = models.CharField(max_length=30, blank=True, null=True)
    customer_mobile = models.CharField(max_length=30, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    product_desc = models.TextField(blank=True, null=True)
    driver_id = models.IntegerField(blank=True, null=True)
    total_pay = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders_test'