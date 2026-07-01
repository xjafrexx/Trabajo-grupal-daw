// ==========================================
// 1. COMPONENTES COMUNES Y AUDITORÍA
// ==========================================
export interface AuditFields {
  id: string;
  status: boolean;
  created: string;
  modified: string;
  created_id: string;
  modified_id: string;
}

// Datos que exige Django para CREAR o EDITAR registros genéricos
export interface BaseInput {
  status: boolean;
  created_id: string;
  modified_id: string;
}

// ==========================================
// 2. CATEGORÍAS
// ==========================================
export interface CategoryListResponse extends AuditFields {
  categoryName: string;
  description: string;
}

export interface CategoryDetailResponse extends CategoryListResponse {
  books: { id: string; title: string }[];
}

export interface CategoryInput extends BaseInput {
  categoryName: string;
  description: string;
}

// ==========================================
// 3. AUTORES
// ==========================================
export interface AuthorListResponse extends AuditFields {
  fullName: string;
  nationality: string;
}

export interface AuthorDetailResponse extends AuthorListResponse {
  books: { id: string; title: string }[];
}

export interface AuthorInput extends BaseInput {
  fullName: string;
  nationality: string;
}

// ==========================================
// 4. LIBROS
// ==========================================
export interface BookListResponse {
  id: string;
  title: string;
  publishYear: string;
  status: string;
  created: string;
  modified: string;
  created_id: string;
  modified_id: string;
  authors: { id: string; fullName: string }[];
  categories: { id: string; categoryName: string }[];
}

export interface BookDetailResponse extends Omit<BookListResponse, 'status'> {
  status: boolean; // Notar que en detalle viene como booleano según tu Swagger
  total_copies: number;
  available_copies: number;
}

export interface BookInput extends BaseInput {
  title: string;
  publishYear: number;
  authors: string[]; // Lista de UUIDs
  categories: string[]; // Lista de UUIDs
}

// ==========================================
// 5. COPIAS DE LIBROS (BOOK COPIES)
// ==========================================
export interface BookCopyDetail extends AuditFields {
  book: {
    id: string;
    authors: string[];
    categories: string[];
    title: string;
    publishYear: number;
    status: boolean;
    created: string;
    modified: string;
    created_id: string;
    modified_id: string;
  };
  copyNumber: number;
  barcode: string;
  physicalCondition: string;
  is_available: boolean;
}

export interface BookCopyInput extends BaseInput {
  book: string; // UUID del libro
  copyNumber: number;
  barcode: string;
  physicalCondition: string;
  is_available: boolean;
}

// ==========================================
// 6. USUARIOS
// ==========================================
export interface UserResponse extends AuditFields {
  firstName: string;
  lastName: string;
  email: string;
  isAdmin: boolean;
}

// ==========================================
// 7. PRÉSTAMOS (LOANS)
// ==========================================
export interface LoanListResponse extends AuditFields {
  loanDate: string;
  dueDate: string;
  loanStatus: string;
  notes: string;
  returnDate: string | null;
  user: string; // ID plano
  book_copy: string; // ID plano
}

export interface LoanDetailResponse extends Omit<LoanListResponse, 'user' | 'book_copy'> {
  user: UserResponse; // Objeto anidado completo
  book_copy: BookCopyDetail; // Objeto anidado completo
}

export interface LoanInput extends BaseInput {
  loanDate: string;
  dueDate: string;
  loanStatus: string;
  notes: string;
  returnDate: string | null;
  user: string; // UUID
  book_copy: string; // UUID
}