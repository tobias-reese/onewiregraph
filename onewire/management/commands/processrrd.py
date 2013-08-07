from django.core.management.base import BaseCommand
import os
from onewire.models import Sensor


class Command(BaseCommand):
    args = None
    help = 'Processes configured sensors'

    def rrd_create(self, id):
        os.makedirs('data/' + id)

    def rrd_exist(self, id):
        return os.path.isdir('data/' + id)

    def handle(self, *args, **options):
        sensors = Sensor.objects.all().filter(state=10)
        for sensor in sensors:
            # prepare rrd
            if not self.rrd_exist(sensor.id):
                self.rrd_create(sensor.id)

            sensor_data_file = '/sys/bus/w1/devices/' + sensor.id + "/w1_slave"

            tfile = open(sensor_data_file)
            text = tfile.read()
            tfile.close()

            secondline = text.split("\n")[1]
            temperaturedata = secondline.split(" ")[9]
            temperature = float(temperaturedata[2:])
            temperature = temperature / 1000
            print(temperature)