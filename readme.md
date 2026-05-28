# Laboratorio 05 : Django admin
| Autores |
| :--- | 
| Jafet Macedo Orozco | 
| Angel Paúl Apaza Nazareth | 
| Eddy Alvaro Muto Montesinos | 

# Descripción de la práctica
- Mostrar el modelo de datos resumido para su proyecto final. (Recomendación: 4-7 tablas)
- Utilizar un entorno virtual para el proyecto de Python Django. (Crear y enviar requirements.txt)
- Crear un proyecto Django y una aplicación con las siglas del proyecto. (Ejemplo: para un sistema académico podría llamarse **sisacad**)
- Crear modelos en archivos independientes.
- Redefinir el método **def save()** de los modelos para realizar operaciones previas de guardado de registro.
- Redefinir el método **def __str__()** para seleccionar atributos específicos de los registros existentes.
- Crear las funciones necesarias para aplicar restricciones desde el Modelo. (Ejemplo: **validators=[validate_even])**)
- Capturar capturas de pantalla de los auto CRUDs generados por Django Admin. (Explique todo el proceso. Ejemplo: Crear profesor, crear curso, asignar curso a un profesor, ...)
- Elaborar README.md.

#  Sistema de Gestión de Biblioteca (sislib)

Este proyecto corresponde al desarrollo del backend para el sistema de gestión de una biblioteca, implementado con **Django** como framework principal.

---

# 1. Descripción del Modelo de Datos
El sistema consta de 8 tablas principales que modelan el flujo completo de una biblioteca, organizadas alfabéticamente en el caso de las relaciones Muchos a Muchos (N:M). Todas las entidades incorporan campos de auditoría (status, created, modified, created_id, modified_id) y llaves primarias basadas en identificadores únicos globales (UUID).

- users: Almacena los lectores y administradores (isAdmin) del sistema.

- authors: Registro de escritores de los libros.

- categories: Géneros literarios o clasificaciones disponibles.

- books: Catálogo general de obras indexadas.

- authors_books: Tabla relacional (N:M) ordenada alfabéticamente que vincula libros con coautores.

- books_categories: Tabla relacional (N:M) ordenada alfabéticamente que clasifica libros en múltiples categorías.

- book_copies: Inventario físico de ejemplares disponibles en estanterías, permitiendo rastrear su estado individual.

- loans: Registra las transacciones de salida y retorno de ejemplares físicos por parte de los usuarios.


##  2. Entorno Virtual y Dependencias

Para el aislamiento de las librerías del proyecto, se utilizó un entorno virtual de Python. Las dependencias requeridas se encuentran consolidadas en el archivo `requirements.txt`.

### Instrucciones de despliegue:
```bash
# 1. Clonar el repositorio
git clone <https://github.com/xjafrexx/Trabajo-grupal-daw.git
cd Trabajo-grupal-daw/sislib

# 2. Crear y activar el entorno virtual
python3 -m venv myvenv
source myvenv/bin/activate  

# 3. Instalar dependencias necesarias
pip install -r requirements.txt

# 4. Ejecutar migraciones e iniciar servidor
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
# Crear un proyecto Django y una aplicación con las siglas del proyecto
Se estructuró el proyecto raíz bajo el nombre del sistema institucional sislib y la aplicación interna encargada de la lógica de negocio usando las siglas reglamentarias: applib.

# Estructura de Modelos Decoupled (Archivos Independientes)
Siguiendo las mejores prácticas de modularidad, la aplicación applib no concentra su estructura en un único models.py. Se modularizó mediante un paquete de Python estructurado de la siguiente manera:

```text
WebApps/applib/models/
├── __init__.py
├── authors_books.py
├── authors.py
├── book_copies.py
├── books_categories.py
├── books.py
├── categories.py
├── loans.py
└── users.py
```
# Redefinir el método def save() de los modelos
# Redefinir el método def str()
# Crear las funciones necesarias para aplicar restricciones desde el Modelo (Validators)
Las reglas críticas de negocio se validan antes de persistir los datos mediante funciones validadoras enlazadas directamente a las columnas.

validate_publish_year: Impide que se guarden libros con un año de publicación superior al año en curso.

```bash
def validate_publish_year(value):
    if value > timezone.now().year:
        raise ValidationError('El año de publicación no puede ser en el futuro.')
```
# Creacion de Super Usuario
```bash
Username (leave blank to use 'lab6'): admin
Email address: 
Password: 1234
Password (again): 1234 
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```