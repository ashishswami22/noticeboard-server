from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import logout
from rest_framework.permissions import IsAuthenticated

class LogoutView(APIView):

    def post(self, request, format=None):
        logout(request)
        return Response()

class SessionView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        return Response(request.user.username)
