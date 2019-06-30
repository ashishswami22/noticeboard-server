from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class TestView(APIView):
    permission_classes = (IsAuthenticated,) 

    def get(self, request, format=None):
        return Response({"first_name":"Ashish","last_name":"Swami"})