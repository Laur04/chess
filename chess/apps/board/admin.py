from django.contrib import admin

# Register your models here.

from .models import Run, HarrisCorners

admin.site.register(Run)
admin.site.register(HarrisCorners)
