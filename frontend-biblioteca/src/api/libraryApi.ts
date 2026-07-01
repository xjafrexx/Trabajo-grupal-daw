import type {
  CategoryListResponse, CategoryDetailResponse, CategoryInput,
  AuthorListResponse, AuthorDetailResponse, AuthorInput,
  BookListResponse, BookDetailResponse, BookInput,
  BookCopyDetail, BookCopyInput,
  UserResponse,
  LoanListResponse, LoanDetailResponse, LoanInput
} from '../types/library';

const API_BASE_URL = 'http://localhost:8000/api';

// Función auxiliar para manejar respuestas fetch
async function handleResponse<T>(response: Response): Promise<T> {
  if (!response.ok) {
    throw new Error(`Error en la petición: ${response.statusText}`);
  }
  if (response.status === 24) return {} as T; // Manejo de No Content (Delete)
  return response.json();
}

export const libraryApi = {
  // === CATEGORÍAS ===
  getCategories: () => fetch(`${API_BASE_URL}/categories/`).then(res => handleResponse<CategoryListResponse[]>(res)),
  getCategory: (id: string) => fetch(`${API_BASE_URL}/categories/${id}/`).then(res => handleResponse<CategoryDetailResponse>(res)),
  createCategory: (data: CategoryInput) => fetch(`${API_BASE_URL}/categories/`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data)
  }).then(res => handleResponse<CategoryListResponse>(res)),
  updateCategory: (id: string, data: Partial<CategoryInput>) => fetch(`${API_BASE_URL}/categories/${id}/`, {
    method: 'PATCH', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data)
  }).then(res => handleResponse<CategoryListResponse>(res)),
  deleteCategory: (id: string) => fetch(`${API_BASE_URL}/categories/${id}/`, { method: 'DELETE' }).then(res => handleResponse<void>(res)),

  // === AUTORES ===
  getAuthors: () => fetch(`${API_BASE_URL}/authors/`).then(res => handleResponse<AuthorListResponse[]>(res)),
  getAuthor: (id: string) => fetch(`${API_BASE_URL}/authors/${id}/`).then(res => handleResponse<AuthorDetailResponse>(res)),
  createAuthor: (data: AuthorInput) => fetch(`${API_BASE_URL}/authors/`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data)
  }).then(res => handleResponse<AuthorListResponse>(res)),
  updateAuthor: (id: string, data: Partial<AuthorInput>) => fetch(`${API_BASE_URL}/authors/${id}/`, {
    method: 'PATCH', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data)
  }).then(res => handleResponse<AuthorListResponse>(res)),
  deleteAuthor: (id: string) => fetch(`${API_BASE_URL}/authors/${id}/`, { method: 'DELETE' }).then(res => handleResponse<void>(res)),

  // === LIBROS ===
  getBooks: () => fetch(`${API_BASE_URL}/books/`).then(res => handleResponse<BookListResponse[]>(res)),
  getBook: (id: string) => fetch(`${API_BASE_URL}/books/${id}/`).then(res => handleResponse<BookDetailResponse>(res)),
  createBook: (data: BookInput) => fetch(`${API_BASE_URL}/books/`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data)
  }).then(res => handleResponse<BookListResponse>(res)),
  updateBook: (id: string, data: Partial<BookInput>) => fetch(`${API_BASE_URL}/books/${id}/`, {
    method: 'PATCH', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data)
  }).then(res => handleResponse<BookListResponse>(res)),
  deleteBook: (id: string) => fetch(`${API_BASE_URL}/books/${id}/`, { method: 'DELETE' }).then(res => handleResponse<void>(res)),

  // === COPIAS DE LIBROS ===
  getBookCopies: () => fetch(`${API_BASE_URL}/book-copies/`).then(res => handleResponse<BookCopyDetail[]>(res)),
  getBookCopy: (id: string) => fetch(`${API_BASE_URL}/book-copies/${id}/`).then(res => handleResponse<BookCopyDetail>(res)),
  createBookCopy: (data: BookCopyInput) => fetch(`${API_BASE_URL}/book-copies/`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data)
  }).then(res => handleResponse<BookCopyDetail>(res)),
  updateBookCopy: (id: string, data: Partial<BookCopyInput>) => fetch(`${API_BASE_URL}/book-copies/${id}/`, {
    method: 'PATCH', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data)
  }).then(res => handleResponse<BookCopyDetail>(res)),
  deleteBookCopy: (id: string) => fetch(`${API_BASE_URL}/book-copies/${id}/`, { method: 'DELETE' }).then(res => handleResponse<void>(res)),

  // === USUARIOS ===
  getUsers: () => fetch(`${API_BASE_URL}/users/`).then(res => handleResponse<UserResponse[]>(res)),

  // === PRÉSTAMOS ===
  getLoans: () => fetch(`${API_BASE_URL}/loans/`).then(res => handleResponse<LoanListResponse[]>(res)),
  getLoan: (id: string) => fetch(`${API_BASE_URL}/loans/${id}/`).then(res => handleResponse<LoanDetailResponse>(res)),
  createLoan: (data: LoanInput) => fetch(`${API_BASE_URL}/loans/`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data)
  }).then(res => handleResponse<LoanListResponse>(res)),
  updateLoan: (id: string, data: Partial<LoanInput>) => fetch(`${API_BASE_URL}/loans/${id}/`, {
    method: 'PATCH', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data)
  }).then(res => handleResponse<LoanListResponse>(res)),
  deleteLoan: (id: string) => fetch(`${API_BASE_URL}/loans/${id}/`, { method: 'DELETE' }).then(res => handleResponse<void>(res))
};