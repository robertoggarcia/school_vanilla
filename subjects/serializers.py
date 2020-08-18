from rest_framework.serializers import ModelSerializer

from subjects.models import Subject
from teachers.serializers import TeacherSerializer


class SubjectDetailSerializer(ModelSerializer):
    teacher = TeacherSerializer(read_only=True)

    class Meta:
        model = Subject
        fields = '__all__'


class SubjectSerializer(ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'