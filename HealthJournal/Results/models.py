from django.db import models

# Create your models here.
class result(models.Model):
    title = models.CharField(max_length=255)
    values = models.TextField()
    file = models.FileField()
    