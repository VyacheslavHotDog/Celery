import socket

from django.test import TestCase
from mainapp.models import Product
from django.db.models import signals
from .models import save_product
from unittest.mock import patch, Mock


@patch('mainapp.models.Product.send_report', return_value=True)
class ProductTestCase(TestCase):

    def setUp(self):
        Product.objects.create(name="apple", count=44)
        Product.objects.create(name="cucumber", count=33)

    def test_product_increase(self, send_report):
        product = Product.objects.get(name="apple")
        self.assertEqual(product.increase_count(), 45)
        send_report.assert_called_once()

    def test_product_decrease(self, send_report):
        product = Product.objects.get(name="cucumber")
        self.assertEqual(product.decrease_count(), 32)







