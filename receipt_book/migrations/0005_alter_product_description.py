# Generated by Django 5.0.2 on 2024-02-27 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipt_book', '0004_product_yield_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
