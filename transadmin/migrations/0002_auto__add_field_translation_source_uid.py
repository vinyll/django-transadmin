# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Translation.source_uid'
        db.add_column(u'transadmin_translation', 'source_uid',
                      self.gf('django.db.models.fields.CharField')(max_length=32, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Translation.source_uid'
        db.delete_column(u'transadmin_translation', 'source_uid')


    models = {
        u'transadmin.translation': {
            'Meta': {'unique_together': "(('context', 'language', 'source'),)", 'object_name': 'Translation'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'context': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'source': ('django.db.models.fields.TextField', [], {}),
            'source_uid': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True'}),
            'trans': ('django.db.models.fields.TextField', [], {'null': 'True'})
        }
    }

    complete_apps = ['transadmin']