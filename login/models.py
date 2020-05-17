from django.db import models
from django.views.generic import ListView

# Create your models here.

class HMember(models.Model):
    name_hml = models.CharField(max_length=50)
    name_hmf = models.CharField(max_length=50)
    HMLEVEL = (
        ('1', 'Normal'),
        ('2', 'Blacklist'),   # 1) registering w/ fake info. 2) cannot be contacted for 14 days.
        ('3', 'force out'),   # against rule
    )
    hmlevel = models.SmallIntegerField(choices=HMLEVEL)
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER)
    email = models.EmailField()
    passwd = models.CharField(max_length=20)
