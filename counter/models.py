from django.db import models

class CounterSnapshot(models.Model):
    counteredValue = models.IntegerField()

    
class CounterHistory(models.Model):
    value= models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
