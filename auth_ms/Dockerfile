# Va a hub.docker.com y descarga la imagen de Python, con tag 3 (version)
FROM python:3
# Variables de entorno de Python
ENV PYTHONUNBUFFERED 1
# RUN (Ejecutar), crear una carpeta llamada users
RUN mkdir /users
# Directorio de trabajo
WORKDIR /users
# Aqui va a agregar la aplicacion para su ejecucion
ADD . /users/
# Instalar los paquetes python desde el archivo requirement.txt
RUN pip install -r requirements.txt
# Exponer en el puerto 8080 (escribir en $PORT)
EXPOSE 8080
# Instrucciones de migracion
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:$PORT