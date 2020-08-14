from django.urls import path, include
from rest_framework.routers import DefaultRouter

from subjects.views import ListSubjectsView, CreateSubjectView, UpdateSubjectView, RetrieveSubjectView, \
    DestroySubjectView, SubjectViewSet

router = DefaultRouter()
router.register(r'subjects_viewset', SubjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('subjects/', ListSubjectsView.as_view()),
    path('subjects/create/', CreateSubjectView.as_view()),
    path('subjects/<int:pk>/', UpdateSubjectView.as_view()),
    path('subjects/detail/<int:pk>/', RetrieveSubjectView.as_view()),
    path('subjects/delete/<int:pk>/', DestroySubjectView.as_view())
]
