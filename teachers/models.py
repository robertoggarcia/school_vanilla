from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
