from django.contrib import admin
from .models import Music, Contributor, Provider

# Register your models here.

admin.site.register(Music)
admin.site.register(Contributor)
admin.site.register(Provider)
