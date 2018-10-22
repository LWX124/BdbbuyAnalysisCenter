from django.shortcuts import render


from .models import *

# django
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

DEFAULT_PAGE_SIZE = 20

@require_http_methods(["GET"])
def get_out_of_date_product(request):
    # 参数获取
    # page_index = request.GET.get('pageIndex', 1)
    # page_size = request.GET.get('pageSize', DEFAULT_PAGE_SIZE)
    # 获取商品数据
    product_list = [i.serializable_values() for i in Product.get_lowcount_outofdate_products()]

    # product_page_list = []
    # paginator = Paginator(product_list, page_size)
    # try:
    #     product_page_list = paginator.page(page_index)
    # except PageNotAnInteger:
    #     product_page_list = paginator.page(1)
    # except EmptyPage:
    #     product_page_list = paginator.page(paginator.num_pages)

    # product_page_list_s = [i.serializable_values() for i in product_page_list]
    return JsonResponse({'data': {'order_list': product_list, 'totalCount': len(product_list)}})