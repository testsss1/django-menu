# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='svg',
            field=models.CharField(max_length=120, null=True, verbose_name='SVG Icon', blank=True),
            preserve_default=True,
        ),
    ]
