import { useBooks } from '../hooks/useBooks'

export function BookTable() {
  const { data: books, isLoading, isError } = useBooks()

  if (isLoading) return <div>⏳ Cargando catálogo de libros...</div>
  if (isError) return <div>❌ Error al cargar los libros del servidor.</div>

  return (
    <div>
      <h3>📚 Libros Disponibles</h3>
      <table border={1} cellPadding={8} style={{ borderCollapse: 'collapse', width: '100%' }}>
        <thead>
          <tr>
            <th>Título del Libro</th>
            <th>Autor</th>
            <th>Categoría</th>
            <th>Año</th>
          </tr>
        </thead>
        <tbody>
          {books && books.length > 0 ? (
            books.map(book => {
              // Extraemos los nombres o manejamos el caso si vienen vacíos
              const authorName = book.authors?.[0]?.fullName || 'Sin autor asignado'
              const categoryName = book.categories?.[0]?.categoryName || 'Sin categoría'

              return (
                <tr key={book.id}>
                  <td><strong>{book.title}</strong></td>
                  <td>{authorName}</td>
                  <td>{categoryName}</td>
                  <td>{book.publishYear}</td>
                </tr>
              )
            })
          ) : (
            <tr>
              <td colSpan={4} style={{ textAlign: 'center' }}>No hay libros registrados en la biblioteca.</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  )
}