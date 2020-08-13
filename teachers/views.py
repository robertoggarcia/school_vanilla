from rest_framework.decorators import api_view
from rest_framework.response import Response

from teachers.models import Teacher
from teachers.serializers import TeacherSerializer


@api_view(['GET', 'POST'])
def teachers(request):
    if request.method == 'GET':
        teachers_data = Teacher.objects.all()
        serialized = TeacherSerializer(teachers_data, many=True)
        return Response(data=serialized.data)

    if request.method == 'POST':
        teacher_data = {
            'first_name': request.data['first_name'],
            'last_name': request.data['last_name'],
            'phone': request.data['phone']
        }
        Teacher.objects.create(**teacher_data)
        return Response(status=201)

    return Response({'foo': 'bar'})


@api_view(['GET', 'PUT', 'DELETE'])
def detail_teacher(request, teacher_id):
    if request.method == 'GET':
        teacher = Teacher.objects.get(id=teacher_id)
        serialized = TeacherSerializer(teacher)
        return Response(data=serialized.data)

    if request.method == 'PUT':
        teacher = Teacher.objects.get(id=teacher_id)
        for field in request.data:
            print(f'Field {field}, value {request.data[field]}')
            setattr(teacher, field, request.data[field])
        teacher.save()
        return Response(status=200)

    if request.method == 'DELETE':
        Teacher.objects.get(id=teacher_id).delete()
        return Response(status=204)
    return Response({})
