from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class GeneMember(models.Model):
    name1_last = models.CharField(max_length=50)
    name1_first = models.CharField(max_length=50)
    name2_last = models.CharField(max_length=50)
    name2_first = models.CharField(max_length=50)
    nationality = models.CharField(max_length=3)
    gender = models.CharField(max_length=1)
    bdate = models.DateField(blank=True, null=True)
    date_created =models.DateTimeField(default=timezone.now)

class MyFamilyStory(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content1 = models.TextField()
    content2 = models.TextField()
    date_created = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)




    # class Post(models.Model):
        # title = models.CharField(max_length=100)
        # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        # text = models.TextField()
        # date_created = models.DateTimeField(default=timezone.now)
        # date_published = models.DateTimeField(blank=True, null=True)

        # def publish(self):
            # self.date_published = timezone.now()
            # self.save()

        # def __str__(self):
            # return self.title
