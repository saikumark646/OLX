from tabnanny import verbose
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify 
# slugify is used for urls,it converts cap lettrs to small and spaces to -
# product name = Poco X3, slug will be poco-x3
# Create your models here.

class Product(models.Model):
    condition_choices = (('New','new'),
                        ('Old','old'))

    name = models.CharField(max_length = 20)
    slug = models.SlugField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null = True)
    brand = models.ForeignKey('Brand',on_delete=models.SET_NULL,null = True) 
    description = models.TextField()
    condition = models.CharField(max_length = 10, choices = condition_choices)
    image = models.ImageField(upload_to='main_product/',blank=True, null=True)
    price = models.DecimalField(max_digits = 10,decimal_places=5)
    created_at = models.DateTimeField(auto_now_add = True)
    
    def save(self,*args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Product,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    category_name = models.CharField(max_length=20)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to='category/',blank=True, null=True)
    
    def save(self,*args, **kwargs):
        if not self.slug and self.category_name:
            self.slug = slugify(self.category_name)
        super(Category,self).save(*args, **kwargs)
        
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.category_name
    
class Brand(models.Model):
    brand_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.brand_name
    
class PrdouctImages(models.Model):
    product_name = models.ForeignKey(Product,on_delete = models.CASCADE)
    image = models.ImageField(upload_to='products/',blank=True, null=True)

    class Meta:
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'
    def __str__(self):
        return str(self.product_name)