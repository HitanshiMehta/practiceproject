from django.db import models

class Movie(models.Model):

    tmdb_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    imdb_id = models.CharField(max_length=255, blank=True)
    img_path = models.CharField(max_length=255, blank=True)
    runtime = models.CharField(max_length=65, blank=True)
    synopsis = models.TextField(blank=True)
    imdb_rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    metascore = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.title)