from rest_framework import serializers
from .models import CounterSnapshot,CounterHistory


class CounterSnapshortSerializer(serializers.ModelSerializer):
    class Meta:
        model = CounterSnapshot
        fields = ['id','counteredValue']


class CounterHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model= CounterHistory
        fields=['id','value','timestamp']

