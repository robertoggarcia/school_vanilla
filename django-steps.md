## Creando mi primer proyecto Django

### Crear ambiente

1. Crear un ambiente virtual
- python -m venv "nombre del ambiente"
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
`
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
`

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


Para ver una migración a nivel SQL, usar el siguiente comando:
python manage.py sqlmigrate "nombre de la aplicación" "número de migración"
`python manage.py sqlmigrate students 0001`


### Django admin
El administrador de Django nos permite gestionar de forma sencilla todo lo relacionado a los modelos. Es necesario contar con un super usuario de django.
`python manage.py createsuperuser`


Para visualizar los modelos de una aplicación, es necesario agregar los modelos al archivo admin.py de la aplicación.
`admin.site.register(Student)`


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
