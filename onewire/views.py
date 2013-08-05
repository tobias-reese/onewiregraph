# Create your views here.
from django.views.generic.edit import CreateView
import json
from django.http.response import HttpResponse
from django.shortcuts import render
from onewire import api
from onewire.models import Sensor


def index(request):
    return render(request, 'index.html', {})

def last_scan(requetst):
    response = HttpResponse(json.dumps(api.last_scan()), content_type='application/json')
    return response

def scan(request):
    response = HttpResponse(json.dumps(api.scan()), content_type='application/json')
    return response

class SensorCreate(CreateView):
    model = Sensor
    fields = ['id', 'state', 'type']

    def get_initial(self):
        return {'id':self.kwargs['id']}