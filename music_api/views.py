from rest_framework import viewsets


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