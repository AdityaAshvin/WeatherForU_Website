from django.db import models

# Create your models here.

class CityName(models.Model):
    name = models.CharField(max_length=122)

    def __str__(self):
        return self.name