from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    # id is assigned automatically by django
    name = models.CharField(max_length=50)

class OrgUser(models.Model):
    # id is assigned automatically by django
    org = models.ForeignKey(Organization, on_delete=models.CASCADE, default=0)
    systemUser = models.ForeignKey(User, on_delete=models.CASCADE, default=0) # used for django's token based authentication workflow
    firstName = models.CharField(max_length=100, default=None)
    lastName = models.CharField(max_length=100, default=None)
    email = models.CharField(max_length=200, default=None)
    contactNumber = models.CharField(max_length=50, default=None)

class Batch(models.Model):
    # id is assigned automatically by django
    title = models.CharField(max_length=50, default=None)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE, default=0)
    description = models.CharField(max_length=200, default=None)

class Location(models.Model):
    # id is assigned automatically by django
    title = models.CharField(max_length=50, default=None)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE, default=0)
    description = models.CharField(max_length=200, default=None)

class Notification(models.Model):
    # id is assigned automatically by django
    title = models.CharField(max_length=200, default=None)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE, default=0)
    content = models.CharField(max_length=1000, default=None)
    attachmentUrl = models.CharField(max_length=500, default=None)

class Event(models.Model):
    # id is assigned automatically by django
    title = models.CharField(max_length=200, default=None)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE, default=0)
    content = models.CharField(max_length=1000, default=None)
    attachmentUrl = models.CharField(max_length=500, default=None)
    start = models.DateTimeField()
    end = models.DateTimeField()

class OrgUserBatchMapping(models.Model):
    OrgUser = models.ForeignKey(OrgUser, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)

class OrgUserEventMapping(models.Model):
    OrgUser = models.ForeignKey(OrgUser, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

class OrgUserNotificationMapping(models.Model):
    OrgUser = models.ForeignKey(OrgUser, on_delete=models.CASCADE)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)

class EventLocationMapping(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
