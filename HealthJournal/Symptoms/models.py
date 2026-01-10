from django.db import models

# Create your models here.
class symptom(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    file = models.FileField(null=True, blank=True)
    actions_taken = models.TextField(null=True, blank=True)
    vitals = models.TextField(null=True, blank=True)