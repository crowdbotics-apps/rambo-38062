from rest_framework import authentication
from vendadetail.models import Vendadetail
from .serializers import VendadetailSerializer
from rest_framework import viewsets

class VendadetailViewSet(viewsets.ModelViewSet):
    serializer_class = VendadetailSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Vendadetail.objects.all()