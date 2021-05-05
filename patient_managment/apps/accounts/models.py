from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserRights(models.Model):
    name = models.CharField(max_length=50 , unique=True)
    Details = models.CharField(max_length=200 , default='rights details')
    def __str__(self):
        return self.name

class UserGroups(models.Model):
    name = models.CharField(max_length=50 , unique=True)
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    #Owner
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    #Settings
    is_full_name_displayed = models.BooleanField(default=True)

    #details
    bio = models.CharField(max_length=500, blank=True, null=True)
    Group = models.ForeignKey(UserGroups, on_delete=models.SET_NULL, blank=True, null=True)
    Rights = models.ManyToManyField(UserRights,blank=True)
    def __str__(self):
        return self.user.username