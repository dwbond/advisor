from django.db import models

class BaseModel(models.Model):
    created = models.DateTimeField('Created', auto_now_add=True, editable=False)_
    last_modified = models.DateTimeField('Last Modified', auto_now=True)
    name = models.CharField(max_length = 100)

    class Meta:
        abstract = True

class Course(BaseModel):

    department = models.CharField(max_length = 5)
    courseNumber = models.CharField(max_length = 3)

    # available next semester?
    # CRN
    # section number
    
    slug = models.SlugField(max_length = 50)

    # ordering
    prerequisites = models.ManyToManyField()
    corequisites = models.ManyToManyField()

    # default sorting order in admin
    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/courses/%s/' % self.slug

class Trajectory(BaseModel):

    # Unsure how to represent this 

    # Kind of want to overwrite "name" as optional

    # Takes courses
    potentialTrajectory = models.ManyToManyField()

    def get_absolute_url(self):
        return 'my-trajectories/%s/' % self.slug

# should inherit from the standard Django User Model
class Student(BaseModel):

    alreadyTaken = models.ManyToManyField()
    trajectory = models.ManyToField()

    slug = models.SlugField(max_length = 50)

    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/%s/' % self.slug
