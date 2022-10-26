from django.db import models

from .person import Person
from .role import Role


class User(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    person = models.OneToOneField(Person, on_delete=models.PROTECT, primary_key=True)
    roles = models.ManyToManyField(Role)
