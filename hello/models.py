from django.db import models

# Create your models here.

class game(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False)

    def __game__(self):
        return self.name


