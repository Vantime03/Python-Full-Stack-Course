from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from equipment.models import Equipment

class Transaction(models.Model):
    equipment_id = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    borrower_id = models.ForeignKey(User, on_delete=models.CASCADE)
    checkout_date_time = models.DateTimeField(default = timezone.now() + timezone.timedelta(hours=6))
    checkin_date_time = models.DateTimeField(blank = True, null = True)
    total_cost = models.DecimalField(max_digits=6, decimal_places=2, blank = True, null = True)
    confirmation_code = models.CharField(max_length=9, blank = True, null = True)
    

    def __str__(self):
        return str(self.equipment_id)


    
