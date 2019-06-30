from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,) 

    def post(self, request, format=None):
        token = Token.objects.get(key=request.META['HTTP_AUTHORIZATION'][6:])
        if token.exists():
            token.delete()
        return Response()