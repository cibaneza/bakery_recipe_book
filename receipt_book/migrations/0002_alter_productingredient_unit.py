# Generated by Django 5.0.2 on 2024-02-27 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipt_book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productingredient',
            name='unit',
            field=models.CharField(choices=[('kg', 'Kilogramo'), ('g', 'Gramo'), ('unit', 'Unidad'), ('l', 'Litro'), ('ml', 'Mililitro')], max_length=10),
        ),
    ]
