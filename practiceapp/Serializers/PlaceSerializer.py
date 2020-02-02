from rest_framework import serializers

from practiceapp.models.PlaceModel import Place

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model= Place
        fields = ('name','address')