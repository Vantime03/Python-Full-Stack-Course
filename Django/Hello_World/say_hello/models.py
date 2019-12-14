from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class  Borrower(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    mailing_address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)

    def __str__(self):
        return self.firstname + " " + self.lastname

class Equipment(models.Model):
    modelnumber = models.CharField(max_length=50)
    serialnumber = models.CharField(max_length=50)
    ToolType = models.CharField(max_length=30)
    borrowerid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rentcost = models.FloatField
    availabe = models.BooleanField



