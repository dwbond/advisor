from django.shortcuts import render, render_to_response, get_object_or_404
from trajectories.models import Course, CourseCollection, Program, Student, Trajectory
from django.db.models import Max

# processing functions

# def analyzeEverything():

# page render functions

# compares saved trajectories
#@login_required
# def compare(request, slug):
def compare(request):

    # this is gonna be hella slow; I need to learn how ajax works and what
    # it will actually need
    
    trajectories = Trajectory.objects.all()
    return render(request, 'compare.html', {
        'trajectories' : trajectories,
    },
    )
