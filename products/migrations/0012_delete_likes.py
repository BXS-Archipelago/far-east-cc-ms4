# Generated by Django 3.2.5 on 2021-09-14 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_remove_review_unlikes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Likes',
        ),
    ]
