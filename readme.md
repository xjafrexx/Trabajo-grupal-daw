# 📚 Sistema de Gestión de Biblioteca - Frontend

Este proyecto es el desarrollo del frontend para el Sistema de Administración de una Biblioteca, construido con un enfoque moderno, robusto y fuertemente tipado. Se conecta a un backend desarrollado en Django para la persistencia de datos.

---

## 🛠️ Tecnologías Utilizadas

* **React + Vite:** Entorno de desarrollo rápido y eficiente.
* **TypeScript:** Type-checking estricto para garantizar la integridad de los datos.
* **TanStack Query (React Query) v5:** Gestión de estado asíncrono, almacenamiento en caché reactivo e invalidación de consultas en tiempo real.
* **React Router DOM v6:** Enrutamiento dinámico en el lado del cliente.
* **Axios:** Cliente HTTP para la comunicación con el servidor.

---

## 🚀 Progreso del Proyecto

Hasta el momento, el desarrollo ha completado las siguientes etapas del mapa de ruta:

### 1. Inicialización y Configuración
* Configuración inicial del entorno utilizando React con Vite y soporte total para TypeScript.

### 2. Capa de Servicios y Tipos (API)
* Definición estricta de interfaces TypeScript mapeadas uno a uno con el esquema de Django (`BaseInput`, `AuditFields`, `BookInput`, `BookCopyInput`, `LoanInput`, etc.).
* Implementación de servicios HTTP modulares independientes para Autores, Categorías, Libros, Copias y Préstamos.

### 3. Implementación de Hooks React Query
* Creación de Custom Hooks optimizados para operaciones CRUD completas (`useQuery` y `useMutation`).
* Configuración de estrategias de sincronización de caché automatizadas: al hacer operaciones de escritura (`POST`, `PATCH`, `DELETE`), la caché de datos se invalida y se actualiza en la interfaz de usuario en segundo plano de manera inmediata.
* Manejo correcto de respuestas HTTP específicas, incluyendo códigos de estado sin contenido (`204 No Content`).

### 4. Creación de Componentes y Vistas Base
* **Dashboard Central:** Panel de control administrativo que calcula métricas en tiempo real a partir de la caché de datos (total de libros, copias, préstamos activos).
* **Vistas de Navegación:** Separación de componentes con cabeceras especializadas (`AdminHeader` y `HomeHeader`).
* **Estructura HTML Pura:** Interfases funcionales diseñadas con HTML minimalista para validar la lógica del sistema antes de la fase estética.

### 5. Configuración de Rutas
* Implementación de enrutamiento dinámico mediante `BrowserRouter`.
* Aislamiento completo entre la vista pública para lectores (`/`) y la plataforma de administración interna (`/admin`).

---

## Gestión del Repositorio (Git)

El proyecto se encuentra organizado y respaldado bajo la siguiente rama de entrega:
* **Rama:** `lab09-proyecto-basico`

---

## Próximos Pasos

 **Corregir y formalizar el proyecto**