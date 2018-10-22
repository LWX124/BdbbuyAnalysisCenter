
from django.urls import path


from .views import *

urlpatterns = [

    path('getWarnigProduct', get_out_of_date_product),

]