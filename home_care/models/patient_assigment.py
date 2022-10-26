from django.db import models

from .person import Person
from .patient import Patient


class PatientAssigment(models.Model):
    id_patient_assigment = models.AutoField(primary_key=True)
    patient_relation = models.CharField(max_length=30)
    assigment_staff = models.ForeignKey(Person, on_delete=models.PROTECT)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
    active = models.BooleanField()
