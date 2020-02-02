from django.db import models

from practiceapp.managers.PlaceManager import PlaceManager

# ADDRESS_TYPES = (
#     ('s', 'Surat'),
#     ('b', 'Bhavnagar'),
#     ('m', 'Mumbai'),
# )

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    objects=PlaceManager()