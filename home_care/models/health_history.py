from django.db import models

from .patient import Patient


class HealthHistory(models.Model):
    marital_status = models.CharField(max_length=30)
    grade_level = models.CharField(max_length=30)
    occupation = models.CharField(max_length=30)
    patient = models.OneToOneField(Patient, on_delete=models.PROTECT, primary_key=True)
    born_city = models.CharField(max_length=30)
    patient_profile = models.CharField(max_length=30)
