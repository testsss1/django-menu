# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menuitem_svg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='svg',
            new_name='extra',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='target',
            field=models.BooleanField(default=False, help_text='Open link in new window', verbose_name='New window'),
            preserve_default=True,
        ),
    ]
