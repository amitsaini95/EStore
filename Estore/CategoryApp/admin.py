from django.contrib import admin
from CategoryApp.models import Category
# Register your models here.
class AdminCategory(admin.ModelAdmin):
    prepopulated_fields={'slug':('categoryName',)}
    list_display=['categoryName','slug','image']
admin.site.register(Category,AdminCategory)