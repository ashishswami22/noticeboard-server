from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    # id is assigned automatically by django
    name = models.CharField(max_length=50)

class OrgUser(models.Model):
    # id is assigned automatically by django
    username = models.CharField(max_length=50)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE, default=0)
    system_user = models.ForeignKey(User, on_delete=models.CASCADE, default=0) # used for django's token based authentication workflow