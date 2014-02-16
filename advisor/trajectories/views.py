from django.shortcuts import render, get_object_or_404
from django.db.models import Max
from django.views.generic import *
from trajectories.models import Course, CourseCollection, Program, Student, Trajectory
from trajectories.utils import *

from braces.views import LoginRequiredMixin

# create a new trajectory
def newTrajectory(LoginRequiredMixin, CreateView):
    model = Trajectory
    form = NewMajorForm
    form = NewMinorForm

    # form processing
    # ensure that the student does not take more than two majors and three minors-- fix 'maxProgramsAllowed' in utils
    # PROGRAM: check if the student is Honors, and overwrite default degreeType to relevant Honors option -- fix 'getGenEds' in utils 
    # TRAJECTORY: with the name of the user and the name of the majors and minors, create a name
    # TRAJECTORY: create the slug from the name of the majors and minors
    # TRAJECTORY: set owner as user, and pull user's previous trajectories
    # TRAJECTORY: set whichPrograms to the programs passed in
    # TRAJECTORY: set semester as user's current semester
    # (?) where is catalogYear being set?
    # save and pass this information to buildTrajectory

# build the trajectory
def buildTrajectory(LoginRequiredMixin, UpdateView):
    model = Trajectory
    form = BuildTrajectoryForm

    # form processing

# student's page; shows saved trajectories
def studentDetail(LoginRequiredMixin, DetailView):
    model = Student

# student can edit their information, such as previous classes or isHonors
def studentUpdate(LoginRequiredMixin, UpdateView):
    models = Student
    form = StudentUpdateForm

# details of a course
def courseDetail(DetailView):
    model = Course

# details of a program
def programDetail(DetailView):
    model = Program

# details of a program
def trajectoryDetail(LoginRequiredMixin, DetailView):
    model = Trajectory

# lists all of  your trajectories
def trajectoryList(LoginRequiredMixin, ListView):
    model = Trajectory
    # needs to make it so it's only your trajectories
    # or eventually, public as well

# lists all programs
def programList(ListView):
    model = Program
