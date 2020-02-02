from django.contrib import admin

from practiceapp.models.PlaceModel import Place
from practiceapp.models.RestaurantModel import Restaurant

admin.site.register(Place)
admin.site.register(Restaurant)
