from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list),
    path('users/<id>/', views.user_detail),
    path('documents/', views.document_list),
    path('logs/', views.log_list)
]