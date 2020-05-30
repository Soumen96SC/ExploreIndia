

# Create your models here.
from django.db import models
class Destination(models.Model):
     
    name = models.CharField(max_length=100)
    desc = models.TextField()
    des1 =models.TextField()
    img = models.ImageField(upload_to='pic/')
class Ppd(models.Model):
    names = models.CharField(max_length=100)
    places = models.IntegerField()
    img = models.ImageField(upload_to='pic/')
class Hotels(models.Model):
    location = models.CharField(max_length=100)
    hotel_name = models.CharField(max_length=100)
    cost= models.IntegerField()
    addrss = models.TextField()
    hotel_img = models.ImageField(upload_to='pic/')     

# class BookingHistory(models.Model):
#     bookperson = models.CharField(max_length=50)
#     username = models.CharField(max_length=36)
#     bookdate = models.DateField()
#     paymentAmount = models.DecimalField(max_digits=8,decimal_places=2)
#     paymentCardNo = models.CharField(max_length=16)
#     companyName = models.CharField(max_length=30, default='company')
#     location = models.CharField(max_length=30, default='location')
#     check_in =  models.DateField()
#     check_out =  models.DateField()
#     bookingday = models.DateField()

class TransactionHistory(models.Model):
    bookperson = models.CharField(max_length=50)
    username = models.CharField(max_length=36)
    bookdate = models.DateField()
    paymentAmount = models.DecimalField(max_digits=8,decimal_places=2)
    paymentCardNo = models.CharField(max_length=16)
    companyName = models.CharField(max_length=30, default='company')
    location = models.CharField(max_length=30, default='location')
    check_in =  models.DateField(blank=True, null=True)
    check_out =  models.DateField(blank=True, null=True)
    cancel_Id = models.CharField(max_length=50, blank = True)
    bookingId = models.CharField(max_length= 50, blank= True)
    cancelled = models.BooleanField(default=False)
    dummy_check_in =  models.DateField(blank=True, null=True)
    dummy_check_out =  models.DateField(blank=True, null=True)

    
