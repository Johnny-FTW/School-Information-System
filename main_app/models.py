from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Classroom(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    max_capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=200)
    class_teacher = models.OneToOneField(Teacher, on_delete=models.DO_NOTHING)
    academic_year = models.CharField(max_length=9, help_text="Format: YYYY/YYYY")
    school_year = models.CharField(max_length=9, help_text="Format: YYYY/YYYY")

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    student_image = models.ImageField(upload_to='images/', null=True, blank=True)
    school_class = models.ForeignKey(Class, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Subject(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    student = models.ManyToManyField(Student)
    classroom = models.ForeignKey(Classroom,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Exam(models.Model):
    name = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    max_points = models.IntegerField()
    points_achieved = models.IntegerField()

    def __str__(self):
        return f'{self.name}: {self.max_points}/{self.points_achieved}'









