from django import forms
from django.core import validators
from . import models


class ClueForm(forms.Form):
    answer = forms.CharField(required=True)
