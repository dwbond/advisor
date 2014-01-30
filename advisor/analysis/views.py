from django.shortcuts import render, get_object_or_404
from trajectories.models import Course, CourseCollection, Program, Student, Trajectory
# import login

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

#@login_required
# def analytics(request, slug):
def analytics(request):

    return render(request, 'analytics.html', {

    },
    )
