from os import name
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User , Group
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from .models import AccountsUsergroups as UserGroups,AccountsUserprofile as UserProfile,AccountsUserprofileRights as UserRights
from django.contrib import auth
from django.utils.translation import gettext_lazy as _

class UserProfileAdmin(admin.ModelAdmin):
    verbose_name = 'Users Profiles'
    model = UserProfile
    list_display = ('id','user','bio','get_name')
    def get_name(self,obj):
        return obj.group.name
    get_name.short_description = 'User Group'  #Renames column head
    pass

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'last_login') # Added last_login
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserGroups)
admin.site.register(UserRights)
admin.site.unregister(Group)
admin.site.site_header = "Admin Service d'anesthesie"