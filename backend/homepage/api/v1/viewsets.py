from rest_framework import authentication
from homepage.models import Homepage
from .serializers import HomepageSerializer
from rest_framework import viewsets

class HomepageViewSet(viewsets.ModelViewSet):
    serializer_class = HomepageSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Homepage.objects.all()