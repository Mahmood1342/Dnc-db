# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apisending',
            options={'ordering': ('-created',), 'verbose_name': 'api_sending'},
        ),
        migrations.AlterModelOptions(
            name='phonedata',
            options={'ordering': ('-created',), 'verbose_name': 'phone_data'},
        ),
        migrations.AlterField(
            model_name='apisending',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='phonedata',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='phonedata',
            name='phone_number',
            field=models.CharField(db_index=True, max_length=15),
        ),
    ]