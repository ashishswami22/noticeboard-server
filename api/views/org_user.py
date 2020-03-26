from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.models import OrgUser
from api.serializers import OrgUserSerializer
from django.core.exceptions import ObjectDoesNotExist

class OrgUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        try:
            orgUser = OrgUser.objects.get(system_user_id=request.user.id)
            return Response(OrgUserSerializer(OrgUser.objects.filter(org_id=orgUser.org_id), many=True).data)
        except ObjectDoesNotExist:
            return Response([])

