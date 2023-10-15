# tasks.py
import datetime
from time import sleep
from celery import shared_task
from .models import CounterSnapshot
from django.utils import timezone


@shared_task
def add_to_counter(amount):
    try:
        counter = CounterSnapshot.objects.latest('timestamp')
    except CounterSnapshot.DoesNotExist:
        counter = CounterSnapshot(value=0) 
    counter.value += amount
    timestamp = timezone.now().strftime("%Y-%m-%d %H:%M")
    CounterSnapshot.objects.create(value=counter.value,timestamp=timestamp)
    counter.save()
    






