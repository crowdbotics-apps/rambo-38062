from rest_framework import serializers
from myschedule.models import Myshedule

class MysheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Myshedule
        fields = "__all__"