# Generated by Django 4.1.7 on 2023-04-10 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor_product_images',
            name='vendor',
        ),
        migrations.RemoveField(
            model_name='vendor_product_images',
            name='vendor_product',
        ),
        migrations.RemoveField(
            model_name='cart_detail',
            name='vendorProduct',
        ),
        migrations.RemoveField(
            model_name='order_detail',
            name='vendor_product',
        ),
        migrations.AddField(
            model_name='order_detail',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(null=True, upload_to='_product_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Vendor_product',
        ),
        migrations.DeleteModel(
            name='Vendor_product_images',
        ),
    ]
