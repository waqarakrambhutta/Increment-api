from rest_framework import serializers
from .models import CounterSnapshot


class CounterSnapshortSerializer(serializers.ModelSerializer):
    class Meta:
        model = CounterSnapshot
        fields = ['id','value','timestamp']
    

