## Creando mi primer proyecto Django

### Crear ambiente

1. Crear un ambiente virtual
    
    python -m venv "nombre del ambiente"
    
    `python -m venv venv`
 
 2. Activar mi ambiente
    - source "nombre del ambiente"/bin/activate (Linux/OsX)
    - "nombre del ambiente"/Scripts/activate.bat (Windows CMD)
    - "nombre del ambiente"/Scripts/Activate.ps1 (Windows PowerShell)
`source venv/bin/activate`

3. Instalar Django 2.2 *
 `pip install Django==2.2.14`


### Crear proyecto

1. Crear mi proyecto de Django *
    - django-admin startproject "nombre del proyecto"
    
    `django-admin startproject school`

2. Configurar ambiente (PyCharm) *
 - Abrir el proyecto (File -> Open -> "ruta")
 - Configurar el ambiente virtual (File -> Settings -> Project -> Project interpreter)
 - Agregar ambiente existente (Add -> existing environment -> "Ruta al venv")


### Configurar base de datos
1. Instalar psycopg2 (si usaremos postgres)
    
    `pip install psycopg2`

2. En el archivo de configuración, vamos a asignar el motor que usaremos:
* postgres
* oracle
* MySql
* Sqlite3

Configuramos los datos de conexión: NAME (nombre de la base de datos), USER, PASSWORD, HOST, PORT.

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'school',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': '127.0.0.1',
            'PORT': '5432'
        }
    }

Previamente debe estar creada la base de datos con ese nombre.


### Correr mi proyecto
1. Verificar que no tenemos errores

    `python manage.py check`

2. Aplicar las migraciones base de Django

    `python manage.py migrate`

3. Correr el servidor
    
    `python manage.py runserver`


### Crear aplicación
1. python manage.py startapp "nombre de la aplicación"
    
    `python manage.py startapp students`

2. Registrar la aplicación en el proyecto
"carpeta de configuración del proyecto"/settings.py -> INSTALLED_APPS

Agregamos la ruta a el archivo "apps.py" y la clase que contiene: "StudentsConfig".


### Crear un modelo
1. Crear un clase que herede de models.Model

2. Crear migraciones
    
    `python manage.py makemigrations`

3. Aplicar esas migraciones
    
    `python manage.py migrate`

4. Registra el modelo para verlo en Admin de Django (admin.py)
```    
    from django.contrib import admin
    
    from subjects.models import Subject    
    
    admin.site.register(Subject)
```
Para ver una migración a nivel SQL, usar el siguiente comando:
python manage.py sqlmigrate "nombre de la aplicación" "número de migración"
    
    `python manage.py sqlmigrate students 0001`


### Django admin
El administrador de Django nos permite gestionar de forma sencilla todo lo relacionado a los modelos. Es necesario contar con un super usuario de django.

`python manage.py createsuperuser`


### BD

### Realación 1:1
`user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE, null=True)`

### Relación 1:N
`teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, related_name='subjects')`

### Relación N:N
Base (Django crea una tabla pivote)
`students = models.ManyToManyField(Student, related_name='courses')`

Creando nuestra propia tabla pivote
`students = models.ManyToManyField(Student, related_name='courses', through='SubjectStudent')`

Donde SubjectStudent, es un modelo que nosotros creamos, con la relación (ForeignKey) de las tablas relacionadas.

Es posible agregar un registro mediante '.add':
`subject_1.students.add(student_1)`

O eliminar un registr con '.remove':
`subject_1.students.remove(student_1)`

## Endpoints

## Crear un serializador
Un serializador nos permite convertir lo que tenemos en la BD a un json, o a una estructura que pueda mandada como respuesta de una petición. Convierte información de una forma a otra.

1. Crear un archivo serializers.py dentro de mi aplicación
2. Crear una clase que herede de ModelSerializer
3. Definir el modelo y los campos que se van a visualizar

Es posible que existan N serializadores, de acuerdo a la necesidad del negocio, es decir, a lo que queremos mostrar.

	class SubjectDetailSerializer(ModelSerializer):
	    teacher = TeacherSerializer(read_only=True)

	    class Meta:
	        model = Subject
	        fields = '__all__'

## Crear un ViewSet
Una ViewSetm, es un conjunto de vistas genericas para las acciones básicas de un endpoint: GET, POST, DELETE, UPDATE (list, retrive, destroy, update).

Para crear un viewset, es necesario definir una clase que herede de ModelViewSet y definir el queryset y el serializador que vamos a utilizar.

	class SubjectViewSet(ModelViewSet):
	    queryset = Subject.objects.all()
	    serializer_class = SubjectSerializer

## Actions
Es posible también, definir acciones especificas que nos permiten definir un comportamiendo adicional sobre un registro en particular o el conjunto de datos.

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

## Filtros
Podemos también, agregar lógica que nos permita filtrar información de nuestro endpoint con base en los campos de nuestro modelo.

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

El código anterior obtiene los parametros pasados a la vista y construye un objeto (parameters) que nos permite filtrar el queryset con dichos paremetros (subjects_filtered).

## Permisos
Es recomendable crear una clase independiente, en donde se gestione la lógica relacionada a los permisos de acceso a la vista o endpoint. Esta clase debe heredar de BasePermission y puede implementar cualquiera o ambos de los siguientes métodos.

	class SubjectPermissions(BasePermission):

	    def has_permission(self, request, view): # GET, POST, DELETE, PUT, actions
	        if request.user.is_staff:
	            return True
	        if not request.user.is_staff and view.action in ['list', 'students', 'retrieve']:
	            return True
	        if not request.user.is_staff and request.method in ['POST', 'DELETE', 'UPDATE']:
	            return False

	    def has_object_permission(self, request, view, obj):
	        if request.user.is_staff:
	            return True

	        if not request.user.is_staff and obj.owner == request.user:
	            return True

	        return False

El método has_permission, es un primer nivel de autorización donde validamos a nivel verbo HTTP, acción o usuario si tiene privilegios.

El método has_object_permission nos permite validar lo necesario a nivel registro, por ejemplo: validar si el usuario que hace la petición es dueño del registro.


## Celery
Es una herramienta que nos permite gestionar tareas de forma asincrona.

1. Instalar la librería
`pip install celery`

2. Crear el archivo de configuración de celery
```
	import os
	from celery import Celery
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

	app = Celery('proj')

	app.config_from_object('django.conf:settings', namespace='CELERY')

	app.autodiscover_tasks()
```

3. Importar la aplicación de Celery
```
	from .celery import app as celery_app

	__all__ = ('celery_app',)
```

4. Configurar el broker (RabbitMQ/Redis)
`CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'`

5. Crear las tareas
```
	from school.celery import app
	from core.utils import send_my_email


	@app.task(name='send_email_to_students')
	def send_email_to_students(students):
	    for student in students:
	        send_my_email(
	            'Bienvenido a la clase',
	            'Gracias por estar en la clase, espero que aprendas mucho',
	            'rob@gmail.com',
	            student.email
	        )

```


6. Ejecutar el worker
`celery -A proj worker -l info`

7. Invocar una tarea:
`send_email_to_students.apply_async(args=[serialized.data])`