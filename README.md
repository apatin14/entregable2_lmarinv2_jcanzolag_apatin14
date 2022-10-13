## Informacion de la materia:

- ST0263 TOPICOS EN TELEMATICA

## Estudiante(s):

- Andres Danilo Patiño Velez, apatin14@eafit.edu.co
- Juan Camilo Anzola Gomez, jcanzolag@eafit.edu.co
- Laura Marin Velez, lmarinv2@eafit.edu.co

## Profesor:

- Edwin Nelson Montoya Munera

## Actividad:

- Entregable Proyecto 1 - Final

## 1. breve descripción de la actividad

Desplegar un servidor con particionamiento y replicación con el fin de afianzar los conocimientos
desarrollados en la sesión de clases.

### 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

- Implementacion de API y routingtire
- Guardado de datos en varias particiones (Base de datos en cache)
- Replicacion de datos en las diferentes particiones (Base de datos en cache)
- Incluir una interfaz de usuario para el uso del sistema

### 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

## 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.


### como se compila y ejecuta.

#### Main class

- py main.py

### detalles del desarrollo.

El desarrollo esta generado en python con una arquitectura Cliente/Servidor, en la cual se encuentra en la raiz el archivo correspondiente a las variables de entorno `.env` la cual contiene la configuracion de la aplicacion.

### opcional - detalles de la organización del código por carpetas o descripción de algún archivo. (ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO, comando 'tree' de linux)

- 📁./
-  |
- ├─📁db_client
    ├─💽app.py
    ├─💽hashing256.py
    ├─💽serialize.py
- ├─📁router_server
    ├─💽hashTable.py
    ├─💽routing.py
- ├─📁routes
    ├─💽record_routes.py
- ├─📁schemas
    ├─💽record.py
- ├─💽.env
- ├─💽README.MD
- ├─💽main.py
- ├─💽requirements.txt
- ├─💽


## 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

Lista de requisitos de python [aca](https://github.com/apatin14/entregable2_lmarinv2_jcanzolag_apatin14/blob/master/requirements.txt)

## IP o nombres de dominio en nube o en la máquina servidor.

[proyecto1](52.204.153.196)

## como se lanza el servidor.

Ejecutando el comando para lanzar la instancia de AWS
Ejecutando el comando para hacer reload del nginx
Ejecutando el comando para lanzar el servicio de gunicorn



## una mini guia de como un usuario utilizaría el software o la aplicación

Se puede abrir la direccion https://52.204.153.196, acontinuacion debe agregar /docs dentro de la misma url

en caso de ser encontrado el servidor mostrar el archivo
en caso contrario monstrar la pantalla de error 404

si se accede bajo un protocolo no valido mostrar un error

#### versión README.md -> 1.0 (2022-Octubre)