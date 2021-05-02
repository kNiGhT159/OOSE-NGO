from django.apps import AppConfig
from django.contrib import admin
from .models import Tinfo, Sinfo

admin.site.register(Tinfo)
admin.site.register(Sinfo)

# Register your models here.
