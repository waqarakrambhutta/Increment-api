import datetime
from .models import CounterSnapshot,CounterHistory
from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .tasks import add_to_counter
from rest_framework.views import APIView
from .serializers import CounterSnapshortSerializer,CounterHistorySerializer
from rest_framework import viewsets



class incrementCounterView(APIView):
    def post(self, request):
        serializer = CounterSnapshortSerializer(data=request.data)
        if serializer.is_valid():
            amount = serializer.validated_data.get('counteredValue')
            add_to_counter(amount)                
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        values = CounterSnapshot.objects.all()
        serializer = CounterSnapshortSerializer(values,many=True)
        return Response(serializer.data)
    
    
class CounterHistoryView(viewsets.ModelViewSet):
    queryset = CounterHistory.objects.all()
    serializer_class = CounterHistorySerializer
    
