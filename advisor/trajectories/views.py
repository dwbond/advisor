from django.shortcuts import render_to_response
from trajectories.models import Course, Trajectory, Student

# other functions

# page render functions

# homepage, sign in to save or compare multiple options
#@login_required -- not sure how this part works
def index(request):

    return render_to_response('index.html', {

    },
    )

# just displays a page for the course
def course(request, slug):

    return render_to_response('course.html', {

    },
    )

# student's page; shows saved trajectories
#@login_required
def student(request, slug):

    return render_to_response('student.html', {

    },
    )

# compares saved trajectories
#@login_required
def compare(request):

    return render_to_response('compare.html', {

    },
    )

# SRCT, how to contribute information
def about(request):

    return render_to_response('about.html', {

    },
    )
