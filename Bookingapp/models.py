from django.db import models

# Create your models here.
class Booking(models.Model):
    customername = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    phonenumber = models.IntegerField(("30"))
    email = models.CharField(max_length = 255)
