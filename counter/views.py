import datetime
from .models import CounterSnapshot
from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .tasks import add_to_counter
from rest_framework.views import APIView
from .serializers import CounterSnapshortSerializer



class incrementCounterView(APIView,):
    def post(self, request):
        serializer = CounterSnapshortSerializer(data=request.data)
        if serializer.is_valid():
            amount = serializer.validated_data.get('value')
            condition_met = True 
            if condition_met:
                add_to_counter(amount)                
                return Response({"message": "Task queued for incrementing the counter."}, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"message": "Condition not met. Counter not incremented."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        values = CounterSnapshot.objects.all()
        serializer = CounterSnapshortSerializer(values,many=True)
        return Response(serializer.data)
    




        
class CounterHistoryView(generics.ListAPIView):
    queryset = CounterSnapshot.objects.all()
    serializer_class = CounterSnapshortSerializer


