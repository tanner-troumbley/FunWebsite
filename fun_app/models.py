from django.db import models
from django import forms
import datetime


class API(models.models):
    name = models.CharField()
    username = models.CharField()
    password = models.CharField(widget=forms.PasswordInput)
    api_url = models.URLField(max_length=300, unique=True, error_messages={'unique': "This API URL has already been registered."})
    expiration = models.DateField(default=datetime.date.now + datetime.timedelta(days=183))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
