# Generated by Django 2.2.14 on 2020-08-12 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_subject_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher'),
        ),
    ]
