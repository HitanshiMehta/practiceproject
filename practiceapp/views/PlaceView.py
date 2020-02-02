from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView

from practiceapp.Serializers.PlaceSerializer import PlaceSerializer
from practiceapp.models.PlaceModel import Place


class PlaceViews(APIView):
    def get(self,*args,**kwrgs):
        place=Place.objects.get_all()
        serializer=PlaceSerializer(place,many=True)
        return Response({"Places":serializer.data})

    def post(self,request):
        place=request.data.get('place')
        serializer=PlaceSerializer(data=place)
        if(serializer.is_valid(raise_exception=True)):
            place_saved=serializer.save()
        else:
            raise APIException("There was a problem!")
        return Response({"success":"Place {} created successfully".format(place_saved)})

