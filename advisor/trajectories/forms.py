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

    # needs to connect with a Student's completedCourses field

    # class Meta:
        # models = Course

	# widgets = {
	    # department abbreviation

	    # course number

	    # name
        # }

class NewTrajectoryForm( ModelForm ):
    # def __init__(self, *args, **kwargs):

    class Meta:
        model = Program
        fields = ('name',
        )
        exclude = ('courseReqs', 'created', 'last_modified', 'catalogYear',
	    'isCompleted', 'programType', 'degreeType',
        )
        labels = {
            'name' : 'Select your Majors'
            #'name' : 'Select your Minor'
        }
        widgets = {
            # I know you can't actually have it assigned twice...
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
    # def __init__(self, *args, **kwargs):

# the user selects the courses they are allowed to take but
# this needs to be presented in a dramatically different way than
# just some silly dropdown
    class Meta:
        model = Trajectory
        fields = ('name', 'courses',
        )
        exclude = ('trajectorySlug', 'previousCourses', 'whichPrograms',
        'isPublic', 'semester'
        )
        labels = (
        # the courses need to be sorted by their associated program, so idk labels
        )
        widgets = {
            # name of the trajectory
            'name' : TextInput(attrs={
                'class' : 'form-control',
                # this shouldn't change often
                'placeholder' = 'Name Your Trajectory',
            }),
            # course names... this isn't probably right
            # users select and save tiles...
            'name' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' = 'Name Your Trajectory',
            }),
        }

class StudentInfoForm( ModelForm ):
    # def __init__(self, *args, **kwargs):

    class Meta:
        model = Student
        fields = ('completedCourses', 'isHonors', 'semester',
        )
        exclude = ('user', 'trajectories',
        )
        labels = {
            'completedCourses' : 'Completed Courses',
            'isHonors' : 'Are you in the Honors College?',
            'semester' : 'Semester',
        }
        widgets = {
            # this should be done above, but I don't know how that works with the models ^^^
            'completedCourses' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Type in courses you\'ve taken',
            }),
            # is the student honors?
            'isHonors' : CheckboxInput(attrs={
                'class' : 'form-control',
            }),

            # semester
            'semester' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'What year are you?'
            }),
        }
