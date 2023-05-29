from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    regNo = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    role = models.CharField(max_length=80)

class Stock(models.Model):
    itemName = models.CharField(max_length=80)
    description = models.CharField(max_length=200) 
    quantity = models.IntegerField()

class Borrow(models.Model):
    orderNo = models.IntegerField()
    projectName = models.CharField(max_length=80)
    projectDescription = models.CharField(max_length=200)
    email = models.CharField(max_length=80)
    requestDate = models.CharField(max_length=80)
    borrowDate = models.CharField(max_length=80)
    returnDate = models.CharField(max_length=80)
    status = models.CharField(max_length=80)

class Orders(models.Model):
    orderNo = models.IntegerField()
    itemName = models.CharField(max_length=80)
    quantity = models.IntegerField()