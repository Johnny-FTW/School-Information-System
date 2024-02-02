from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.db import models
import os

# Create your models here.


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    date_of_birth = models.DateField(null=True, blank=True)
    title = models.CharField(null=True, blank=True)

    def __str__(self):
        return self.user


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
    date_of_birth = models.DateField(null=True, blank=True)
    student_image = models.ImageField(upload_to='static/', null=True, blank=True)
    school_class = models.ForeignKey(Class, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.user

    def save(self, *args, **kwargs):
        try:
            old_instance = Student.objects.get(pk=self.pk)
            if old_instance.student_image:
                if self.student_image and old_instance.student_image.path != self.student_image.path:
                    os.remove(old_instance.student_image.path)
        except Student.DoesNotExist:
            pass

        super().save(*args, **kwargs)
        if self.student_image:
            img = Image.open(self.student_image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.student_image.path)


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
    grade = models.CharField(null=True, max_length=1)
    max_points = models.IntegerField(blank=True)
    points_achieved = models.IntegerField(blank=True)

    def __str__(self):
        return f'{self.name}: {self.grade}'










