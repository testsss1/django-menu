# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('base_url', models.CharField(max_length=100, null=True, verbose_name='Base URL', blank=True)),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('enabled', models.BooleanField(default=True, help_text='Disable or enable menu', verbose_name='Enabled')),
            ],
            options={
                'verbose_name': 'menu',
                'verbose_name_plural': 'menus',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField(default=500, verbose_name='Order')),
                ('link_url', models.CharField(help_text='URL or URI to the content, eg /about/ or http://foo.com/', max_length=100, verbose_name='Link URL')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('login_required', models.BooleanField(help_text='Should this item only be shown to authenticated users?', verbose_name='Login required')),
                ('anonymous_only', models.BooleanField(help_text='Should this item only be shown to non-logged-in users?', verbose_name='Anonymous only')),
                ('image', models.ImageField(upload_to=b'menu', null=True, verbose_name='Picture', blank=True)),
                ('enabled', models.BooleanField(default=True, help_text='Disable or enable menu', verbose_name='Enabled')),
                ('menu', models.ForeignKey(verbose_name='Name', to='menu.Menu')),
                ('submenu', models.ForeignKey(related_name='submenu', verbose_name='Submenu', blank=True, to='menu.Menu', null=True)),
            ],
            options={
                'verbose_name': 'menu item',
                'verbose_name_plural': 'menu items',
            },
            bases=(models.Model,),
        ),
    ]
