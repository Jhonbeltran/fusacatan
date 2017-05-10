from django.db import models
from datetime import datetime

class Zone(models.Model):
    date = models.DateTimeField(default=datetime.now)
    location = models.CharField(max_length=255)
    moisture = models.DecimalField(max_digits=6, decimal_places=2)
    rainfall = models.DecimalField(max_digits=6, decimal_places=2)
    trees =  models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return self.location

    class Meta:
        ordering = ('date',)

