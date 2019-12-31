from django import forms
from .models import short_URL

class UrlForm(forms.ModelForm):
    class Meta:
        model = short_URL
        fields = ['long_url']