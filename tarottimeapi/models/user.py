from django.db import models

class Event(models.model):
    name = models.CharField(max_length=50)
    uid = models.CharField(max_length=50)
