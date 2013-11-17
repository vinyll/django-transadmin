# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models, DatabaseError


class Migration(SchemaMigration):

    def forwards(self, orm):
        try:
            # Adding model 'Translation'
            db.create_table(u'transadmin_translation', (
                (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
                ('context', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
                ('language', self.gf('django.db.models.fields.CharField')(max_length=5)),
                ('source', self.gf('django.db.models.fields.TextField')()),
                ('trans', self.gf('django.db.models.fields.TextField')(null=True)),
                ('comment', self.gf('django.db.models.fields.TextField')(null=True)),
            ))
            db.send_create_signal(u'transadmin', ['Translation'])

            # Adding unique constraint on 'Translation', fields ['context', 'language', 'source']
            db.create_unique(u'transadmin_translation', ['context', 'language', 'source'])
        except DatabaseError:
            pass

    def backwards(self, orm):
        # Removing unique constraint on 'Translation', fields ['context', 'language', 'source']
        db.delete_unique(u'transadmin_translation', ['context', 'language', 'source'])

        # Deleting model 'Translation'
        db.delete_table(u'transadmin_translation')


    models = {
        u'transadmin.translation': {
            'Meta': {'unique_together': "(('context', 'language', 'source'),)", 'object_name': 'Translation'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'context': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'source': ('django.db.models.fields.TextField', [], {}),
            'trans': ('django.db.models.fields.TextField', [], {'null': 'True'})
        }
    }

    complete_apps = ['transadmin']
