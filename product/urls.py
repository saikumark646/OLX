from django.urls import path
from .views import ProductListView,ProductDetails

app_name  = 'product'

urlpatterns = [
    path('list/',ProductListView,name = 'product_list'),
    path('list/<slug:category_slug>/',ProductListView,name = 'product_category'),
    path('list/detail/<slug:product_slug>/',ProductDetails,name = 'product_detail')
    
]
