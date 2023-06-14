from django.db import models
from django.contrib import admin


class Metrics(models.Model):
    time = models.DateTimeField(null=True, blank=True)
    voltage = models.IntegerField(null=True, blank=True)
    current = models.IntegerField(null=True, blank=True)


admin.site.register(Metrics)
