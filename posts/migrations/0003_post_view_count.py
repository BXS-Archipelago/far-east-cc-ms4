# Generated by Django 3.2.5 on 2021-09-17 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
