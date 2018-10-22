from django.shortcuts import render

import json


# django
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

# custom
from .models import *



# Create your views here.
@require_http_methods(["GET"])
def test_order(request):
    orders = Orders.objects.all()
    order_list = [i.serializable_values() for i in orders[0:10]]

    return JsonResponse({'message':'test', 'order_list': order_list})
