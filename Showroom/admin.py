from django.contrib import admin
from .models import *
# Register your models here.
class LoginAdmin(admin.ModelAdmin):
    list_display = ["id","name", "email"]

class ProductsAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price"]

class MessagesAdmin(admin.ModelAdmin):
    list_display = ["name","email","message"]

    
admin.site.register(UserLogin, LoginAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Messages, MessagesAdmin)