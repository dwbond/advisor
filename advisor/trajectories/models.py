from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created = models.DateTimeField('Created', auto_now_add=True, editable=False)
    last_modified = models.DateTimeField('Last Modified', auto_now=True)

    class Meta:
        abstract = True

class Course(BaseModel):

    name = models.CharField(max_length = 150)

    # ordering
    prerequisites = models.ManyToManyField('Course', related_name = 'prereqField', null=True)
    corequisites = models.ManyToManyField('Course', related_name = 'coreqField', null=True)

    # basic course information
    department = models.CharField(max_length = 150)
    departmentAbbr = models.CharField(max_length = 5)
    courseNumber = models.CharField(max_length = 3)
    courseDescription = models.TextField()
    credits = models.IntegerField()

    # available next semester?
    # CRN
    # section number
    # professor
    
    # Course may need program-specific information

    # default sorting order in admin
    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/courses/%s/' % self.slug

# gen eds are coursecollections in programs
class CourseCollection(BaseModel):

    name = models.CharField(max_length = 150)

    # a number of courses
    courses = models.ManyToManyField('Course',)

    # how many of those are required
    numReq = models.IntegerField()

    isCompleted = models.BooleanField(False)

class Program(BaseModel):

    name = models.CharField(max_length = 150)

    # courseCollections
    courseReqs =  models.ManyToManyField('CourseCollection',)

    # major or minor or gened
    programType = models.CharField(max_length = 25)

    # is BA, BS, Honors
    degreeType = models.CharField(max_length = 25)

    isCompleted = models.BooleanField(False)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

# should inherit from the standard Django User Model
class Student(User):

    user = models.OneToOneField(User)

    alreadyTaken = models.ManyToManyField('Course', null=True)
    
    trajectory = models.ManyToManyField('Trajectory', null=True)

    # aka username, etc should all be here

    class Meta:
        ordering = ('user',)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return self.name

class Trajectory(BaseModel):

    name = models.CharField(max_length = 150)

    # Takes courses
    previousCourses = models.ManyToManyField('Trajectory',)

    isPublic = models.BooleanField()

    # this isn't exactly done correctly-- ideally courses should be elements
    # of a list, not one created for each and every semester
    semester = models.IntegerField()

    def get_absolute_url(self):
        return 'my-trajectories/%s/' % self.slug

        return '/%s/' % self.slug
