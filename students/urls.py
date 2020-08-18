from django.urls import path, include
from rest_framework.routers import DefaultRouter

from students.views import students, student_done, student_detail, StudentView, StudentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)

app_name = 'students'
urlpatterns = [
    path('', include(router.urls)),
    path('students_view/', students, name='view'),
    path('students/done/', student_done, name='done'),
    path('students/<student_id>/', student_detail, name='detail'),
    path('students_django/', StudentView.as_view(), name='django')
]
