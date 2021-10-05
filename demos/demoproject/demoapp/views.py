from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from .models import Place,People


def fun(request):
    obj = Place.objects.all()


    obj1= People.objects.all()
    return render(request, 'index.html', {'result': obj,'lab':obj1})
