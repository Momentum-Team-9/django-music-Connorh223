from django import forms
from django.db import models
from django.db.models import fields
from .models import Albums, Tracks

class AlbumsForm(forms.ModelForm):
    class Meta:
        model = Albums
        fields = [
            'title',
            'artist',
            'release_year',
            'photo',
        ]

# class TracksForm(forms.ModelForm):
#     class Meta:
#         model = Tracks
#         fields = [
            
#         ]