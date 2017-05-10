from django.db import models
from datetime import datetime

class Disaster(models.Model):
    date = models.DateTimeField(default=datetime.now)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    deceases = models.IntegerField()
    material_losses = models.IntegerField()


    def __str__(self):
        return self.name

    class Meta:
        ordering = ('date',)
