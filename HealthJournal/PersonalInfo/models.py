from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class info(models.Model):
    name = models.CharField(max_length=256)
    fname = models.CharField(max_length=256)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    activity_level = models.IntegerField()
    nutrition_preferences = models.TextField(null=True, blank=True)
    medical_conditions = models.TextField(null=True, blank=True)
