
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import PresenderViewSet
router = DefaultRouter()
router.register('presender', PresenderViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
