from django.urls import path

from students.views import students, student_done, student_detail, StudentView

app_name = 'students'
urlpatterns = [
    path('students/', students, name='view'),
    path('students/done/', student_done, name='done'),
    path('students/<student_id>/', student_detail, name='detail'),
    path('students_django/', StudentView.as_view(), name='django')
]
