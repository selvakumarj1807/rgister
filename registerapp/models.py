from django.db import models

# Create your models here.
# user_management/models.py

from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return self.username
