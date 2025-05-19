from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse
from .models import Department

# Create your views here.

def homeView(request):
    template = loader.get_template('home.html')
    context = {
        'departments' : Department.objects.all()
    }
    return HttpResponse(template.render(context, request))
