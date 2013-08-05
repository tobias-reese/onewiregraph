from datetime import datetime
import os
from onewire.models import KeyValue, Sensor

__author__ = 'sickboy'

dateformat = '%Y%m%d %H:%M:%S'
dateformat_print = '%Y-%m-%d %H:%M:%S'

def last_scan():
    try:
        last = KeyValue.objects.get(pk='last_scan')
        lastscan = datetime.strptime(last.value, dateformat)
        return lastscan.strftime(dateformat_print)
    except KeyValue.DoesNotExist:
        return None

def scan():
    # get all sensors
    sensors = Sensor.objects.all()

    unconfigured = list()

    for root, dirs, files in os.walk('/sys/bus/w1/devices'):
        if 'w1_bus_master1':
            dirs.remove('w1_bus_master1')
        for dir in dirs:
            unconfigured.append(dir)

    # update last scan
    try:
        last = KeyValue.objects.get(pk='last_scan')
        last.value = datetime.now().strftime(dateformat)
        last.save()
    except KeyValue.DoesNotExist:
        last = KeyValue(key='last_scan', value=datetime.now().strftime(dateformat))
        last.save()

    # build dict
    return_dict = {'unconfigured': unconfigured, 'states': Sensor.DEVICE_STATE}
    return return_dict
