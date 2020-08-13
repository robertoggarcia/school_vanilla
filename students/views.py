import datetime
import json

from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from students.models import Student
from django.views import View


class StudentView(View):
    http_method_names = ['get', 'post']

    def get(self, request):
        students_data = Student.objects.all()
        context = {
            'students': students_data
        }
        return render(request, 'students/list.html', context)

    def post(self, request):
        student_data = {
            'name': request.POST['name'],
            'age': int(request.POST['age']),
            'grade': float(request.POST['grade'])
        }

        try:
            Student.objects.create(**student_data)
        except Exception as e:
            print(e)
        return redirect('students:done')


def students(request):
    if request.method == 'GET':
        students_data = Student.objects.all()
        context = {
            'students': students_data
        }
        return render(request, 'students/list.html', context)

    if request.method == 'POST':
        student_data = {
            'name': request.POST['name'],
            'age': int(request.POST['age']),
            'grade': float(request.POST['grade'])
        }

        try:
            Student.objects.create(**student_data)
        except Exception as e:
            print(e)
        return redirect('students:done')
    return render(request, 'students/list.html', {})


def student_done(request):
    return render(request, 'students/done.html', {'message': 'Listo'})


def student_detail(request, student_id):
    if request.method == 'GET':
        student = Student.objects.get(id=student_id)
        context = {
            'student': student
        }
        return render(request, 'students/detail.html', context)
    if request.method == 'POST':
        student = Student.objects.get(id=student_id)
        student.delete()
        return redirect('students:done')
