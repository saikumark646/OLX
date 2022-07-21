from itertools import product
from django.shortcuts import get_object_or_404, render
from .models import Product,PrdouctImages,Category
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
# Create your views here.

def ProductListView(request,category_slug=None):
    category = None
    products = Product.objects.all()
    
    if category_slug:
        category = get_object_or_404(Category,slug = category_slug)
        products = products.filter(category = category)
        
    search_query = request.GET.get('q')
    if search_query:
        products = products.filter(
            Q(name__icontains = search_query) |
            Q(description__icontains = search_query) |
            Q(condition__icontains = search_query) |
            Q(brand__brand_name__icontains = search_query) |
            Q(category__category_name__icontains = search_query)
        )
        
        
    categorylist = Category.objects.annotate(total_products = Count('product')) 
    # to check total number of products in a category
    
    paginator = Paginator(products,2) # which takes 2 products 
    page = request.GET.get('page')
    products = paginator.get_page(page)
    
    return render(request,'product/product_list.html',{
        "products":products,
        'category_list':categorylist,
        'category':category
    })
    
def ProductDetails(request,product_slug):
    product = get_object_or_404(Product,slug = product_slug)
    productimages = PrdouctImages.objects.filter(product_name = product )
    return render(request,'product/product_detail.html',
                  {
        'product':product,
        'product_images':productimages
    })