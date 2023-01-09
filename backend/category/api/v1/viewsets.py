from rest_framework import authentication
from category.models import Category
from .serializers import CategorySerializer
from rest_framework import viewsets

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    authentication_classes = (authentication.SessionAuthentication, authentication.TokenAuthentication)
    queryset = Category.objects.all()