from rest_framework import authentication
from myschedule.models import Myshedule
from .serializers import MysheduleSerializer
from rest_framework import viewsets

class MysheduleViewSet(viewsets.ModelViewSet):
    serializer_class = MysheduleSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Myshedule.objects.all()