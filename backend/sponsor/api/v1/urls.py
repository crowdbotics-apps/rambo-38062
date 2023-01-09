
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import SponsorViewSet
router = DefaultRouter()
router.register('sponsor', SponsorViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
