from django.contrib import admin

# Register your models here.
from main_app.models import User, Student, Teacher, TeacherProfile

admin.site.register(User)

admin.site.register(Teacher)

admin.site.register(TeacherProfile)
