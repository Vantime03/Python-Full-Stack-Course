from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse



class Equipment(models.Model):
    model_number = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=200)
    tool_name = models.CharField(max_length=100, default='Hand Tools')
    description = models.TextField()
    rent_cost = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    image1 = models.ImageField(default='default1.png', upload_to='equipment_pics')
    image2 = models.ImageField(default='default1.png', upload_to='equipment_pics')
    image3 = models.ImageField(default='default1.png', upload_to='equipment_pics')

    #this will resize the the image to 300px by 300px
    def save(self):
        super().save()

        img1 = Image.open(self.image1.path)
        img2 = Image.open(self.image2.path)
        img3 = Image.open(self.image3.path)

        if img1.height > 300 or img1.width > 300:
            output_zize = (300, 300) 
            img1.thumbnail(output_zize)
            img1.save(self.image1.path )

        if img2.height > 300 or img2.width > 300:
            output_zize = (300, 300) 
            img2.thumbnail(output_zize)
            img2.save(self.image2.path )

        if img3.height > 300 or img3.width > 300:
            output_zize = (300, 300) 
            img3.thumbnail(output_zize)
            img3.save(self.image3.path )

    # tool_type = 

    def __str__(self):
        return self.tool_name

    def get_absolute_url(self):
        return reverse('equipment-detail', kwargs={'pk': self.pk})

    
