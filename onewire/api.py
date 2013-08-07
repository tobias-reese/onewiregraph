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

def sensor_exists(sensors, id):
    for sensors in sensors:
        if (sensors.id == id):
            return True
    return False

def scan():
    # get all sensors
    sensors = Sensor.objects.all()

    unconfigured = list()
    configured = list()

    for root, dirs, files in os.walk('/sys/bus/w1/devices'):
        if 'w1_bus_master1':
            dirs.remove('w1_bus_master1')
        for dir in dirs:
            if sensor_exists(sensors, dir):
                configured.append(dir)
            else:
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
    return_dict = {'unconfigured': unconfigured, 'configured': configured, 'states': Sensor.DEVICE_STATE}
    return return_dict

def sensors():
    sensors = Sensor.objects.all().filter(state=10)
    configured = list()
    for sensor in sensors:
        configured.append(sensor.id)
    return_dict = {'configured': configured}
    return return_dict

def save(request):
    id = request.POST.get('id')
    type = request.POST.get('type')
    state = request.POST.get('state')
    consolidation = request.POST.get('consolidation')
    minvalue = request.POST.get('minvalue')
    maxvalue = request.POST.get('maxvalue')
    sensor = Sensor(id=id,type=type,state=state,consolidation=consolidation,minvalue=minvalue,maxvalue=maxvalue)
    sensor.save(1)
