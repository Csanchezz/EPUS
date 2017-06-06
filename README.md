EPUS
=====
de [Universidad del Valle de Guatemala - Campus Sur](http://campussur.uvg.edu.gt/)

### Easy Publication System

Sistema encargado de las publicaciones hechas en [UVG Campus Sur](http://campussur.uvg.edu.gt/).

## Dependencias

- Python 3
- pip
- Django 1.10
- MySQL
- virtualenv

## Instalación

#### Obtener el código
Clonar este repositorio:
```
https://github.com/Csanchezz/EPUS.git
```

#### Preparar el entorno
Entrar a la carpeta del repositorio (`cd EPUS`) y crear una carpeta llamada `etc`. En esa carpeta, crear un ambiente virtual con `virtualenv` llamado `venv`
```
virtualenv venv --no-site-packages --distribute
```
Activar el ambiente virtual con
```
source venv/bin/activate (linux)
venv\scripts\activate (windows)
```

#### Instalar dependencias de Python
Regresar a la carpeta raíz (`EPUS`) y instalar las dependencias con pip
```
pip install -r requirements.txt
```

#### Ejecutar el servidor
Ejecutar el servidor con el archivo manage.py desde la raíz.
```
python3 src/manage.py runserver 0.0.0.0:8000
```

#### Ejecutar el servidor dev
Ejecutar el servidor con el archivo manage.py desde la raíz.
```
python3 src/manage.py runserver 0.0.0.0:8000 --settings=src.settings_dev
=======
#### Ejecutar el servidor con la base de datos en
Escribir esto en settings_dev.py
```
Cambiar la raíz en
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

## Estructura del sistema
De forma ideal, las carpetas del sistema se verán así

```
.
├── etc
│   ├── media
│   └── venv
├── src
│   ├── apps
│   ├── fix
│   ├── src
│   ├── static
│   ├── templates
│   └── manage.py
├── README.md
└── requirements.txt
```
