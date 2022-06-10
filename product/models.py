from django.db import models
from user.models import *


# Create your models here.

class CategoryModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "categories"


class OrderStatusModel(models.Model):
    class Meta:
        db_table = "orders"

    status = models.CharField(max_length=256, default='')

class ProductModel(models.Model):
    class Meta:
        db_table = "products"

    name = models.CharField(max_length=256, default='')
    category = models.ForeignKey('CategoryModel', on_delete=models.CASCADE)
    description = models.CharField(max_length=256, default='')
    price = models.IntegerField(default='')
    stock = models.IntegerField(default='')

    
class UserOrderModel(models.Model):
    class Meta:
        db_table = "useroredrs"

    user = models.ForeignKey('user.UserModel', on_delete=models.CASCADE)

    product = models.ForeignKey('productModel', on_delete=models.CASCADE)
    status = models.ForeignKey('OrderStatusModel', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField(default='')
    available = models.BooleanField()


