from django.db import models
from django.contrib.auth.models import User



class UserDetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)



class DonateContact(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name =  models.CharField(max_length=70)
    email = models.EmailField(max_length=100 )
    phone = models.CharField(max_length=50)


class Contact(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name =  models.CharField(max_length=70)
    email = models.EmailField(max_length=100 )
    phone = models.CharField(max_length=50)
    message =  models.TextField()



class Donation(models.Model):
    mode = (
        ('Paypal','Paypal'),
    )
    category= (
        ('Education','Education'),
        ('Nutrition','Nutrition'),
        ('Cloth','Cloth')
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField( max_length=200, null = True, default= 0 )
    payment_id = models.CharField(max_length=100, null=True, blank=True)
    payment_method = models.CharField(max_length=100, choices=mode)
    Category = models.CharField(max_length=100, choices=category)
    place = models.CharField(max_length=100) 



class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.TextField()
