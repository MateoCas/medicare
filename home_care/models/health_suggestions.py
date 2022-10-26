from django.db import models

from .patient import Patient


class HealthSuggestions(models.Model):
    id_health_suggestion = models.AutoField(primary_key=True)
    suggestion = models.CharField(max_length=250)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)

