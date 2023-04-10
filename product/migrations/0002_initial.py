# Generated by Django 4.1.7 on 2023-03-22 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor_product_images',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vendor_product_images',
            name='vendor_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.vendor_product'),
        ),
        migrations.AddField(
            model_name='vendor_product',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='vendor_product',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.vendor_detail'),
        ),
        migrations.AddField(
            model_name='vendor_detail',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.city'),
        ),
        migrations.AddField(
            model_name='vendor_detail',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.state'),
        ),
        migrations.AddField(
            model_name='vendor_detail',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.subcategory'),
        ),
        migrations.AddField(
            model_name='order_detail',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.order'),
        ),
        migrations.AddField(
            model_name='order_detail',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order_detail',
            name='vendor_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.vendor_product'),
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.customer_address'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.status'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feedback',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.vendor_detail'),
        ),
        migrations.AddField(
            model_name='customer_address',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.city'),
        ),
        migrations.AddField(
            model_name='customer_address',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.state'),
        ),
        migrations.AddField(
            model_name='customer_address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.state'),
        ),
        migrations.AddField(
            model_name='cart_detail',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.cart'),
        ),
        migrations.AddField(
            model_name='cart_detail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='cart_detail',
            name='vendorProduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.vendor_product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]