from django.urls import path
from . import views

urlpatterns = [
    path('page/', views.display_home),
    path('page/processed/', views.display_processed)
]