from django.db import models

class Products(models.Model):
    product_id = models.CharField(max_length=50, verbose_name='کلید',null=True, blank=True )
    product_sku = models.CharField(max_length=300, verbose_name='نام محصول',null=True, blank=True )
    product_regular_price = models.CharField(max_length=300, verbose_name='قیمت عادی',null=True, blank=True )
    product_price = models.CharField(max_length=300, verbose_name='قیمت شگفت',null=True, blank=True )
    product_image = models.CharField(max_length=300, verbose_name='تصویر محصول',null=True, blank=True )
    product_permalink = models.CharField(max_length=500, verbose_name='لینک کالا',null=True, blank=True )
    product_sp = models.CharField(max_length=500, verbose_name='اولویت',null=True, blank=True )
    product_created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد', blank=True, null=True)
    product_updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی', blank=True, null=True)

    objects = models.Manager()
    
    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.product_sku