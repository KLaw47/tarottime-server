from django.db import models

class ReadingCard(models.Model):
    card_id = models.ForeignKey("Card", on_delete=models.CASCADE)
    reading_id = models.ForeignKey("Reading", on_delete=models.CASCADE)
