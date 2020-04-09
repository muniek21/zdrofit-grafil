from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import Class


def index(request):
    all_classes = Class.objects.all()
    template = loader.get_template('grafik/index.html')
    context = { 'all_classes': all_classes}
    return HttpResponse(template.render(context, request))
