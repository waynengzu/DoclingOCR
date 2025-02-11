from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('documents', views.DocumentViewSet)
router.register('logs', views.LogViewSet)
router.register('uploads', views.UploadViewSet)
router.register('OCRs', views.OCRViewSet)

urlpatterns = router.urls