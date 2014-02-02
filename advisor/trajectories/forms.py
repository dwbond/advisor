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

# class SelectYourCourses( ModelForm ):

    # class Meta:
        # models = Course

	# widgets = {
	    # department abbreviation

	    # course number

	    # name

class NewTrajectoryForm( ModelForm ):
    # def __init__(self, *args, **kwargs):

    class Meta:
        model = Program
        fields = ('name', 'degreeType', 'programType', 'isHonors',
        )
        exclude = ('courseReqs', 'created', 'last_modified', 'catalogYear',
	    'isCompleted',
        )
        widgets = {
	    # name of major(s)
            'name' : TextInput(attrs={
	        'class' : 'form-control',
		'placeholder' : 'Government and International Politics',
	    }),
            # name of minor(s)
            'name' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' = 'Software Engineering',
            }),
        }

# class CreateTrajectoryForm ( ModelForm ):

# class StudentInfoForm( ModelForm ):
