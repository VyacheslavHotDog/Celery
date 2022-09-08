from django.test import TestCase
from mainapp.models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="apple", count=44)
        Product.objects.create(name="cucumber", count=33)
        # Product.objects.create(name="melon", count=1)
        # Product.objects.create(name="venison", count=10)

    def test_product_increase(self):
        product = Product.objects.get(name="apple")
        self.assertEqual(product.increase_count(), 451)

    def test_product_decrease(self):
        product = Product.objects.get(name="cucumber")
        self.assertEqual(product.decrease_count(), 32)

