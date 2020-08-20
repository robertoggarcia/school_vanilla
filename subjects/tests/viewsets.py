from rest_framework.test import APITestCase
from faker import Faker

from subjects.models import Subject
from teachers.models import Teacher


class TestSubjectViewSet(APITestCase):

    def setUp(self) -> None:
        faker = Faker()
        self.url_base = 'http://127.0.0.1:8000'
        self.teacher = Teacher.objects.create(first_name=faker.name(),
                                              last_name=faker.last_name(),
                                              phone=faker.phone_number())
        self.s1 = Subject.objects.create(name='Python', description=faker.text())
        self.s2 = Subject.objects.create(name='JavaScript',
                                         description=faker.text(), teacher=self.teacher)

    def test_get_list(self):
        endpoint = '/subjects/'
        response = self.client.get(f'{self.url_base}{endpoint}')

        self.assertEqual(response.status_code, 200, 'La url no existe')
        self.assertEqual(response.data['count'], 2, 'El queryset es incorrecto')

    def test_filter_by_teacher(self):
        endpoint = f'/subjects/?teacher={self.teacher.id}'
        response = self.client.get(f'{self.url_base}{endpoint}')

        self.assertEqual(response.data['count'], 1, 'El filtro por FK no funciona')

    def test_filter_text(self):
        endpoint = f'/subjects/?name=python'
        response = self.client.get(f'{self.url_base}{endpoint}')

        self.assertEqual(response.data['count'], 1, 'El filtro por texto no funciona')

    def test_serializer_retrieve(self):
        endpoint = f'/subjects/{self.s2.id}/'
        response = self.client.get(f'{self.url_base}{endpoint}')

        self.assertEqual(response.data['teacher']['id'], self.teacher.id, 'Información incompleta')

    def test_teacher_get_action(self):
        endpoint = f'/subjects/{self.s2.id}/teacher/'
        response = self.client.get(f'{self.url_base}{endpoint}')

        self.assertEqual(response.status_code, 200)

    def test_teacher_post_action(self):
        endpoint = f'/subjects/{self.s1.id}/teacher/'
        data = {
            'teacher_id': self.teacher.id
        }
        response = self.client.post(f'{self.url_base}{endpoint}', data=data)
        self.assertEqual(response.status_code, 200)
        self.s1.refresh_from_db()
        self.assertEqual(self.s1.teacher.id, self.teacher.id, 'La acción de asignar profesor esta fallando')
        assert self.s1.teacher.id == self.teacher.id
