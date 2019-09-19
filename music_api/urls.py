from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'api', views.MusicViewSet, basename='api')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('music/', include(router.urls)),
    path('upload_file/', views.upload_file),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]