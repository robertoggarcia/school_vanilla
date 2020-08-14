from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from subjects.models import Subject
from subjects.serializers import SubjectSerializer


class ListSubjectsView(ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class CreateSubjectView(CreateAPIView):
    serializer_class = SubjectSerializer


class UpdateSubjectView(UpdateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class RetrieveSubjectView(RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class DestroySubjectView(DestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
