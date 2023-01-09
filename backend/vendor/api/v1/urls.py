
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import VendorViewSet
router = DefaultRouter()
router.register('vendor', VendorViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
