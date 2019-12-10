from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters


from app1 import serializers
from app1 import models
from app1 import permissions


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


class HelloViewSet(viewsets.ViewSet):
    """Test api viewsets"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return hello message"""

        a_viewset = [
            'Uses action (list, create, Retrive, update, partial_update)',
            'Automatically maps to URLs using Return',
            'Provides more functionality with less code',
        ]

        return Response({'message':'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """"Create a new hello message"""
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

    def retrive(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Responce({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends =(filters.SearchFilter,)
    search_fields =('name', 'email',)
