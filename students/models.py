from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    grade = models.FloatField(default=0.0)
    active = models.BooleanField(default=True)
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
