from django.test import TestCase
from .models import Products

class ProductsModelTestCase(TestCase):
    def setUp(self):
        self.product = Products.objects.create(
            product_id='123456',
            product_sku='example_sku',
            product_regular_price='100',
            product_price='80',
            product_image='example.jpg',
            product_permalink='http://example.com/product',
            product_sp='example_sp'
        )

    def test_product_creation(self):
        """Test that a product is created correctly"""
        self.assertEqual(self.product.product_id, '123456')
        self.assertEqual(self.product.product_sku, 'example_sku')
        self.assertEqual(self.product.product_regular_price, '100')
        self.assertEqual(self.product.product_price, '80')
        self.assertEqual(self.product.product_image, 'example.jpg')
        self.assertEqual(self.product.product_permalink, 'http://example.com/product')
        self.assertEqual(self.product.product_sp, 'example_sp')

    def test_verbose_names(self):
        """Test that verbose names are correctly set"""
        self.assertEqual(Products._meta.get_field('product_id').verbose_name, 'کلید')
        self.assertEqual(Products._meta.get_field('product_sku').verbose_name, 'نام محصول')
        self.assertEqual(Products._meta.get_field('product_regular_price').verbose_name, 'قیمت عادی')
        self.assertEqual(Products._meta.get_field('product_price').verbose_name, 'قیمت شگفت')
        self.assertEqual(Products._meta.get_field('product_image').verbose_name, 'تصویر محصول')
        self.assertEqual(Products._meta.get_field('product_permalink').verbose_name, 'لینک کالا')
        self.assertEqual(Products._meta.get_field('product_sp').verbose_name, 'اولویت')
        self.assertEqual(Products._meta.get_field('product_created_at').verbose_name, 'تاریخ ایجاد')
        self.assertEqual(Products._meta.get_field('product_updated_at').verbose_name, 'تاریخ بروزرسانی')

    def test_string_representation(self):
        """Test that the string representation is correct"""
        self.assertEqual(str(self.product), 'example_sku')
