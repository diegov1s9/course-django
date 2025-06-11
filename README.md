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
source nombre_proyecto/bin/activate
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
