from rest_framework import serializers
from customertext.models import Customertext

class CustomertextSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customertext
        fields = "__all__"