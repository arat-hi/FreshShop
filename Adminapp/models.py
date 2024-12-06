from django.db import models

# Create your models here.

class AdminModel(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.admin_username



class ProductModel(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=400)
    description = models.TextField(null=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'product_table'

