from django.shortcuts import render


from .models import *

# django
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

DEFAULT_LOW_COUNT = 5

@require_http_methods(["GET"])
def get_out_of_date_product(request):
    # 参数获取
    page_size = request.GET.get('lowCount', DEFAULT_LOW_COUNT)
    # 获取商品数据
    product_list = [product.toJson() for product in Product.get_lowcount_outofdate_products()]
    return JsonResponse({'data': {'order_list': product_list, 'totalCount': len(product_list)}})