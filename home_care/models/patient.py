from django.db import models

from .person import Person


class Patient(models.Model):
    city = models.CharField(max_length=30)
    birthday = models.CharField(max_length=30)
    person = models.OneToOneField(Person, on_delete=models.PROTECT, primary_key=True)

