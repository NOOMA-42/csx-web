from django.db import models

# Create your models here.

class Account(models.Model):
    account = models.CharField(max_length=18, unique=True, blank=False)
    password = models.CharField(max_length=18, unique=True, blank=False)

    def __str__(self):
        return self.title