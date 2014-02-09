from django.shortcuts import render, get_object_or_404
from django.db.models import Max
from django.views.generic import *
from trajectories.models import Course, CourseCollection, Program, Student, Trajectory
from trajecgtories.utils import *

from braces.views import LoginRequiredMixin

# create a new trajectory
def NewTrajectory(LoginRequiredMixin, CreateView):
    model = Trajectory
    form = CreateTrajectoryForm

# build the trajectory
def BuildTrajectory(LoginRequiredMixin, UpdateView):
    model = Trajectory
    form = BuildTrajectoryForm

# student's page; shows saved trajectories
def StudentDetail(LoginRequiredMixin, DetailView):
    model = Student

# student can edit their information, such as previous classes or isHonors
def StudentUpdate(LoginRequiredMixin, UpdateView):
    models = Student
    form = StudentUpdateForm

# details of a course
def CourseDetail(DetailView):
    model = Course

# details of a program
def ProgramDetail(DetailView):
    model = Program

# details of a program
def TrajectoryDetail(LoginRequiredMixin, DetailView):
    model = Trajectory

# lists all of  your trajectories
def TrajectoryList(LoginRequiredMixin, ListView):
    model = Trajectory
    # needs to make it so it's your trajectory
    # or eventually, public as well

# lists all programs
def ProgramList(ListView):
    model = Program
