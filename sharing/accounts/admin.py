from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile

# profile admin 
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "profile"


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

# admin 의 기본 User 모델 등록 취소.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)