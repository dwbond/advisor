from django import forms
from django.db import models
from django.core.exceptions import ValidationError
from trajectories.models import Trajectory

from haystack.forms import SearchForm

# searching
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

# WHERE ARE WE SETTING THE CATALOG YEAR?

# pick a new Major
# ModelForms fill out existing Models
class NewMajorForm( ModelForm ):
    class Meta:
        model = Major
        fields = ('name',
        )
        # does this work with the cbvs?
        exclude = ('slug', 'courseReqs', 'catalogYear', 'isCompleted',
            'degreeType',
        )
        labels = {
            'name' : 'Major(s)',
        }
        widgets = {
	    # name of major(s)
            'name' : forms.TextInput(attrs={
	        'class' : 'form-control',
		'placeholder' : 'Government and International Politics',
	    }),
        }

# pick a new Minor
class NewMinorForm( ModelForm ):
    class Meta:
        model = Minor
        fields = ('name',
        )
        exclude = ('slug', 'courseReqs', 'catalogYear', 'isCompleted',
            'degreeType',
        )
        labels = {
            'name' : 'Minor(s)',
        }
        widgets = {
            # name of minor(s)
            'name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Software Engineering',
            }),
        }

# build a trajectory
class BuildTrajectoryForm( ModelForm ):
    class Meta:
        model = Trajectory
        fields = ('name', 'courses',
        )
        exclude = ('slug', 'owner', 'completedCourses', 'whichPrograms',
        'isPublic', 'semester'
        )
        labels = {
        # the courses need to be sorted by their associated program, so idk labels
            'name' : 'Trajectory Name',
            'courses' : 'Courses You Can Take This Semester',
        }
        widgets = {
            # name of the trajectory
            # this should be generated automatically, e.g.
            # Daniel's Music Theory and Biology Minor v. 4 Trajectory
            'name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' = 'Name Your Trajectory',
            }),
            # users select and save tiles... don't use the widget
            'courses' : forms.SelectMultiple(attrs={
                'class' : 'form-control',
            }),
        }

class StudentUpdateForm( ModelForm ):
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
            'completedCourses' : forms.SelectMultiple(attrs={
                'class' : 'form-control',
            #    'placeholder' : 'Type in courses you\'ve taken',
            }),
            # is the student honors?
            'isHonors' : forms.CheckboxInput(attrs={
                'class' : 'form-control',
            }),
            # semester
            'semester' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'What year are you?'
            }),
        }
