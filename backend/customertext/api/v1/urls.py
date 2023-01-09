
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CustomertextViewSet
router = DefaultRouter()
router.register('customertext', CustomertextViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
