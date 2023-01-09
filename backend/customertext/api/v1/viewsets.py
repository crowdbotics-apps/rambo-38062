from rest_framework import authentication
from customertext.models import Customertext
from .serializers import CustomertextSerializer
from rest_framework import viewsets

class CustomertextViewSet(viewsets.ModelViewSet):
    serializer_class = CustomertextSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Customertext.objects.all()