from django.db import models
from django import forms
import datetime


class API(models.Model):
    name = models.CharField(max_length=260)
    username = models.CharField(max_length=260)
    password = models.CharField(max_length=260)
    api_url = models.URLField(max_length=300, unique=True,
                              error_messages={'unique': "This API URL has already been registered."})
    expiration = models.DateField(default=datetime.datetime.now() + datetime.timedelta(days=183))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
