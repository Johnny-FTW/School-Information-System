from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db.models import *


class Subject(Model):
    name = CharField(max_length=16, null=False, unique=True)

    def __str__(self):
        return self.name


