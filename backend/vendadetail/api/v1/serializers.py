from rest_framework import serializers
from vendadetail.models import Vendadetail

class VendadetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vendadetail
        fields = "__all__"