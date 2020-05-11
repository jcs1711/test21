from django.db import models
from django.utils import timezone

# Create your models here.

class Executives(models.Model):
    position = models.CharField(max_length=15)
    date_created = models.DateTimeField(default=timezone.now)