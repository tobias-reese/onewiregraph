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
        (30, 'deleted'),
    )
    DEVICE_TYPE = (
        (1, 'temperature'),
    )
    id = models.CharField(max_length=15,primary_key=True)
    state = models.IntegerField(choices=DEVICE_STATE,blank=False)
    type = models.IntegerField(choices=DEVICE_TYPE,blank=False)
