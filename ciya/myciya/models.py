from django.db import models

# Create your models here.

class user(models.Model):
    uid = models.CharField(max_length=20)
    class Meta:
        db_table ="user"