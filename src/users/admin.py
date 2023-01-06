from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import HospitalUser

admin.site.register(HospitalUser, UserAdmin)
