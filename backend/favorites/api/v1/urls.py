
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import FavortiesViewSet
router = DefaultRouter()
router.register('favorties', FavortiesViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
