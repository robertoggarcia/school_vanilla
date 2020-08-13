from django.conf.urls import url
from django.urls import path
from rest_framework import routers

from teachers.views import teachers, detail_teacher, TeachersView, TeacherDetailView

urlpatterns = [
    path('teachers/', teachers),
    path('teachers/<teacher_id>/', detail_teacher),
    path('teachers_view/', TeachersView.as_view()),
    path('teachers_view/<pk>/', TeacherDetailView.as_view()),
]
