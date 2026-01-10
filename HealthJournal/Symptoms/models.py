from django.db import models

# Create your models here.
class symptom(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    actions_taken = models.TextField(null=True, blank=True)
    vitals = models.TextField(null=True, blank=True)

class journal(models.Model):
    entry = models.TextField(null=True, blank=True)