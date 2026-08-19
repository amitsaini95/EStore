from django.db import models
from django.utils.text import slugify
# Create your models here.
class Category(models.Model):
    categoryName=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,blank=True)
    description=models.TextField()
    image=models.ImageField(upload_to="categoryImage",blank=True,null=True)

    class Meta:
        verbose_name="category"
        verbose_name_plural="Categories"

    def __str__(self):
        return self.categoryName
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.categoryName)
        super().save(*args, **kwargs)
