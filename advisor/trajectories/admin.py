from django.contrib import admin
from trajectories.models import Course, CourseCollection, Program, Student, Trajectory

from django.contrib.auth.models import User

from django.forms import CheckboxSelectMultiple

# Register your models here.
admin.site.register(Course)
admin.site.register(CourseCollection)
admin.site.register(Program)
admin.site.register(Student)
admin.site.register(Trajectory)
