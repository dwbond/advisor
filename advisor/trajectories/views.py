from django.shortcuts import render, get_object_or_404
from django.db.models import Max
from django.views.generic import *
from trajectories.models import Course, CourseCollection, Program, Student, Trajectory
from trajecgtories.utils import *

from braces.views import LoginRequiredMixin
# a page for creating new trajectories
# @login_required
def create_trajectory(LoginRequiredMixin, CreateView):
    model = Trajectory
    form = CreateTrajectoryForm

    #programs = Program.objects.all()
    #courses = Course.objects.all()
    # select year

# "Build"
def update_trajectory(LoginRequiredMixin, UpdateView):
    model = Trajectory
    form = UpdateTrajectoryForm

# student's page; shows saved trajectories
# @login_required

def detail_student(LoginRequiredMixin, DetailView):
    model = Student
    trajectories = Trajectory.objects.filter(student__user__username=username)
    topTrajectories = topTrajectories(trajectories)

# simply displays a page for the course
def detail_course(DetailView):
    model = Course

# simply returns a page showing a program
# @login_required
def detail_program(DetailView):
    model = Program

def detail_trajectory(LoginRequiredMixin, DetailView):
    model = Trajectory

def list_trajectory(LoginRequiredMixin, ListView):
    model = Trajectory

def list_program(ListView):
    model = Program

# simply displays a page for an individual trajectory, (along with edit links)
# @login_required
# actually needs more than one slug, the one for the user
