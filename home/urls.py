from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import get_latest_json, save_json, latest_upload

urlpatterns = [
    path('page/', views.display_index),
    path('analyzed/', views.display_analyze),
    path('latest-json/', get_latest_json, name='latest-json'),
    path('save-json/', save_json, name='save-json'),
    path('latest-upload/', latest_upload, name='latest-upload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)