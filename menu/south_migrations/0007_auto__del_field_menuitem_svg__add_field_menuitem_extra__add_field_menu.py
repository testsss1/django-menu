# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Renaming field 'MenuItem.svg'
        db.rename_column(u'menu_menuitem', 'svg', 'extra')

        # Adding field 'MenuItem.target'
        db.add_column(u'menu_menuitem', 'target',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'MenuItem.svg'
        db.rename_column(u'menu_menuitem', 'extra', 'svg')

        # Deleting field 'MenuItem.target'
        db.delete_column(u'menu_menuitem', 'target')


    models = {
        u'menu.menu': {
            'Meta': {'object_name': 'Menu'},
            'base_url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'menu.menuitem': {
            'Meta': {'object_name': 'MenuItem'},
            'anonymous_only': ('django.db.models.fields.BooleanField', [], {}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'extra': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'link_url': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['menu.Menu']"}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '500'}),
            'submenu': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'submenu'", 'null': 'True', 'to': u"orm['menu.Menu']"}),
            'target': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['menu']