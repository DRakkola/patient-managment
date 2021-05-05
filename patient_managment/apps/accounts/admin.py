from django.contrib import admin
from .models import UserGroups, UserProfile, UserRights
from django.contrib.auth.models import User

admin.site.register(UserProfile)
admin.site.register(UserGroups)
admin.site.register(UserRights)