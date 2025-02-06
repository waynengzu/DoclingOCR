from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<pk>/', views.UserDetail.as_view()),
    path('documents/', views.DocumentList.as_view()),
    path('documents/<pk>/', views.DocumentDetail.as_view()),
    path('logs/', views.LogList.as_view()),
    path('logs/<pk>/', views.LogDetail.as_view())
]