from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=150)
    des=models.ImageField()
class Ticket(models.Model):
    visitor_name = models.CharField(max_length=100)
    checkin = models.DateField()
    image = models.ImageField(upload_to='ticket_images/')