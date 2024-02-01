# Generated by Django 5.0.1 on 2024-01-25 07:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book')),
            ],
            options={
                'db_table': 'cart_item',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('items', models.ManyToManyField(to='cart.cartitem')),
            ],
            options={
                'db_table': 'cart',
                'ordering': ['-created_at'],
            },
        ),
    ]