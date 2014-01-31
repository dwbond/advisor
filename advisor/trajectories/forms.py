from django import forms
from django.db import models
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Select
from trajectories.models import Trajectory

from haystack.forms import SearchForm

class StyledSeachForm( SearchForm ):
    q = forms.CharField(
        required = False,
	label = 'Search',
	widget = forms.TextInput(attrs={
	    'class' : 'form-control',
	    'placeholder' : 'Search',
	    'autofocus' : 'autofocus',
        }),
    )

class NewTrajectoryForm( ModelForm ):
    # def __init__(self, *args, **kwargs):

    class Meta:
        model = Trajectory
        fields = (
        )
        exclude = (
        )
        labels = {
        }
        widgets = {
        }
