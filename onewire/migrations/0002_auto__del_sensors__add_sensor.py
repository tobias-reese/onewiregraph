# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Sensors'
        db.delete_table(u'onewire_sensors')

        # Adding model 'Sensor'
        db.create_table(u'onewire_sensor', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=15, primary_key=True)),
            ('state', self.gf('django.db.models.fields.IntegerField')()),
            ('type', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'onewire', ['Sensor'])


    def backwards(self, orm):
        # Adding model 'Sensors'
        db.create_table(u'onewire_sensors', (
            ('state', self.gf('django.db.models.fields.IntegerField')()),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=15, primary_key=True)),
        ))
        db.send_create_signal(u'onewire', ['Sensors'])

        # Deleting model 'Sensor'
        db.delete_table(u'onewire_sensor')


    models = {
        u'onewire.keyvalue': {
            'Meta': {'object_name': 'KeyValue'},
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'onewire.sensor': {
            'Meta': {'object_name': 'Sensor'},
            'id': ('django.db.models.fields.CharField', [], {'max_length': '15', 'primary_key': 'True'}),
            'state': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['onewire']