from datetime import datetime
from django.db import models


# Create your models here.

# for room name  
class Room(models.Model):
    name = models.CharField(max_length=1000)
    
# for messages storing and timing
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
