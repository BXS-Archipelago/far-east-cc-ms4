# Generated by Django 3.2.5 on 2021-08-11 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_has_sizes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='has_sizes',
        ),
    ]