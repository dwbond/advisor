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
    # TRAJECTORY: set owner as user
    # TRAJECTORY: set user's completedCourses as Trajectory's completedCourses(?)
    # ^^ that seems unnecessary
    # TRAJECTORY: set whichPrograms to the programs passed in
    # TRAJECTORY: set semester as user's current semester
    # (?) where is catalogYear being set?
    # save and pass this information to buildTrajectory

# build the trajectory
def buildTrajectory(LoginRequiredMixin, UpdateView):
    model = Trajectory
    form = BuildTrajectoryForm

    # form processing
    # rewrite utils as necessary
    # -- if all CourseCollections of a Program are completed, mark program as completed
    # BLEH-- I feel like the original logic in utils might be a bit better: figure out what I was thinking -->> get all courses that have prereqs in the same list of already completed courses (lightbulb?), and if there are coreqs, that course must also have its prereqs fulfilled
    # remainingReqCourses-- Program's courseReqs (only iterate over completed=False-- add fulfilledReq to models.py) and Trajectory's completedCourses
    # allPrereqCoreq-- retrieve a list of all prereqs and coreqs of those courses
    # continue on until 
    # courses is the non-duplicated list of prereqs and coreqs

    # do this for each section (multiple forms??? D-:)
    # get gen eds-- gen eds are a separate category
    # if a section is completed, return a value to allow the template to display as such

    # enoughCourses-- if all requirements are fulfilled, check that there are 120 credits

    # submit, save as trajectory, and create a new trajectory with the new information-- the next node down on the tree-- saving completed courses **within** the trajectory, NOT back to student
    # (this information is cycled over until a student has completed all programs)

# student's page; shows saved trajectories
def studentDetail(LoginRequiredMixin, DetailView):
    model = Student

# student can edit their information, such as previous classes or isHonors
def studentUpdate(LoginRequiredMixin, UpdateView):
    models = Student
    form = StudentUpdateForm

    # form processing

    # note: show merely the names of the trajectories-- pulling up the end nodes shouldn't actually be necessary, as thought earlier
    # save the new information
    # note for the future-- how does this impact already created trajectories?

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
