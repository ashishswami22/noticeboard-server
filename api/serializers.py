from rest_framework import serializers
from api.models import OrgUser

class OrgUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgUser
        fields = '__all__'
        depth = 1
