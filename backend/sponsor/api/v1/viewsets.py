from rest_framework import authentication
from sponsor.models import Sponsor
from .serializers import SponsorSerializer
from rest_framework import viewsets

class SponsorViewSet(viewsets.ModelViewSet):
    serializer_class = SponsorSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Sponsor.objects.all()