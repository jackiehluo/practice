"""Models for this Django app"""

from django.db import models
from django.core.urlresolvers import reverse

class Movies(models.Model):
    """Model for the movies table in the database"""

    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    year = models.TextField()
    genre = models.TextField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie', args=[str(self.title.replace(' ', '_'))])

    class Meta:
        """Meta class for Movies model"""

        managed = True
        db_table = 'movies'
