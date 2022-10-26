from django.db import models

from .health_history import HealthHistory


class HistoryRecord(models.Model):
    id_record = models.AutoField(primary_key=True)
    diagnostic = models.CharField(max_length=250)
    health_history = models.ForeignKey(HealthHistory, on_delete=models.PROTECT)
