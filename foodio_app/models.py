from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)  
    mobile = models.CharField(max_length=15)  
    email = models.EmailField() 
    person_count = models.IntegerField(max_length=3) 

    def __str__(self):
        return self.name  # This is used to display the reservation's name in admin and other contexts