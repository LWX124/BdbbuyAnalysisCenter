from django.db import models
from django.db.models import Q

from enum import Enum

# custom
from Tools.model_util import CModel

# Create your models here.

LOW_QTY_COUNT = 5

class ProductStatus(Enum):
    ProductAll=0
    ProductOnsale=1
    ProductOffsale=2



class Category(CModel):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class CategoryProduct(CModel):
    product_id = models.IntegerField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_product'
        unique_together = (('product_id', 'category_id'),)


class Product(CModel):
    product_id = models.AutoField(primary_key=True)
    sku = models.CharField(unique=True, max_length=50, blank=True, null=True)
    en_name = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    price = models.CharField(max_length=11, blank=True, null=True)
    purchase_price = models.CharField(max_length=11, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    manufacturer = models.CharField(max_length=30, blank=True, null=True)
    images_num = models.IntegerField(blank=True, null=True)
    search_key = models.CharField(max_length=300, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    tax_id = models.CharField(max_length=11, blank=True, null=True)
    shop_ids = models.TextField(blank=True, null=True)
    cat_ids = models.CharField(max_length=200, blank=True, null=True)
    special_price = models.CharField(max_length=11, blank=True, null=True)
    special_price_start = models.CharField(max_length=32, blank=True, null=True)
    special_price_end = models.CharField(max_length=32, blank=True, null=True)
    total_sell = models.IntegerField()
    create_at = models.CharField(max_length=30, blank=True, null=True)
    quality_date = models.CharField(max_length=30, blank=True, null=True)
    show_index = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'

    @classmethod
    def get_lowcount_outofdate_products(cls, **kwargs):
        low_count = kwargs.get('low_count', 0)
        products = []
        for stock in ProductStock.get_low_qty_data(low_count=low_count):
            product_list = Product.objects.filter(product_id=stock.product_id)
            if product_list and len(product_list) > 0:
                product = product_list[0]
                if ProductStatus.ProductOnsale.value == product.status:
                    products.append(product)
        return products

    def toJson(self):
        product_qty = ProductStock.get_product_stock(product_id=self.product_id)
        json_dic = {
            'product_id': self.product_id,
            'sku': self.sku,
            'en_name': self.en_name,
            'name': self.name,
            'price': self.price,
            'purchase_price': self.purchase_price,
            'description': self.description,
            'manufacturer': self.manufacturer,
            'images_num': self.images_num,
            'search_key': self.search_key,
            'status': self.status,
            'tax_id': self.tax_id,
            'shop_ids': self.shop_ids,
            'cat_ids': self.cat_ids,
            'special_price': self.special_price,
            'special_price_start': self.special_price_start,
            'special_price_end': self.special_price_end,
            'total_sell': self.total_sell,
            'create_at': self.create_at,
            'quality_date': self.quality_date,
            'show_index': self.show_index,
            'product_qty': product_qty
        }
        return json_dic




class ProductComment(CModel):
    product_id = models.IntegerField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    create_at = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_comment'


class ProductDetail(CModel):
    product_id = models.IntegerField(blank=True, null=True)
    detail = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_detail'


class ProductOrder(CModel):
    product_id = models.IntegerField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_order'


class ProductStock(CModel):
    shop_id = models.IntegerField(blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_stock'
        unique_together = (('shop_id', 'product_id'),)

    @classmethod
    def get_low_qty_data(cls, low_count):
        product_list = ProductStock.objects.filter(qty__lte=low_count)
        return product_list

    @classmethod
    def if_low(cls, product_id, low_count):
        result = False
        try:
            product = ProductStock.objects.get(product_id=product_id)
            result = (product and int(product.qty) < low_count)
        except Exception as e:
            result = True

        return result

    @classmethod
    def get_product_stock(cls, product_id):
        count = 0
        try:
            product = ProductStock.objects.get(product_id=product_id)
            count = product.qty
            print(product.product_id)
            print(product.qty)
        except Exception as e:
            print(e)
        return count




class ProductTierPrice(CModel):
    product_id = models.IntegerField(blank=True, null=True)
    tier_price = models.CharField(max_length=30, blank=True, null=True)
    tier_count = models.IntegerField(blank=True, null=True)
    customer_group_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_tier_price'
        unique_together = (('product_id', 'customer_group_id'),)