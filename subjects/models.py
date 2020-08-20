from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from students.models import Student
from teachers.models import Teacher


class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, related_name='subjects')
    students = models.ManyToManyField(Student, related_name='courses', through='SubjectStudent')
    owner = models.ForeignKey(User, related_name='subjects', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class SubjectStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_created=True, default=timezone.now)
