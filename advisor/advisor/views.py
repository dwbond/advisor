from django.shortcuts import render, render_to_response, get_object_or_404
from trajectories.models import Course, CourseCollection, Program, Student, Trajectory
from django.db.models import Max

# processing functions

# page render functions

# this is where all users not signed in are redirected
#@login_required
def login(request):
    
    return render(request, 'login.html', {
        "courses" : courses
    },
    )

# "homepage", create a new trajectory
#@login_required
def index(request):

    return render(request, 'index.html', {

    },
    )

# search

# # # # # STATIC PAGES # # # # #

# SRCT, how to contribute information, how Advisor works
def about(request):

    return render(request, 'about.html', {

    },
    )

# def privacy(request):
