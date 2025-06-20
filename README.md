# course-django

#### Primeros pasos 
#### Primeros pasos

1. Verifica que tienes Python instalado:
    ```sh
    python3 --version
    ```
    Deberías ver la versión de Python instalada (por ejemplo, Python 3.12.1).

2. Verifica que tienes pip instalado:
    ```sh
    pip --version
    ```
    Deberías ver la versión de pip instalada (por ejemplo, pip 24.0).

Si no tienes Python o pip, puedes instalarlos usando [Homebrew](https://brew.sh/) en Mac:
```sh
brew install python
```
MAC con homebrew: 
```
# Crear entorno virtual
python3 -m venv nombre_proyecto

# Activar
source nombre_proyecto/bin/activate # Linux y Mac
.\venv\Scripts\activate # Windows

# Instalar paquetes
pip install lo-que-necesites

# Desactivar
deactivate
```

### Crear proyecto en Django

1. **Instalar Django**  
    Instala Django en tu entorno virtual:
    ```sh
    pip install django
    ```
    Puedes especificar la version de django en **./requirements.txt**
    ```
    pip install -r requirements.txt
    ```

2. **Crear un nuevo proyecto**  
    Crea un nuevo proyecto llamado `core` en el directorio actual:
    ```sh
    django-admin startproject core .
    ```
    > El punto (`.`) al final indica que el proyecto se creará en el directorio actual.

3. **Verifica la estructura del proyecto**  
    Se crearán archivos y carpetas como `manage.py` y una carpeta llamada `core` con la configuración del proyecto.

4. **Iniciar el servidor de desarrollo**  
    Ejecuta el servidor para comprobar que todo funciona correctamente:
    ```sh
    python manage.py runserver
    ```
    > Accede a http://127.0.0.1:8000/ en tu navegador para ver el proyecto en funcionamiento.

5. **Ejecutar migraciones**
```
python manage.py migrate
```

5. **Crear un usuario administrador**
```
python manage.py createsuperuser
username: admin
email: mail@admin.com
password: admin123
```
6. Se agrega una vista (views.py), se crea un folder para templates, se configura en settings.py. y se crea una url para la nueva vista.

7. Proteger información sensible en settings.py mediante django-environ
    ```
    pip instalar django-environ
    ```
    o desde requirements.txt 
    - crear .env en core
    - configurar en settings.py 
    ```
    import environ
    # Set up environment variables
    env = environ.Env()
    # Read .env file
    environ.Env.read_env()  

    # ejemplos de uso:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = os.environ.get('DEBUG', default=False)
    ```

### Crear App Blog
```
# No olvidar trabajar en el ambiente virtual (venv)
python manage.py startapp blog
```

1. Agregar nuestra App en /core/settings.py # INSTALLED_APPS = []
2. Crear nuestro archivo de urls.py en la App Blog con la estructura base.
```
from django.urls import path

app_name="blog"

urlpatterns = [
    
]
```

3. Agregar un nuevo path en /core/urls.py 
``` 
path('blog/', include('blog.urls', namespace='blog'))
```
4. Crear vista para listar blogs
5. Crear el template para listar blogs
6. Crear el Modelo de Post en /blog/models.py
7. Crear archivo de migraciones
```
python manage.py makemigrations blog
```
8. Ejecutar las migraciones
```
python manage.py migrate
```
9. Registrar el modelo Post en Admin
Esto nos permite hacer crud como Admin
- Ir a /blog/admin.py y agregar:
```
from .models import Post
admin.site.register(Post)
```
10. **Crud desde la Web**

- Crear formulario en blog/forms.py
- Crear Vista para el formulario
- Crear Template
- Crear url 

11. Usar Tailwind CSS
- Se busca en [django-tailwind](https://pypi.org/project/django-tailwind/) 
- Se agrega al archivo requirementes.txt
- [Link de la documentación](https://django-tailwind.readthedocs.io/en/latest/installation.html)






