from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from pdf_django.tasks import sample_task
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    count = models.IntegerField(verbose_name='Количество',)
    description = models.CharField(verbose_name='Описание', max_length=1023, null=True)

    def get_absolute_url(self):
        return reverse('home')

    def increase_count(self):
        self.count += 1
        self.save()
        return self.count

    def decrease_count(self):
        if self.count > 0:
            self.count -= 1
            self.save()
        return self.count

    def send_report(self, pdf_data):
        sample_task.delay(pdf_data)


@receiver(pre_save, sender=Product, dispatch_uid="product_id")
def save_product(sender, instance, **kwargs):
    if instance.id is not None:
        previous = sender.objects.get(id=instance.id)
        if previous.count != instance.count:
            pdf_data = {
                'name': instance.name,
                'countBefore': previous.count,
                'countAfter': instance.count,
            }
            instance.send_report(pdf_data)
