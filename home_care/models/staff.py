from django.db import models

from .person import Person


class Staff(models.Model):
    record = models.CharField(max_length=30)
    speciality = models.CharField(max_length=30)
    person = models.OneToOneField(Person, on_delete=models.PROTECT, primary_key=True)

