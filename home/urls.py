from django.urls import path
from . import views

urlpatterns = [
    path('page/', views.display_index),
    path('processed/', views.display_process),

]