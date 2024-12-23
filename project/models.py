from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    question = models.CharField(max_length=255)
    comment = models.TextField()

# Create your models here.
