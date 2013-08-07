# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Sensor.consolidation'
        db.add_column(u'onewire_sensor', 'consolidation',
                      self.gf('django.db.models.fields.FloatField')(default=1),
                      keep_default=False)

        # Adding field 'Sensor.minvalue'
        db.add_column(u'onewire_sensor', 'minvalue',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Sensor.maxvalue'
        db.add_column(u'onewire_sensor', 'maxvalue',
                      self.gf('django.db.models.fields.IntegerField')(default=1000),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Sensor.consolidation'
        db.delete_column(u'onewire_sensor', 'consolidation')

        # Deleting field 'Sensor.minvalue'
        db.delete_column(u'onewire_sensor', 'minvalue')

        # Deleting field 'Sensor.maxvalue'
        db.delete_column(u'onewire_sensor', 'maxvalue')


    models = {
        u'onewire.keyvalue': {
            'Meta': {'object_name': 'KeyValue'},
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'onewire.sensor': {
            'Meta': {'object_name': 'Sensor'},
            'consolidation': ('django.db.models.fields.FloatField', [], {'default': '1'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '15', 'primary_key': 'True'}),
            'maxvalue': ('django.db.models.fields.IntegerField', [], {'default': '1000'}),
            'minvalue': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'state': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['onewire']