import datetime
from time import sleep
from celery import shared_task
from .serializers import CounterHistorySerializer
from .models import CounterSnapshot
from django.utils import timezone


def add_to_counter(amount=0):
    try:
        counter = CounterSnapshot.objects.latest('counteredValue')
    except CounterSnapshot.DoesNotExist:
        counter = CounterSnapshot(counteredValue=0) 
    counter.counteredValue += amount
    counter.save()
    
    
@shared_task
def store_counter_history():
    try:
        latest_snapshot= CounterSnapshot.objects.latest('id')
    except CounterSnapshot.DoesNotExist:
        pass
    new_history_record = {
        'value': latest_snapshot.counteredValue,
        'timestamp': timezone.now()
    }

    history_serializer = CounterHistorySerializer(data=new_history_record)

    if history_serializer.is_valid():
        history_serializer.save()
    
    
    
    






