from django.db import models
from django.utils import timezone

# Create your models here.

class JMembers(models.Model):
    name1_last = models.CharField(max_length=50)
    name1_first = models.CharField(max_length=50)
    date_created = models.DateTimeField(default=timezone.now)
