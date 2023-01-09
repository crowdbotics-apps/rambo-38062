from rest_framework import authentication
from presender.models import Presender
from .serializers import PresenderSerializer
from rest_framework import viewsets

class PresenderViewSet(viewsets.ModelViewSet):
    serializer_class = PresenderSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Presender.objects.all()