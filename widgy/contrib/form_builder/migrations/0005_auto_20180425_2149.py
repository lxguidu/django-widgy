# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-25 21:49
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('form_builder', '0004_auto_20171117_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choicefield',
            name='ident',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='ident',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='form',
            name='ident',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='forminput',
            name='ident',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='multiplechoicefield',
            name='ident',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='textarea',
            name='ident',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]