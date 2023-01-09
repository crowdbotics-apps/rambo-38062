
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ScheduleViewSet
router = DefaultRouter()
router.register('schedule', ScheduleViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
