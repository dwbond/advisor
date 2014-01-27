from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save

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

    def isUpperClass:
      if courseNumber > 300:
          return True:
      else:
          return False

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

    # if the course collection's numreq is met
    isCompleted = models.BooleanField(False)

class Program(BaseModel):

    name = models.CharField(max_length = 150)

    # courseCollections
    courseReqs =  models.ManyToManyField('CourseCollection',)

    # major or minor or gened
    programType = models.CharField(max_length = 25)

    # is BA, BS, Honors
    # all majors must take a gened program, null for minors, geneds
    # CHECK VIEWS, MAKE SURE I DIDN'T ALREADY SOMEHOW ACCOUNT FOR THIS
    degreeType = models.ManyToManyField('Program', null=True)

    # if all coursecollections' and gened requirements are satisfied, then the
    # program is completed
    isCompleted = models.BooleanField(False)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

# should inherit from the standard Django User Model
class Student(models.Model):

    user = models.OneToOneField(User)

    # the student's already-completed classes, the root of the trajectory tree
    alreadyTaken = models.ManyToManyField('Course', null=True)
    
    # all of the student's trajectories
    trajectory = models.ManyToManyField('Trajectory', null=True)

    # aka username, etc should all be here

    class Meta:
        ordering = ('user',)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return self.name

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

class Trajectory(BaseModel):

    name = models.CharField(max_length = 150)

    # Takes courses
    previousCourses = models.ManyToManyField('Trajectory',)

    # the program(s) that this trajectory is completing
    # CHECK VIEWS, MAKE SURE I DIDN'T ALREADY SOMEHOW ACCOUNT FOR THIS
    forPrograms = models.ManyToManyField('Program',)

    # whether or not the trajectory can be seen by others
    isPublic = models.BooleanField()

    # this isn't exactly done correctly-- ideally courses should be elements
    # of a list, not one created for each and every semester
    semester = models.IntegerField()

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "trajectories"

    def get_absolute_url(self):
        return 'my-trajectories/%s/' % self.slug

        return '/%s/' % self.slug
