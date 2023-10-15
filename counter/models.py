from django.db import models

class CounterSnapshot(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
