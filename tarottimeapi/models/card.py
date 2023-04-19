from django.db import models

class Event(models.Model):
    type = models.CharField(max_length=50)
    name_short = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    meaning_up = models.CharField(max_length=100)
    meaning_rev = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    suit = models.CharField(max_length=50, null=True, blank=True)
