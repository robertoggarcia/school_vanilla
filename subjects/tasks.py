from school.celery import app
from core.utils import send_my_email


@app.task(name='send_email_to_students')
def send_email_to_students(students):
    for student in range(1):
        send_my_email(
            'Bienvenido a la clase',
            'Gracias por estar en la clase, espero que aprendas mucho',
            'rob@gmail.com',
            'fake@gmail.com'
        )
