from django.db import models

# Create your models here.

class user(models.Model):
    uid = models.CharField(max_length=20)
    class Meta:
        db_table ="user"
class register(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    class Meta:
        db_table="register"