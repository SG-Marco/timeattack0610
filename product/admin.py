from django.contrib import admin
from .models import UserOrderModel, ProductModel, OrderStatusModel, CategoryModel


# Register your models here.
admin.site.register(UserOrderModel)
admin.site.register(ProductModel)
admin.site.register(OrderStatusModel)
admin.site.register(CategoryModel)
