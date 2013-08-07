# -*- coding: utf8 -*-
from django.core.management.base import BaseCommand
import os
import shlex
from onewire.models import Sensor
from subprocess import call
from onewiregraph import settings


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
                # archives
                # 24 points for last 2h with 5 min resulution
                # 96 points for last 24h with 15 min resolution
                # 210 points for last 7d with 2h resolution
                # 280 points for last 1month with 12h resolution
                # 360 points for last 1y with 1d resolution
                create_cmd = "rrdtool create data/" + sensor.id + "/data.rrd " \
                                                                      "DS:temperatur:GAUGE:600:U:U " \
                                                                      "RRA:AVERAGE:0.5:1:24 " \
                                                                      "RRA:AVERAGE:0.5:3:96 " \
                                                                      "RRA:AVERAGE:0.5:48:210 " \
                                                                      "RRA:AVERAGE:0.5:144:280 " \
                                                                      "RRA:AVERAGE:0.5:288:360"
                call(create_cmd.split(" "))

            sensor_data_file = '/sys/bus/w1/devices/' + sensor.id + "/w1_slave"

            tfile = open(sensor_data_file)
            text = tfile.read()
            tfile.close()

            secondline = text.split("\n")[1]
            temperaturedata = secondline.split(" ")[9]
            temperature = float(temperaturedata[2:])
            temperature = temperature / 1000
            update_cmd = "rrdtool update data/" + sensor.id + "/data.rrd N:" + unicode(temperature)
            call(update_cmd.split(" "))
            print(sensor.id + u"->" + unicode(temperature)+u"°C")
            graph1_cmd = "rrdtool graph data/" + sensor.id + "/hour.png --end now -Y --start end-2h --width 419 --height 250 " \
                                                             "DEF:temp=data/" + sensor.id + "/data.rrd:temperatur:AVERAGE " \
                                                             "LINE2:temp#FF0000 " \
                                                             "VDEF:tempmax=temp,MAXIMUM " \
                                                             "VDEF:tempmin=temp,MINIMUM " \
                                                             u"GPRINT:tempmax:\"Max  %6.2lf\" " \
                                                             u"GPRINT:tempmin:\"Min  %6.2lf\" "


            call(shlex.split(graph1_cmd))
            graph2_cmd = "rrdtool graph data/" + sensor.id + "/day.png --end now -Y --start end-1d --width 419 --height 250 " \
                                                             "DEF:temp=data/" + sensor.id + "/data.rrd:temperatur:AVERAGE " \
                                                             "LINE2:temp#FF0000 " \
                                                             "VDEF:tempmax=temp,MAXIMUM " \
                                                             "VDEF:tempmin=temp,MINIMUM " \
                                                             u"GPRINT:tempmax:\"Max  %6.2lf\" " \
                                                             u"GPRINT:tempmin:\"Min  %6.2lf\" "
            call(shlex.split(graph2_cmd))
            graph3_cmd = "rrdtool graph data/" + sensor.id + "/week.png --end now -Y --start end-1w --width 419 --height 250 " \
                                                             "DEF:temp=data/" + sensor.id + "/data.rrd:temperatur:AVERAGE " \
                                                             "LINE2:temp#FF0000 " \
                                                             "VDEF:tempmax=temp,MAXIMUM " \
                                                             "VDEF:tempmin=temp,MINIMUM " \
                                                             u"GPRINT:tempmax:\"Max  %6.2lf\" " \
                                                             u"GPRINT:tempmin:\"Min  %6.2lf\" "
            call(shlex.split(graph3_cmd))
            graph4_cmd = "rrdtool graph data/" + sensor.id + "/month.png --end now -Y --start end-30d --width 419 --height 250 " \
                                                             "DEF:temp=data/" + sensor.id + "/data.rrd:temperatur:AVERAGE " \
                                                             "LINE2:temp#FF0000 " \
                                                             "VDEF:tempmax=temp,MAXIMUM " \
                                                             "VDEF:tempmin=temp,MINIMUM " \
                                                             u"GPRINT:tempmax:\"Max  %6.2lf\" " \
                                                             u"GPRINT:tempmin:\"Min  %6.2lf\" "
            call(shlex.split(graph4_cmd))
            graph5_cmd = "rrdtool graph data/" + sensor.id + "/year.png --end now -Y --start end-1y --width 419 --height 250 " \
                                                             "DEF:temp=data/" + sensor.id + "/data.rrd:temperatur:AVERAGE " \
                                                             "LINE2:temp#FF0000 " \
                                                             "VDEF:tempmax=temp,MAXIMUM " \
                                                             "VDEF:tempmin=temp,MINIMUM " \
                                                             u"GPRINT:tempmax:\"Max  %6.2lf\" " \
                                                             u"GPRINT:tempmin:\"Min  %6.2lf\" "
            call(shlex.split(graph5_cmd))
