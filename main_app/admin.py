from django.contrib import admin

# Register your models here.
from main_app.models import *

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Classroom)
admin.site.register(Subject)
admin.site.register(Class)
admin.site.register(Exam)
admin.site.register(SubjectSchedule)



