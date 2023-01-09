from rest_framework import serializers
from presender.models import Presender

class PresenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Presender
        fields = "__all__"