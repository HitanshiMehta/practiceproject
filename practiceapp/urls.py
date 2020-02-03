from django.urls import path, include

from practiceapp.views.MovieVIew import MovieDetailsView
from practiceapp.views.PlaceView import PlaceViews


urlpatterns = [
    path('place/', PlaceViews.as_view()),
    path('movie/', MovieDetailsView.as_view()),
]