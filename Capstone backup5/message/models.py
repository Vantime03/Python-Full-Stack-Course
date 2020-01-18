from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from equipment.models import Equipment
from django.urls import reverse

class Message(models.Model):
    subject = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    created_date = models.DateTimeField(default=timezone.now)
    received_date = models.DateTimeField(null = True, blank = True)
    sender = models.ForeignKey(User, on_delete = models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete = models.CASCADE, related_name='receiver') 
    equipment = models.ForeignKey(Equipment, on_delete = models.CASCADE, related_name='equipment', null = True)
    
    def __str__(self):
        return self.subject


    
