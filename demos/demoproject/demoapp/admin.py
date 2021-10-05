 #from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Place
admin.site.register(Place)
from .models import People
admin.site.register(People)