from django.shortcuts import render_to_response
from trajectories.models import Course, Trajectory, Student

# other functions

def remainingReqCourses(requiredCourses, coursesTaken):
    """ returns remaining courses for program """
    remainingReqCourses = []
    for course in requiredCourses:
        if course not in coursesTaken:
            remainingReqCourses.append(course)

def allPrereqCoreq(course, remainingReqCourses):
    """ returns required courses that have course as a prereq or coreq """
    allPrereqCoreq = []
    for requiredCourse in remainingReqCourses:
        for prereq in course.prereqs:
            if prereq is requiredCourse:
                allPrereqCoreq.append(prereq)
        for coreq in course.coreqs:
            if coreq is requiredCourse:
                allPrereqCoreq.append(coreq)
    return allPreqCoreq

def nextCourses(coursesTaken, remainingReqCourses):
     """ returns the courses student can take given what's been taken """
     nextCourses = []
     for course in remainingReqCourses:
         if course.prereqs not in coursesTaken:
             nextCourses.append(course)
         # you have to take the prereqs for something first
         elif course.coreq not in coursesTaken:
             nextCourses.append(course)
         else:
             possiblity = allPrereqCoreq(course, remainingReqCourses)
             append nextCourses.append(possiblity)
     return nextCourses

# how does one deal with "you have to take the coreq at the same time?"


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
