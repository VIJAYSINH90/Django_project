# Generated by Django 4.1.7 on 2023-04-10 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_vendor_product_images_vendor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(null=True, upload_to='product_images/'),
        ),
    ]
