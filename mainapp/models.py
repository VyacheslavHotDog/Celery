from django.db import models

# Create your models here.
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    count = models.IntegerField(verbose_name='Количество',)
    description = models.CharField(verbose_name='Описание', max_length=1023, null=True)

    def get_absolute_url(self):
        return reverse('home')
