from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Profile
# Register your models here.

class UserInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Доп. информация'
 

class UserAdmin(UserAdmin):
    inlines = (UserInline, )
 

admin.site.unregister(User)
admin.site.register(User, UserAdmin)