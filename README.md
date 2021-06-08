# Project-Selva

# Guia para poder correr el proyecto:

1. Clonar este repositorio en una carpeta local.
2. Abrir una cmd.
3. Moverse a la carpeta del proyecto(_cd C:.../src_)
4. Ejecutar el comando **_pipenv install_**
5. Ejecutar el comando _pipenv shell_ 

Ya dentro de la shell de pip y con todo instalado, podemos proceder a abrir el server ejecutando el comando: _py manage.py runserver_


# Guia para plasmar cambios en el dominio:

1. Abrir una pipenv shell en la carpeta _/src_
2. Ejecutar el comando _py manage.py makemigrations SelvaPampa_
3. Si todo salio bien, Ejecutar _py manage.py migrate SelvaPampa_

Si no hubo algun error en la migracion, deberia haber plasmado todos los cambios a la base de datos que este seleccionada en el archivo de configuracion seleccionado. 

**Si se quiere utilizar otra configuracion, se deberá aclarar en el manage.py.**


