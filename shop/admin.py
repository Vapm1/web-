from django.contrib import admin

from .models import Product
# Register your models here.
# from django.contrib import admin
# from .models import MyModel


# @admin.register(MyModel)
# class MyModelAdmin(admin.ModelAdmin):
#     list_display = ('field_1', 'field_2', 'field_3', ) # указываем названия полей как в модели
#     list_editable = ('field_2', 'field_3', )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
