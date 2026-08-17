from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import *

class AccountAdmin(UserAdmin):
    list_display=['email','username','first_name','last_name','is_superuser']
    filter_horizontal=()
    list_filter=()
    fieldsets=()
admin.site.register(Account,AccountAdmin)