# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MenuItem.image'
        db.add_column(u'menu_menuitem', 'svg',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MenuItem.image'
        db.delete_column(u'menu_menuitem', 'svg')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'svg': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'link_url': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['menu.Menu']"}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '500'}),
            'submenu': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'submenu'", 'null': 'True', 'to': u"orm['menu.Menu']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['menu']