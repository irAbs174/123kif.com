# Generated by Django 5.0.1 on 2024-02-05 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='کلید')),
                ('product_sku', models.CharField(blank=True, max_length=300, null=True, verbose_name='نام محصول')),
                ('product_regular_price', models.CharField(blank=True, max_length=300, null=True, verbose_name='قیمت عادی')),
                ('product_price', models.CharField(blank=True, max_length=300, null=True, verbose_name='قیمت شگفت')),
                ('product_image', models.CharField(blank=True, max_length=300, null=True, verbose_name='تصویر محصول')),
                ('product_permalink', models.CharField(blank=True, max_length=500, null=True, verbose_name='لینک کالا')),
                ('product_sp', models.CharField(blank=True, max_length=500, null=True, verbose_name='اولویت')),
                ('product_created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد')),
                ('product_updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='تاریخ بروزرسانی')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
    ]
