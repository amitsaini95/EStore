from django.db import models
from CategoryApp.models import Category
# Create your models here.
from django.utils.text import slugify
from django.urls import reverse

class Product(models.Model):
    productName=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,blank=True,unique=True)
    description=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="ProductCategory")
    price=models.DecimalField(max_digits=5,decimal_places=2)
    productImage=models.ImageField(upload_to="productImage",blank=True)
    stock=models.IntegerField()
    isAvailable=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.productName
    def get_url(self):
        return reverse('productdetailCat', kwargs={'category_slug': self.category.slug,'product_slug':self.slug})
       
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.productName)
        super().save(*args, **kwargs)




class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager,self).filter(variationCategory='color',isActive=True)
    def sizes(self):
        return super(VariationManager,self).filter(variationCategory='size',isActive=True)
VARIATION_CATEGORY_CHOICES=(
('color','color'),
('size','size')
)
class Variation(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    variationCategory=models.CharField(choices=VARIATION_CATEGORY_CHOICES,max_length=10)
    variationValue=models.CharField(max_length=20)
    isActive=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now=True)
    objects=VariationManager()

    def __str__(self):
      
   
        return self.variationValue