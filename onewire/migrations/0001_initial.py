# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'KeyValue'
        db.create_table(u'onewire_keyvalue', (
            ('key', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'onewire', ['KeyValue'])

        # Adding model 'Sensors'
        db.create_table(u'onewire_sensors', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=15, primary_key=True)),
            ('state', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'onewire', ['Sensors'])


    def backwards(self, orm):
        # Deleting model 'KeyValue'
        db.delete_table(u'onewire_keyvalue')

        # Deleting model 'Sensors'
        db.delete_table(u'onewire_sensors')


    models = {
        u'onewire.keyvalue': {
            'Meta': {'object_name': 'KeyValue'},
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'onewire.sensors': {
            'Meta': {'object_name': 'Sensors'},
            'id': ('django.db.models.fields.CharField', [], {'max_length': '15', 'primary_key': 'True'}),
            'state': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['onewire']