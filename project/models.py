from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(unique=True)
    question = models.CharField(max_length=50, choices=[
        ('Косметический ремонт', 'Косметический ремонт'),
        ('Капитальный ремонт', 'Капитальный ремонт'),
    ])
    comment = models.TextField()


    def __str__(self):
        return self.username
# Create your models here.
