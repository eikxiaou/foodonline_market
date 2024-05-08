from typing import Any
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import User,UserProfile

from . import models
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('first_name','last_name','username','email','phone_number','role','date_joined','last_login','is_staff','is_active')
    fieldsets = ()
    def get_form(self, request: Any, obj: Any | None = ..., change: bool = ..., **kwargs: Any) -> Any:
        form = super().get_form(request, obj, **kwargs)
        print(form.base_fields.keys())
        form.base_fields['password'].disabled =True
        return form

admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)