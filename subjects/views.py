from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.paginations import SmallResultsSetPagination
from students.models import Student
from students.serializers import StudentSerializer
from subjects.models import Subject
from subjects.permissions import SubjectPermissions
from subjects.serializers import SubjectSerializer, SubjectDetailSerializer
from teachers.models import Teacher
from teachers.serializers import TeacherSerializer


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    pagination_class = SmallResultsSetPagination
    permission_classes = [SubjectPermissions, ]

    def get_queryset(self):
        parameters = {}
        for param in self.request.query_params:
            if param in ['page', 'page_size']:
                continue
            if param in ['teacher', 'id', 'students']:
                parameters[param] = self.request.query_params[param]
                continue
            parameters[param + '__icontains'] = self.request.query_params[param]

        subjects_filtered = Subject.objects.filter(**parameters)
        return subjects_filtered

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SubjectDetailSerializer
        return SubjectSerializer

    @action(detail=True, methods=['GET', 'POST', 'DELETE', 'PUT']) # subjects/pk/teacher/
    def teacher(self, request, pk=None):
        subject = self.get_object()

        if request.method == 'GET':
            if not subject.teacher:
                return Response(status=status.HTTP_204_NO_CONTENT, data={'message': 'No hay profesor asignado'})

            teacher = subject.teacher
            serialized = TeacherSerializer(teacher)
            return Response(status=status.HTTP_200_OK, data=serialized.data)

        if request.method in ['POST', 'PUT']:
            teacher_id = request.data.get('teacher_id', '')
            teacher = get_object_or_404(Teacher, id=teacher_id)
            #try:
            #    return Teacher.objects.get(id=teacher_id)
            #except:
            #    return Response(status=status.HTTP_404_NOT_FOUND)
            subject.teacher = teacher
            subject.save()
            serialized = SubjectDetailSerializer(subject)
            return Response(status=status.HTTP_200_OK, data=serialized.data)

        if request.method == 'DELETE':
            subject.teacher = None
            subject.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(detail=True, methods=['GET', 'POST'])
    def students(self, request, pk=None):
        subject = self.get_object()

        if request.method == 'GET':
            serialized = StudentSerializer(subject.students, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)

        if request.method == 'POST':
            students_ids = request.data.get('students')
            for id in students_ids:
                student = Student.objects.get(id=id)
                subject.students.add(student)
            subject.save()
            return Response(status=status.HTTP_200_OK)

    @action(detail=False)
    def order(self, request):
        subjects = Subject.objects.all().order_by('name')
        serialized = SubjectSerializer(subjects, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
