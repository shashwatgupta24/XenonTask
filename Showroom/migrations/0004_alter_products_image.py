# Generated by Django 4.0.6 on 2022-11-09 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Showroom', '0003_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='uploads/products/'),
        ),
    ]