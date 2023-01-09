
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import HomepageViewSet
router = DefaultRouter()
router.register('homepage', HomepageViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
