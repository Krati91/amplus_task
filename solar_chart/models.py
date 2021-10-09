from django.db import models

# Create your models here.

PARAMETER_CHOICES = [
    ('generation', 'generation'),
    ('irradiation', 'irradiation')
]


class SolarPlant(models.Model):
    plant_id = models.CharField(max_length=3)
    date = models.DateField()
    parameter = models.CharField(max_length=12, choices=PARAMETER_CHOICES)
    value = models.DecimalField(max_digits=15, decimal_places=5)
