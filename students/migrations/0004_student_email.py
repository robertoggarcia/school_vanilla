# Generated by Django 2.2.14 on 2020-08-21 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(default='student@gmail.com', max_length=100),
        ),
    ]