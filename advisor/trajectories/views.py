from django.shortcuts import render, render_to_response, get_object_or_404
from trajectories.models import Course, CourseCollection, Program, Student, Trajectory
from django.db.models import Max

# processing functions

# run on each coursecollection
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

# run on each coursecollection
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
    """ returns the gen eds a student has to take based on their selected
        programs """
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
	    if firstMajorType is secondMajorType:
	        genEdList.append(secondMajorType)
		return genEdList
	except:
	    return genEdList

def maxProgramsAllowed(programList, maxProgramNumber):
    """ called to ensure student can't sign up for more than 2 majors, etc """
    if (len(programList) + 1) > maxProgramNumer:
        return False
    else:
        return True

def fulfilledReq(coursesTaken, courseCollection, numReq):
    """ makes CourseCollection.isCompleted True if completed
        should only use where isCompleted is False
	can also be used for Program.isCompleted """
    finished = 0
    for reqCourse in courseCollection:
	if reqCourse in coursesTaken:
	    finished += 1
	    if finished >= numReq:
                courseCollection.isCompleted = True
	        break

def topTrajectories(trajectories):
    """ Only shows the uppermost level of trajectories--
        there's no reason that *all* of the previously loaded classes
	need be gone through; furthermore, students only need to see
	the top level of each of their trajectories on their homepage """
    
    names = set()
    for trajectory in trajectories:
        names.append(trajectory.name)

    topTrajectories = []
    for name in names:
        namedTrajectories = trajectories.filter(name = name)
	topNamedTrajectory = namedTrajectories.aggregate(Max('semester'))
	topTrajectories.append(topNamedTrajectory)

    return topTrajectories

def enoughCourses(coursesTaken):
    """ required credits for degree program """
    if len(coursesTaken) > 120:
        return True
    else:
        return False

# note: coreq requirements are fulfilled through onpage javascript, not here

# page render functions

# this is where all users not signed in are redirected
def login(request):

    return render(request, 'login.html', {

    },
    )

# "homepage", create a new trajectory
#@login_required
def index(request):

    return render(request, 'index.html', {

    },
    )

# student selects the classes for their trajectories
# @login_required
# def create(request, slug): slug is the user's
def create(request):

    # needs to get list of programs from user
    programs = []

    return render(request, 'create.html', {
    
    },
    )

# student's page; shows saved trajectories
# @login_required
def student(request, slug):
    student = get_object_or_404(Student, user__username=username)
    trajectories = Trajectory.objects.filter(student__user__username=username)
    topTrajectories = topTrajectories(trajectories)

    return render(request, 'student.html', {
        'student' : student,
        'topTrajectories' : topTrajectories,

    },
    )

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

# simply displays a page for the course
def course(request, slug):

    course = get_object_or_404(Course, slug=slug)
    return render(request, 'course.html', {
        'course' : course,
    },
    )

# simply returns a page showing a program
# def program (request, slug):

    # program = get_object_or_404(Program, slug=slug)
    # return render(request, 'program.html, {
        # 'program' : program,
    # },
    # )

# simply displays a page for an individual trajectory, (along with edit links)
# @login_required
def trajectory(request, slug):
# actually needs more than one slug, the one for the user

    trajectory = get_object_or_404(Trajectory, slug=slug) 
    return render(request, 'trajectory.html', {
        'trajectory' : trajectory,
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
