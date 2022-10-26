from django.db import models

from .patient import Patient


class VitalSigns(models.Model):
    blood_pressure = models.CharField(max_length=30)
    respiration_rate = models.CharField(max_length=30)
    pulse_rate = models.CharField(max_length=30)
    id_vital_sign = models.AutoField(primary_key=True)
    body_temperature = models.CharField(max_length=30)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
