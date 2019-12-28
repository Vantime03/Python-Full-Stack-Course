from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Equipment(models.Model):
    model_number = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=200)
    tool_name = models.CharField(max_length=100, default='Hand Tools')
    description = models.TextField()
    rent_cost = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    # tool_type = 

    def __str__(self):
        return self.tool_name