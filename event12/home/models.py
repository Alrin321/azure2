from django.db import models
from django.db import models



class User_Details(models.Model):
    
     username=models.CharField(max_length=30)
     password=models.CharField(max_length=20)
     mobile=models.IntegerField()
     semester=models.CharField(max_length=10)
     email=models.CharField(max_length=10)
     registeredevent=models.ImageField(upload_to='pics')
     class Meta:
        verbose_name_plural="User_Details"

class EventDetails(models.Model):
    
    eventtitle=models.CharField(max_length=20)
    Date=models.DateField()
    Time=models.CharField(max_length=20)
    Location=models.CharField(max_length=20,default='college')
    max_no_participants=models.IntegerField()
    Description=models.TextField(max_length=20)
    eventbanner=models.ImageField(upload_to='pics')
    def __str__(self):
        return self.eventtitle
    class Meta:
        verbose_name_plural="EventDetails"

class event_registrations(models.Model):
    event = models.ForeignKey(EventDetails, on_delete=models.CASCADE)
    user = models.ForeignKey(User_Details, on_delete=models.CASCADE)
