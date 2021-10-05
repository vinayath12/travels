from django.shortcuts import render

# Create your views here.
from .models import work
def news(request):
    obj=work.objects.all()
    return render(request,'indexs.html',{'result':obj})