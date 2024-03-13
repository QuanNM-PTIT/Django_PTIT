from djongo import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'
        ordering = ['-created_at']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    supplier = models.CharField(max_length=255)
    sku = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/covers/')
    quantity = models.IntegerField()
    description = models.TextField()
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'
        ordering = ['created_at']

    def __str__(self):
        return self.name
