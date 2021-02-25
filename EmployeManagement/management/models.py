from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.TextField()
    dob = models.DateField(blank=True, null=True)
    company = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name+" "+self.last_name
        

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    address = models.TextField()
    dob = models.DateField(blank=True, null=True)
    company = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name+" "+self.last_name