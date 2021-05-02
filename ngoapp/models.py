from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator , MinValueValidator

class Tinfo(models.Model):
    Name = models.CharField(max_length=255)
    Password = models.CharField(max_length=20)
    Email = models.EmailField(unique=True)
    PhoneNo = models.CharField(max_length=12)
    Address = models.CharField(max_length=1000)


class Sinfo(models.Model):
    Name = models.CharField(max_length=255)
    Password = models.CharField(max_length=20)
    Email = models.EmailField()
    ParNo = models.CharField(max_length=12)
    Std = models.CharField(max_length=5)

class Announcement(models.Model):
    teacher_email=models.EmailField(null=True)
    heading=models.CharField(max_length=100)
    body=models.CharField(max_length=300)
    expires_on=models.DateField()