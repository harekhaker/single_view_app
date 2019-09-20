from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'music', views.MusicViewSet, basename='music')
router.register(r'generate_report', views.MusicCSVViewSet, basename='music_csv')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('upload_file/', views.upload_file),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]