from django.db import models


class Role(models.Model):
    id_rol = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=30)
