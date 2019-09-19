import os

from rest_framework import viewsets
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST


from .serializers import MusicSerializer
from .models import Music

class MusicViewSet(viewsets.ModelViewSet):

    serializer_class = MusicSerializer

    def get_queryset(self):

        arguments = {}
        for k, v in self.request.query_params.items():
            if v:
                arguments[k] = v
        queryset = Music.objects.filter(**arguments)

        return queryset

def handle_uploaded_file(f, f_name):
    with open(os.path.join(settings.MEDIA_ROOT, f_name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@require_POST
def upload_file(request):
    handle_uploaded_file(request.FILES['file'], request.FILES['file'].name)
    return JsonResponse({'status': 204})