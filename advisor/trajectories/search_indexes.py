from haystack import indexes
from django.utils import timezone # required for when the indexes were last updated
from trajectories.models import Course

class CourseIndex(indexes.SearchIndex, indexes.Indexable):
    # search result
    # there can only be one document=True per model
    text = indexes.CharField( document=True, use_template=True )

    # search filtering
    name = indexes.CharField( model_attr = 'name' )
    contents = indexes.CharField( model_attr = 'courseDescription' )
    department = indexes.CharField( model_attr = 'department' )
    departmentAbbr = indexes.CharField( model_attr = 'departmentAbbr' )
    courseNumber = indexes.CharField( model_attr = 'courseNumber' )

    def get_model(self):
        return Course

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
