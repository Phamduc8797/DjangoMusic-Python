# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-27 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0003_image_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.ImageField(upload_to='static/images/uploads'),
        ),
    ]
