# mural91

## Descripción del Proyecto

El proyecto **mural91** es una aplicación web desarrollada con FastAPI para la gestión y visualización de actividades semanales. La aplicación permite a los administradores crear y gestionar actividades, mientras que los usuarios pueden consultar el mural91. La aplicación utiliza SQLite como sistema de gestión de bases de datos.

## Estructura del Proyecto

A continuación se describe la estructura del proyecto y la funcionalidad de cada módulo y archivo.

### Directorio Principal


### Directorio `app/`
Este directorio contiene el código fuente principal de la aplicación.

- **`__init__.py`**: Inicializa el paquete de la aplicación.
- **`main.py`**: Archivo principal para ejecutar la aplicación. Configura y arranca el servidor FastAPI.

#### Directorio `models/`

Contiene los modelos de datos utilizados por SQLAlchemy para la base de datos.

- **`__init__.py`**: Inicializa el paquete de modelos.
- **`activity.py`**: Define el modelo para las actividades. Incluye la estructura de la tabla de actividades en la base de datos.
- **`user.py`**: Define el modelo para los usuarios, incluyendo campos para administradores y usuarios normales.
- **`role.py`**: Define los roles de usuario (por ejemplo, administrador, usuario) para gestionar permisos.

#### Directorio `schemas/`

Contiene los esquemas de Pydantic para la validación y serialización de datos.

- **`__init__.py`**: Inicializa el paquete de esquemas.
- **`activity.py`**: Esquemas para la validación de datos relacionados con actividades (e.g., creación, actualización).
- **`user.py`**: Esquemas para la validación de datos de usuarios (e.g., registro, actualización de perfil).
- **`token.py`**: Esquemas para la gestión de tokens JWT utilizados en la autenticación.

#### Directorio `routes/`

Contiene las rutas y endpoints de la API.

- **`__init__.py`**: Inicializa el paquete de rutas.
- **`activity.py`**: Endpoints relacionados con la gestión de actividades (e.g., creación, consulta, actualización, eliminación).
- **`user.py`**: Endpoints relacionados con la gestión de usuarios (e.g., perfil de usuario, actualización de información).
- **`auth.py`**: Endpoints para autenticación y gestión de usuarios (e.g., inicio de sesión, registro, recuperación de contraseñas).

#### Directorio `db/`

Contiene la configuración y el manejo de la base de datos.

- **`__init__.py`**: Inicializa el paquete de base de datos.
- **`database.py`**: Configuración de la conexión a la base de datos SQLite y la creación del motor de base de datos. Incluye la configuración de SQLAlchemy y la creación de la base de datos.

#### Directorio `services/`

Contiene la lógica de negocio y servicios auxiliares.

- **`__init__.py`**: Inicializa el paquete de servicios.
- **`activity_service.py`**: Lógica de negocio relacionada con las actividades, incluyendo operaciones como la creación, actualización y eliminación.
- **`user_service.py`**: Lógica de negocio relacionada con los usuarios, incluyendo operaciones como la creación de usuarios y la gestión de perfiles.
- **`auth_service.py`**: Lógica de autenticación, incluyendo la generación y validación de tokens JWT y la gestión de contraseñas.

#### Directorio `core/`

Contiene la configuración de la aplicación, funciones de seguridad y dependencias compartidas.

- **`__init__.py`**: Inicializa el paquete de núcleo.
- **`security.py`**: Funciones de seguridad, como el hashing de contraseñas y la gestión de tokens JWT.
- **`config.py`**: Configuración general de la aplicación, incluyendo variables de entorno y parámetros de configuración.
- **`dependencies.py`**: Funciones y dependencias compartidas que pueden ser utilizadas en diferentes partes de la aplicación.

### Directorio `alembic/`

Contiene archivos para la gestión de migraciones de base de datos con Alembic.

- **`versions/`**: Directorio para las migraciones de la base de datos.
- **`env.py`**: Configuración de Alembic.
- **`README`**: Documentación sobre el uso de Alembic.

### Directorio `tests/`

Contiene pruebas unitarias y de integración para asegurar el correcto funcionamiento de la aplicación.

- **`__init__.py`**: Inicializa el paquete de pruebas.
- **`test_activity.py`**: Pruebas para los endpoints y servicios relacionados con las actividades.
- **`test_user.py`**: Pruebas para los endpoints y servicios relacionados con los usuarios.
- **`test_auth.py`**: Pruebas para la autenticación y gestión de sesiones.

### Archivos Principales

- **`.env`**: Archivo para almacenar variables de entorno (como credenciales de base de datos y configuraciones sensibles).
- **`.gitignore`**: Configuración para ignorar archivos no deseados en el control de versiones.
- **`requirements.txt`**: Lista de dependencias del proyecto.
- **`README.md`**: Documentación general del proyecto.

## Cómo Ejecutar el Proyecto

1. **Configura el entorno**:
   - Crea un archivo `.env` con las variables de entorno necesarias.

2. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt


