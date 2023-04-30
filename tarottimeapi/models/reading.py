from django.db import models

class Reading(models.Model):
  user_id = models.ForeignKey("User", on_delete=models.CASCADE)
  ques = models.CharField(max_length=50)
  answer = models.CharField(max_length=50)
