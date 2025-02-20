from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('page/', views.display_index),
    path('processed/', views.display_process),
    path('analyzed/', views.display_analyze),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)