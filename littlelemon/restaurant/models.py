from django.db import models


# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField(default=10)
    booking_date = models.DateField()

    def __str__(self): 
        return self.first_name


# Add code to create Menu model
class Menu(models.Model):
   title = models.CharField(max_length=255) 
   price = models.DecimalFieldField() 
   inventory = models.SmallIntegerField(max_digits=10, decimal_places=2) 

   def __str__(self):
      return f'{self.title} : {str(self.price)}'
