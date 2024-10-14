from rest_framework import serializers
from .models import *
from .sms import send_sms

class TemperatureLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureLog
        fields = "__all__"

    def create(self, validated_data):
        
        instance = TemperatureLog.objects.create(**validated_data)
        send_sms()
        return super().create(validated_data)