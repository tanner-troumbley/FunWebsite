from django import forms
from .models import API

class API_form(forms.ModelForm):
    class Meta:
        model = API
        fields = "__all__"
