from django.db import models


# Create your models here.
class CartItem(models.Model):
    cart_id = models.ForeignKey('Cart', on_delete=models.CASCADE)
    book_id = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'CartItems'
        ordering = ['created_at']

    def __str__(self):
        return self.cart_id


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Carts'
        ordering = ['created_at']


    def __str__(self):
        return self.cart_id