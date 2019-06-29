from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=50)

class OrgUser(models.Model):
    username = models.CharField(max_length=50)
    password_hash = models.CharField(max_length=50)