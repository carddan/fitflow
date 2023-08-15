from django.contrib import admin
from .models import FitUser, CyclePhase, Workout
from django.contrib.auth.admin import UserAdmin

admin.site.register(FitUser)
admin.site.register(CyclePhase)

admin.site.register(Workout)

class UserAdminConfig(UserAdmin):
    search_fields = ('username', 'email', 'first_name')
    list_filter = ('username', 'email', 'firstname', 'is_active', 'is_staff', 'is_superuser')
    ordering = ('date_joined', )
    list_display = ('username', 'email', 'firstname', 'is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'firstname')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Personal', {'fields': ('about',)}),
    )


                