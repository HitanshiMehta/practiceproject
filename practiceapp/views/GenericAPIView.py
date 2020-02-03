from rest_framework import views


class GenericAPIView(views.APIView):
    """
    Base class for all other generic views.
    """

    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(GenericAPIView, self).get_serializer(*args, **kwargs)