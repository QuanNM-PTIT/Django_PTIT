from django.db import models
from book.models import Book


class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "cart_item"
        ordering = ["-created_at"]

    def total(self):
        return self.quantity * self.book.price

    def get_book_title(self):
        return self.book.title

    def get_book_price(self):
        return self.book.price


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    items = models.ManyToManyField(CartItem)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "cart"
        ordering = ["-created_at"]

    def total(self):
        total = 0
        for item in self.items.all():
            total += item.total()
        return total

    def get_items(self):
        return self.items.all()
