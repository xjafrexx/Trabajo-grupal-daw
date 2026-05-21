##  1. Modelo Lógico (Diagrama Entidad-Relación - DER)

El siguiente diagrama representa de forma gráfica cómo se conectan las tablas de nuestra biblioteca.

![Diagrama Entidad Relación de la Biblioteca](./supabase/Modelo_DER.png)

---
### Creación de la Tablas:

Creamos la tabla `users` 

```sql
create table users (
    id uuid primary key default gen_random_uuid(),
    "firstName" text not null,
    "lastName" text not null,
    email text unique not null,
    
    -- Columnas obligatorias de auditoría
    status boolean default true,
    created timestamp with time zone default now(),
    modified timestamp with time zone default now(),
    created_id uuid, 
    modified_id uuid
);

Creamos la tabla `authors` 

create table authors (
    id uuid primary key default gen_random_uuid(),
    "fullName" text not null,
    nationality text,
    
    -- Columnas obligatorias de auditoría
    status boolean default true,
    created timestamp with time zone default now(),
    modified timestamp with time zone default now(),
    created_id uuid references users(id),
    modified_id uuid references users(id)
);

Creamos la tabla `categories`

create table categories (
    id uuid primary key default gen_random_uuid(),
    "categoryName" text not null,
    description text,
    
    -- Columnas obligatorias de auditoría
    status boolean default true,
    created timestamp with time zone default now(),
    modified timestamp with time zone default now(),
    created_id uuid references users(id),
    modified_id uuid references users(id)
);

Creamos la tabla `books`

create table books (
    id uuid primary key default gen_random_uuid(),
    title text not null,
    "publishYear" integer,
    
    -- Llaves foráneas (1 a muchos)
    author_id uuid references authors(id) on delete restrict,
    category_id uuid references categories(id) on delete restrict,
    
    -- Columnas obligatorias de auditoría
    status boolean default true,
    created timestamp with time zone default now(),
    modified timestamp with time zone default now(),
    created_id uuid references users(id),
    modified_id uuid references users(id)
);

Creamos la tabla `loans`

create table loans (
    id uuid primary key default gen_random_uuid(),
    user_id uuid references users(id) on delete restrict,
    book_id uuid references books(id) on delete restrict,
    "loanDate" date not null default current_date,
    "returnDate" date,
    
    -- Columnas obligatorias de auditoría
    status boolean default true,
    created timestamp with time zone default now(),
    modified timestamp with time zone default now(),
    created_id uuid references users(id),
    modified_id uuid references users(id)
);