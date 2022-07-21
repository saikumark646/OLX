from django.contrib import admin
from .models import Product,Category,Brand,PrdouctImages
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(PrdouctImages)
admin.site.register(Brand)