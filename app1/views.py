from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from app1 import serializers


class HelloApiView(APIView):
    """test api view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """returns a list of apiview request"""
        an_apiview = [
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Isnsimilar to treditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'massage':'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """"Create hello massage with our name"""
        serializer = self.serializer_class(data=request.data)


        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """"Handle a partial update of an object"""
        return Response({'methode': 'PATCH' })

    def delete(self, request, pk=None):
        """delete an object"""
        return Response({'methode':'DELETE'})
