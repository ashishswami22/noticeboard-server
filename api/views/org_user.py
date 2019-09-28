from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.models import OrgUser

class OrgUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        orgUser = OrgUser.objects.filter(system_user_id=request.user.id)
        if not orgUser.exists():
            return Response([])
        return Response(OrgUser.objects.filter(org_id=orgUser.org_id))