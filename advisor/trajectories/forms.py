from django import forms
from django.db import models
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Select
from trajectories.models import Trajectory

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
