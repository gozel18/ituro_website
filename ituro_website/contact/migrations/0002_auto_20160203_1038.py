# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-03 10:38
from __future__ import unicode_literals

import contact.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='img',
            field=models.ImageField(upload_to=contact.models.get_upload_path),
        ),
    ]
