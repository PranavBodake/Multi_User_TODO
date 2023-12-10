from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TODO(models.Model):

    staus_choices = [
        ('Completed', 'COMPLETED'),
        ('Pending', 'PENDING')
    ]

    title = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices = staus_choices)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

