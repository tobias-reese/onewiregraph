from django.db import models

# Create your models here.

class KeyValue(models.Model):
    key = models.CharField(max_length=255,primary_key=True)
    value = models.CharField(max_length=255,null=True,blank=True)

class Sensor(models.Model):
    DEVICE_STATE = (
        (1, 'unconfigured'),
        (10, 'configured'),
        (20, 'not connected'),
    )
    DEVICE_TYPE = (
        (1, 'temperature'),
    )
    CONSOLIDATION_TYPE = (
        (1, 'raw'),
        (0.01, 'percent (div by 100)'),
        (0.001, 'promille (div by 1000)')
    )
    id = models.CharField(max_length=15,primary_key=True)
    name = models.CharField(max_length=25,blank=False)
    state = models.IntegerField(choices=DEVICE_STATE,blank=False)
    type = models.IntegerField(choices=DEVICE_TYPE,blank=False)
    consolidation = models.FloatField(choices=CONSOLIDATION_TYPE, blank=False,default=1)
    minvalue = models.IntegerField(default=0)
    maxvalue = models.IntegerField(default=1000)