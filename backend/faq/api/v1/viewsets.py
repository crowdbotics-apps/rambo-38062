from rest_framework import authentication
from faq.models import Faq
from .serializers import FaqSerializer
from rest_framework import viewsets

class FaqViewSet(viewsets.ModelViewSet):
    serializer_class = FaqSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Faq.objects.all()