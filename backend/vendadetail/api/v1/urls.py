
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import VendadetailViewSet
router = DefaultRouter()
router.register('vendadetail', VendadetailViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
