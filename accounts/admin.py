from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

from . import models
# Register your models here.

class UserAdmin(BaseUserAdmin):
        model = User
        list_display=['username','email']



admin.site.register(User,UserAdmin)