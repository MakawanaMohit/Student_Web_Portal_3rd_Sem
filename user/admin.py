from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(User)



