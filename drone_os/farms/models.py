from django.db import models

# Create your models here.
class Farm(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)