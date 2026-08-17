from django.db import models

# Create your models here.
class Category(models.Model):
    categoryName=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,blank=True)
    description=models.TextField()
    image=models.ImageField(upload_to="categoryImage",blank=True)

    def __str__(self):
        return self.categoryName
