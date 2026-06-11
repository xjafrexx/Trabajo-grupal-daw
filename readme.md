# Laboratorio 08 : Django REST Framework
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
- Capturar capturas de pantalla de los auto CRUDs generados por Django Admin. (Explique todo el proceso. Ejemplo: Crear profesor, crear curso, asignar curso a un profesor, ...)
- Elaborar README.md.
#  Sistema de Gestión de Biblioteca (sislib)

Este proyecto corresponde al desarrollo del backend para el sistema de gestión de una biblioteca, implementado con **Django** como framework principal.

# Sistema de Gestión de Biblioteca (sislib) - API REST 


##  Requisitos e Instalación

### 1. Activar el Entorno Virtual
Asegúrese de inicializar su entorno virtual antes de ejecutar los comandos del framework.

**En GNU/Linux:**
```bash
source my_env/bin/activate
```
**En MS Windows:**
```bash
source my_env/bin/activate
my_env\Scripts\activate.bat
```
### 2. Instalar dependencias
Instale Django REST Framework y los componentes necesarios registrados en el archivo de requerimientos:
```bash
pip install -r requirements.txt
```
### 3. Aplicar Migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```
### 4. Desplegar el navegador
```bash
python manage.py runserver
```
## Endpoints de la API REST

| Método HTTP        | Endpoint               | Descripción                                                                                                                                |
| ------------------ | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| GET / POST         | `/api/users`           | Listar usuarios / Registrar un nuevo usuario (Modo Plano).                                                                                 |
| GET / PUT / DELETE | `/api/users/{id}`      | Detalle, actualización y eliminación de un usuario por UUID.                                                                               |
| GET / POST         | `/api/authors`         | Listar autores / Registrar un nuevo autor.                                                                                                 |
| GET / PUT / DELETE | `/api/authors/{id}`    | Detalle, actualización y eliminación de un autor.                                                                                          |
| GET / POST         | `/api/categories`      | Listar categorías / Registrar una categoría literaria.                                                                                     |
| GET / PUT / DELETE | `/api/categories/{id}` | Detalle, actualización y eliminación de una categoría.                                                                                     |
| GET / POST         | `/api/books`           | Listar libros (Modo Plano) / Registrar un nuevo libro.                                                                                     |
| GET                | `/api/books/{id}`      | Consulta Compleja (Detalle Anidado): muestra el libro con sus copias físicas asociadas.                                                    |
| GET / POST         | `/api/book-copies`     | Listar copias de libros / Registrar una copia física.                                                                                      |
| GET / POST         | `/api/loans`           | Listar préstamos activos / Registrar un nuevo préstamo.                                                                                    |
| GET                | `/api/loans/{id}`      | Consulta Compleja (Detalle Anidado): devuelve el préstamo junto con la información detallada del usuario y la copia del libro involucrada. |



