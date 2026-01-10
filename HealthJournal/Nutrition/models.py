from django.db import models

# Create your models here.
class nutrition(models.Model):
    title = models.CharField(max_length=100)
    food_drink = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(null=True, blank=True)
    