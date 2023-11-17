from django.contrib import admin

# Register your models here.
from main_app.models import Student, Teacher, User

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)


