from django.db import models

class BaseModel(models.Model):
    created = models.DateTimeField('Created', auto_now_add=True, editable=False)_
    last_modified = models.DateTimeField('Last Modified', auto_now=True)
    name = models.CharField(max_length = 100)

    class Meta:
        abstract = True

class Course(BaseModel):

    # ordering
    prerequisites = models.ManyToManyField('Course')
    corequisites = models.ManyToManyField('Course')

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

    slug = models.SlugField(max_length = 50)

    # default sorting order in admin
    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/courses/%s/' % self.slug

# gen eds are coursecollections in programs
class CourseCollection(BaseModel):

    # a number of courses
    courses = ManyToManyField('Course')

    # how many of those are required
    numberOfCoursesReq = IntegerField()

class Program(BaseModel):

    # courseCollections
    courseReqs =  ManyToManyField('CourseCollection')

    # major or minor or gened
    programType = models.CharField()

    # is BA, BS, Honors
    degreeType = models.CharField()

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

# should inherit from the standard Django User Model
class Student(BaseModel):

    alreadyTaken = models.ManyToManyField('Course')
    trajectory = models.ManyToField('Trajectory')

    # aka username, etc should all be here

    slug = models.SlugField(max_length = 50)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):

class Trajectory(BaseModel):

    # Kind of want to overwrite "name" as optional

    # Takes courses
    potentialTrajectory = models.ManyToManyField('Course')

    # this isn't exactly done correctly-- ideally courses should be elements
    # of a list, not one created for each and every semester
    semester = models.IntegerField()

    def get_absolute_url(self):
        return 'my-trajectories/%s/' % self.slug

       return '/%s/' % self.slug
