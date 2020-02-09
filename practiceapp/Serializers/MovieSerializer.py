from django.utils import timezone
from rest_framework import serializers
from rest_framework.fields import empty

from practiceapp.models.MovieModel import Movie


class MovieSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""


    def __init__(self, instance=None, data=empty, **kwargs):

        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        super().__init__(instance, data, **kwargs)

        # if fields is not None:
        #     # Drop any fields that are not specified in the `fields` argument.
        #     allowed = set(fields)
        #     print("allowed",allowed)
        #     existing = set(self.fields.keys())
        #     print("existing",existing)
        #
        #     for field_name in existing - allowed:
        #         print("in for loop",self.fields.pop(field_name))
        #         self.fields.pop(field_name)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

        # self.context["Search_Name"]=serializers.CharField(max_length=100,write_only=True)



    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Movie
        fields = "__all__"

    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        if data['release_date'] > data['end_date']:
            raise serializers.ValidationError("end date must occur after release date")
        return data
