from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<id>/', views.UserDetail.as_view()),
    path('documents/', views.DocumentList.as_view()),
    path('logs/', views.log_list)
]