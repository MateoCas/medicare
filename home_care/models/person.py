from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    adress_personal = models.CharField(max_length=150)
    phone_number = models.IntegerField()
    identification = models.CharField(max_length=30, primary_key=True)
    active = models.BooleanField()
