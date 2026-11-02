# PROYECTO IMCOMPLETO

### Inicializar git:

git init

git add .

git status

On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   Prueba.txt


git commit -m "primer commit texto prueba"

git status

git remote add origin https://github.com/

git branch -M main

git push -u origin main


### REQ01

#### Entorno Virtual (venv) e Instalación de Dependencias
python -m venv venv
- Activación (Windows): venv\Scripts\activate
- Activación (Mac/Linux): source venv/bin/activate

pip install django

#### Creación del Proyecto Django
django-admin startproject comunidad_conecta .

El contenedor global que configura todo el sitio web. No contiene la lógica de negocio todavía, sino los archivos globales de configuración (settings.py), el enrutador principal (urls.py) y los puntos de entrada para servidores web (wsgi.py / asgi.py).

¿Por qué el punto (.) al final? Por defecto, el comando startproject crea una carpeta extra con el nombre del proyecto. Agregar el punto le indica a Django que inicialice los archivos de configuración directamente en la carpeta actual de trabajo (la que ya tienes conectada a tu repositorio de Git), evitando anidar carpetas innecesarias y facilitando la estructura del proyecto.

#### Creación de la Aplicación (App) y Registro
python manage.py startapp correspondencia

(Y registrar 'correspondencia' en INSTALLED_APPS dentro de settings.py)

Diferencia entre Proyecto y Aplicación: En la filosofía de Django, un Proyecto es el sitio web completo, mientras que una Aplicación (App) es un módulo o componente independiente y reutilizable encargado de una tarea específica (siguiendo el principio de responsabilidad única). Para el caso de ComunidadConecta, creamos la app correspondencia para manejar la lógica de las encomiendas, conserjes y residencias.

¿Por qué registrarla en INSTALLED_APPS? Django utiliza un patrón modular. Aunque crees la carpeta con los archivos de la app, Django no sabrá que existe a menos que la declares explícitamente en el archivo settings.py. Al registrarla, permites que Django detecte sus modelos de bases de datos, sus migraciones, sus templates y sus archivos estáticos.

#### Migraciones Iniciales y Servidor de Desarrollo
python manage.py migrate
python manage.py runserver

¿Qué son las migraciones y por qué ejecutarlas (migrate)? Django viene por defecto con aplicaciones internas ya instaladas (como el sistema de autenticación de usuarios, sesiones y el panel de administración). Estas aplicaciones requieren tablas en la base de datos (por defecto SQLite). El comando migrate toma los archivos de esquemas de bases de datos de Django y los traduce/ejecuta en el motor de base de datos para crear dichas tablas físicas.

¿Qué hace el servidor local (runserver)? Levanta un servidor web de desarrollo ligero integrado en Python (basado en WSGI/ASGI) corriendo normalmente en [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Su propósito es permitirte probar el código en tiempo real en tu navegador web de forma local, recargándose automáticamente cuando modificas archivos de código, sin necesidad de configurar servidores pesados de producción como Nginx o Apache en esta etapa de desarrollo.
