from rest_framework import authentication
from vendor.models import Vendor
from .serializers import VendorSerializer
from rest_framework import viewsets

class VendorViewSet(viewsets.ModelViewSet):
    serializer_class = VendorSerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Vendor.objects.all()