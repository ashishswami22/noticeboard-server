from django.contrib import admin

from .models import OrgUser, Organization

admin.site.register(OrgUser)
admin.site.register(Organization)