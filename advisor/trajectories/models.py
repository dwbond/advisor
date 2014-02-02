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
    courseSlug = models.SlugField(max_length = 50, unique=True)

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

    def get_absolute_url(self):
        return '/courses/%s/' % self.slug

# gen eds are coursecollections in programs
class CourseCollection(BaseModel):

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

class Program(BaseModel):

    name = models.CharField(max_length = 150)
    # programSlug = models.SlugField(max_length = 50, unique = True)

    # courseCollections
    courseReqs =  models.ManyToManyField('CourseCollection',)

    # is BA, BS, Honors
    # all majors must take a gened program, null for minors, geneds
    degreeType = models.ManyToManyField('Program', null=True)

    # major or minor or gened
    programType = models.CharField(max_length = 25)

    # catalog year for the Program
    catalogYear = models.DateField()
    
    # if all coursecollections' and gened requirements are satisfied, then the
    # program is completed
    isCompleted = models.BooleanField(False)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    # def get_absolute_url(self):
        # return 'my-trajectories/%s/' % self.slug

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

class Trajectory(BaseModel):

    name = models.CharField(max_length = 150)
    trajectorySlug = models.SlugField(max_length = 50, unique = True)

    # Takes courses
    previousCourses = models.ManyToManyField('Trajectory',)

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
