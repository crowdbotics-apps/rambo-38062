from rest_framework import authentication
from favorites.models import Favorties
from .serializers import FavortiesSerializer
from rest_framework import viewsets

class FavortiesViewSet(viewsets.ModelViewSet):
    serializer_class = FavortiesSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Favorties.objects.all()