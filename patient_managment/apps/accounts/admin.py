from os import name
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User , Group
from .models import AccountsUsergroups as UserGroups,AccountsUserprofile as UserProfile,AccountsUserprofileRights as UserRights
from django.utils.translation import gettext_lazy as _
from django.contrib.admin.models import LogEntry
from django.http import HttpResponse

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

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    
    # to have a date-based drilldown navigation in the admin page
    date_hierarchy = 'action_time'
    

    # to filter the resultes by users, content types and action flags
    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    # when searching the user will be able to search in both object_repr and change_message
    search_fields = [
        'object_repr',
        'change_message'
    ]

    list_display = [
        'action_time',
        'user',
        'content_type',
        'action_flag',
    ]
    def has_add_permission(self, request):
            return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser