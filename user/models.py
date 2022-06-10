from django.db import models

# Create your models here.
class UserModel(models.Model):
    class Meta:
        db_table = "users"

    email = models.CharField(max_length=256, default='')
    password = models.CharField(max_length=256, default='')
