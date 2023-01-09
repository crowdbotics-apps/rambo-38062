from rest_framework import authentication
from schedule.models import Schedule
from .serializers import ScheduleSerializer
from rest_framework import viewsets

class ScheduleViewSet(viewsets.ModelViewSet):
    serializer_class = ScheduleSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Schedule.objects.all()