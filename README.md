# Laboratorio 05 : Base de datos
| Autores | Rol | Porcentaje |
| :--- | :--- | :---: |
| Richart Escobedo | Elaboración del modelo lógico DER | 100% |
| Richart Escobedo | Implementación del modelo físico PostgreSQL | 100% |
| Richart Escobedo | Implementación en Supabase | 100% |
| Richart Escobedo | Elaboración del informe | 100% |
| | **Total** | **100%** |

| Entregables | URL |
| :--- | :--- |
| Repositorio | https://github.com/rescobedoq/enrollments.git |
| Informe | https://github.com/rescobedoq/enrollments/blob/main/informes/DAW_lab05_bd.pdf |

# Descripción de la práctica
- Elaboración del modelo lógico DER.
- Implementación del modelo físico PostgreSQL.
- Implementación en Supabase - Backend como servicio disponible en la nube.
- Elaborar README.md.
##  1. Modelo Lógico (Diagrama Entidad-Relación - DER)

El siguiente diagrama representa de forma gráfica cómo se conectan las tablas de nuestra biblioteca.

![Diagrama Entidad Relación de la Biblioteca](./supabase/modelo_DER.png)

---
## 2. Creación de la Tablas:

Creamos la tabla `users` 

```sql
-- TABLA 1: users 
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    is_admin BOOLEAN DEFAULT false,
    
    -- Columnas obligatorias de auditoría
    status BOOLEAN DEFAULT true,
    created TIMESTAMP WITH TIME ZONE DEFAULT now(),
    modified TIMESTAMP WITH TIME ZONE DEFAULT now(),
    created_id UUID, 
    modified_id UUID
);

-- TABLA 2: authors
CREATE TABLE authors (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    full_name TEXT NOT NULL,
    nationality TEXT,
    
    -- Columnas obligatorias de auditoría
    status BOOLEAN DEFAULT true,
    created TIMESTAMP WITH TIME ZONE DEFAULT now(),
    modified TIMESTAMP WITH TIME ZONE DEFAULT now(),
    created_id UUID REFERENCES users(id),
    modified_id UUID REFERENCES users(id)
);

-- TABLA 3: categories 
CREATE TABLE categories (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    category_name TEXT NOT NULL,
    description TEXT,
    
    -- Columnas obligatorias de auditoría
    status BOOLEAN DEFAULT true,
    created TIMESTAMP WITH TIME ZONE DEFAULT now(),
    modified TIMESTAMP WITH TIME ZONE DEFAULT now(),
    created_id UUID REFERENCES users(id),
    modified_id UUID REFERENCES users(id)
);

-- TABLA 4: books 
CREATE TABLE books (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title TEXT NOT NULL,
    publish_year INTEGER,
    
    -- Llaves foráneas (1 a muchos)
    author_id UUID REFERENCES authors(id) ON DELETE RESTRICT,
    category_id UUID REFERENCES categories(id) ON DELETE RESTRICT,
    
    -- Columnas obligatorias de auditoría
    status BOOLEAN DEFAULT true,
    created TIMESTAMP WITH TIME ZONE DEFAULT now(),
    modified TIMESTAMP WITH TIME ZONE DEFAULT now(),
    created_id UUID REFERENCES users(id),
    modified_id UUID REFERENCES users(id)
);

-- TABLA 5: book_copies
CREATE TABLE book_copies (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    book_id UUID NOT NULL REFERENCES books(id) ON DELETE RESTRICT, 
    barcode TEXT UNIQUE NOT NULL,
    physical_condition TEXT NOT NULL DEFAULT 'Bueno', -- Ejemplos: 'Bueno', 'Dañado', 'Desgastado'
    is_available BOOLEAN NOT NULL DEFAULT true,
    
    -- Columnas obligatorias de auditoría
    status BOOLEAN DEFAULT true,
    created TIMESTAMP WITH TIME ZONE DEFAULT now(),
    modified TIMESTAMP WITH TIME ZONE DEFAULT now(),
    created_id UUID REFERENCES users(id),
    modified_id UUID REFERENCES users(id)
);

-- TABLA 6: loans
CREATE TABLE loans (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE RESTRICT,
    book_copy_id UUID REFERENCES book_copies(id) ON DELETE RESTRICT, 
    loan_date DATE NOT NULL DEFAULT current_date,
    due_date DATE NOT NULL DEFAULT (current_date + INTERVAL '14 days'),
    return_date DATE,
    loan_status TEXT NOT NULL DEFAULT 'Activo', -- Ejemplos: 'Activo', 'Devuelto', 'Vencido'
    notes TEXT,
    
    -- Columnas obligatorias de auditoría
    status BOOLEAN DEFAULT true,
    created TIMESTAMP WITH TIME ZONE DEFAULT now(),
    modified TIMESTAMP WITH TIME ZONE DEFAULT now(),
    created_id UUID REFERENCES users(id),
    modified_id UUID REFERENCES users(id)
);

```

## 3. Infraestructura y Tecnología: Supabase

Para el despliegue y gestión de la base de datos, el proyecto utiliza **Supabase**, una plataforma de desarrollo de código abierto que funciona como **Backend como servicio (BaaS)** disponible completamente en la nube. 

* **Base de Datos Gestionada:** Al estar hospedado en la nube, PostgreSQL se ejecuta sin necesidad de configurar servidores locales, garantizando alta disponibilidad y respaldos automáticos.
* **Autenticación Nativa (Supabase Auth):** Facilita la creación y control de accesos de los usuarios, conectándose de forma directa con nuestra lógica de permisos y la columna `is_admin` de la tabla `users`.
* **API REST Automatizada:** Supabase genera instantáneamente una API segura a partir de nuestras tablas (`users`, `books`, `loans`, etc.), permitiendo que cualquier aplicación Frontend (web o móvil) pueda consultar o registrar datos de la biblioteca de inmediato.
* **Consola de Administración Visual:** Permite al equipo monitorear el inventario de libros, verificar préstamos activos y auditar registros mediante una interfaz gráfica intuitiva (Table Editor) y un editor SQL centralizado.

---