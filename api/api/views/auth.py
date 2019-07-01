from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import logout

class LogoutView(APIView):

    def post(self, request, format=None):
        logout(request)
        return Response()