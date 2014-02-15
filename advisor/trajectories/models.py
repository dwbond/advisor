from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField 

class Course(TimeStampedModel):
    name = models.CharField(max_length = 150)
    courseSlug = AutoSlugField(populate_from='name', unique=True)

    # ordering
    prerequisites = models.ManyToManyField('Course', related_name = 'prereqField', null=True)
    corequisites = models.ManyToManyField('Course', related_name = 'coreqField', null=True)

    # basic course information
    department = models.CharField(max_length = 150)
    departmentAbbr = models.CharField(max_length = 5)
    courseNumber = models.CharField(max_length = 3)
    courseDescription = models.TextField()
    credits = models.IntegerField()

    # catalog year for the course
    catalogYear = models.DateField()

    def isUpperClass(coursenumber):
      if courseNumber > 300:
          return True
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

    #def get_absolute_url(self):
     #   return '/courses/%s/' % self.slug

# gen eds are coursecollections in programs
class CourseCollection(TimeStampedModel):
    name = models.CharField(max_length = 150)

    # a number of courses
    courses = models.ManyToManyField('Course',)

    # how many of those are required
    numReq = models.IntegerField()

    # function to determine if there is a difference between this and last year
    # not everything changes-- should be able to multiple reference to one thing

    # catalog year for the coursecollection
    catalogYear = models.DateField()

    # if the course collection's numreq is met
    isCompleted = models.BooleanField(False)

class Program(TimeStampedModel):
    name = models.CharField(max_length = 150)
    # change populate_from
    slug = AutoSlugField(populate_from='name',unique=True)

    # courseCollections
    courseReqs =  models.ManyToManyField('CourseCollection',)
    
    # catalog year for the Program
    catalogYear = models.DateField()
    
    # if all coursecollections and gened requirements are satisfied, then the
    # program is completed
    # FINISH THIS
    def isCompleted(courseReqs):
        return True

    isCompleted = models.BooleanField(False)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    # def get_absolute_url(self):
        # return 'my-trajectories/%s/' % self.slug
class Major(Program):
    degreeType = models.ForeignKey('GenEd')

    class Meta:
        pass

class Minor(Program):
    major = models.ForeignKey('Major') 

    class Meta:
        pass

class GenEd(Program):
    pass

class Trajectory(TimeStampedModel):
    name = models.CharField(max_length = 150)
    slug = AutoSlugField(populate_from='name',unique=True)
    owner = models.ForeignKey(User)

    # Takes courses
    previousCourses = models.ManyToManyField('Trajectory',)

    # the newly added courses for that trajectory
    courses = models.ManyToManyField('Course',)

    # def getPreviousTrajectory(Trajectory):
        # return Trajectory

    # the program(s) that this trajectory is completing
    whichPrograms = models.ManyToManyField('Program',)

    # whether or not the trajectory can be seen by others
    isPublic = models.BooleanField()

    # semesters since entering college
    semester = models.IntegerField()

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "trajectories"

    def get_absolute_url(self):
        return 'my-trajectories/%s/' % self.slug

# should inherit from the standard Django User Model
class Student(models.Model):
    user = models.OneToOneField(User)
    # does User have a slug field?

    # aka username, etc should all be here
    
    # all of the student's trajectories
    trajectories = models.ManyToManyField('Trajectory', null=True)

    # a big ol' list of courses the student has already completed
    completedCourses = models.ManyToManyField('Course', null=True)

    isHonors = models.BooleanField(False),

    semester = models.IntegerField()

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
