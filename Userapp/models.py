from django.db import models
from Adminapp.models import ProductModel
from django.contrib.auth.models import User
# Create your models here.



class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_on = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'{self.product.name} (x{self.quantity}) - {self.user.username if self.user else "Guest"}'