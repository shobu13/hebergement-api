from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class HostedInline(admin.StackedInline):
    model = Hosted
    max_num = 1


class HostInline(admin.StackedInline):
    model = Host
    max_num = 1
    extra = 0


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        UserAdmin.fieldsets[0],
        (UserAdmin.fieldsets[1][0],
         {'fields': UserAdmin.fieldsets[1][1]['fields'] + ('phone_number', 'description', 'city_name', 'city_lat', 'city_lng')}),
        UserAdmin.fieldsets[2],
        UserAdmin.fieldsets[3],
    )
    inlines = (HostedInline, HostInline)


admin.site.register(User, CustomUserAdmin)
