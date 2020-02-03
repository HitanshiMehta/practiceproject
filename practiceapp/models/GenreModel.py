from django.db import models


class Genre(models.Model):

    genre = models.CharField(max_length=65)

    def __str__(self):
        return "{}".format(self.genre)