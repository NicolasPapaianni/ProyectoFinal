# Generated by Django 4.0.6 on 2022-08-07 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category_products_price_products_stock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.FloatField(),
        ),
    ]
