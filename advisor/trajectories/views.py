from django.shortcuts import render, render_to_response
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
             possibility = allPrereqCoreq(course, remainingReqCourses)
             nextCourses.append(possibility)
     return nextCourses

# this algorithm sucks because if there's a change to the number of allowed
# majors then this will break
def getGenEds(programs, isHonors):
    genEdList = []
    if isHonors:
        genEdList.append("Honors")
	# will require a program in the database called "Honors"
	return genEdList
    else:
        firstMajorType = program[0].degreeType
	genEdList.append(firstMajorType)
	try:
	    secondMajor = program[1].degreeType
	    if firstMajorType is secondMajorType
	        genEdList.append(secondMajorType)
		return genEdList
	except:
	    return genEdList

# how does one deal with "you have to take the coreq at the same time?"

def topTrajectories(trajectories):
    topTrajectories = []
    # trajectories take trajectories
    # representing how you build up semester by semester
    # find the one on the top of the pile
    return topTrajectories

def getGenEds(programList, honorsBoolean):



# page render functions

# homepage, sign in to save or compare multiple options
#@login_required -- not sure how this part works
def index(request):

    return render(request, 'index.html', {

    },
    )

# SRCT, how to contribute information
def about(request):

    return render(request, 'about.html', {

    },
    )

# student creates trajectory
def makeTrajectory(request, slug):

    # needs to get list of programs from user
    programs = []
    # 

    return render(request, 'maketrajectory.html', {
    
    },
    )

# just displays a page for the course
def course(request, slug):

    return render(request, 'course.html', {

    },
    )

# student's page; shows saved trajectories
#@login_required
def student(request, slug):

    student = get_object_or_404(Student, user__username=username)
    trajectories = Trajectory.objects.filter(student__user__username=username)
    topTrajectories = topTrajectories(trajectories)
    # until the topTrajectories function is written, this is a blank list

    return render(request, 'student.html', {

      'student' : student,
      'topTrajectories' : topTrajectories,

    },
    )

# compares saved trajectories
#@login_required
def compare(request, slug):

    return render(request, 'compare.html', {

    },
    )

# page like one for courses, except for programs? >_>

#search for courses or programs view
