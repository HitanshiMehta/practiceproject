from rest_framework import serializers
from practiceapp.models.MovieModel import Movie


class MovieSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(MovieSerializer, self).__init__(many=many, *args, **kwargs)

    # genres = serializers.SlugRelatedField(slug_field='genre', many=True, queryset=Genre.objects.all())

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Movie
        fields = ('tmdb_id',
                  'imdb_id',
                  'title',
                  'release_date',
                  'img_path',
                  'runtime',
                  'synopsis',
                  'imdb_rating',
                  'metascore')

# def create(self, validated_data):
#     genres_data = validated_data.pop('genres')
#     movie = Movie.objects.create(**validated_data)
#
#     for genre_name in genres_data:
#         genre, created = Genre.objects.get_or_create(genre=genre_name)
#         movie.genres.add(genre)
#
#     return movie