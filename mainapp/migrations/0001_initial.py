# Generated by Django 4.1 on 2022-08-31 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('count', models.IntegerField()),
                ('description', models.CharField(max_length=1023, null=True)),
            ],
        ),
    ]
