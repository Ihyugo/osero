from django.db import models

# Create your models here.

class OseroPanel(models.Model):
    file = models.FileField(upload_to='')

class Book(models.Model):
    panel = models.IntegerField(primary_key=True)

class AllPanel(models.Model):
    allpanel = models.CharField(max_length=100)
