from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """test api view"""

    def get(self, request, format=None):
        """returns a list of apiview request"""
        an_apiview = [
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Isnsimilar to treditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'massage':'Hello!', 'an_apiview': an_apiview})
