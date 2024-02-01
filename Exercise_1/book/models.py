from django.db import models


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    price = models.IntegerField()
    category = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000, null=True)

    class Meta:
        db_table = "book"
        ordering = ["-id"]