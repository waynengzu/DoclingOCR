from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('users', views.UserViewSet)
router.register('documents', views.DocumentViewSet)
router.register('logs', views.LogViewSet)

urlpatterns = router.urls