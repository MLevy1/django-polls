from django.contrib import admin

# Register your models here.
from .models import Activity, SubProj

admin.site.register(Activity)
admin.site.register(SubProj)
