from django.db import models

# Create your models here.

class OseroPanel(models.Model):
    file = models.FileField(upload_to='')
