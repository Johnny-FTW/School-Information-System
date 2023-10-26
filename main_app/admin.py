from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

from main_app.models import Subject

admin.site.register(Subject)
