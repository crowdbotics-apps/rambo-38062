from rest_framework import serializers
from homepage.models import Homepage

class HomepageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Homepage
        fields = "__all__"