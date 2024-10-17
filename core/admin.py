from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Areas, Apartment, User

# Register your models here.
class CustomUserAdmin(UserAdmin):
    pass

admin.site.register(Areas)
admin.site.register(Apartment)
admin.site.register(User, UserAdmin)