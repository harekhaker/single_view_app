from django.contrib import admin
from .models import Music, Contributor, Source, Title

# Register your models here.

admin.site.register(Music)
admin.site.register(Contributor)
admin.site.register(Source)
admin.site.register(Title)
