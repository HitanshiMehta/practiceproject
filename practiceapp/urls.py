from django.urls import path, include

from practiceapp.views.PlaceView import PlaceViews

urlpatterns = [
    path('place/', PlaceViews.as_view()),
]