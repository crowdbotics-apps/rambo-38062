from rest_framework import serializers
from favorites.models import Favorties

class FavortiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorties
        fields = "__all__"