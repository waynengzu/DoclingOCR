from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<id>/', views.UserDetail.as_view()),
    path('documents/', views.document_list),
    path('logs/', views.log_list)
]