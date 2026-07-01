import { useBooks } from '../hooks/useBooks'
import { useAuthors } from '../hooks/useAuthors'
import { useBookCopies } from '../hooks/useBookCopies'
import { useLoans } from '../hooks/useLoans'

export function Dashboard() {
  // Consumo de datos directo desde la caché de React Query
  const { data: books } = useBooks()
  const { data: authors } = useAuthors()
  const { data: copies } = useBookCopies()
  const { data: loans } = useLoans()

  // Cálculos rápidos de negocio
  const totalBooks = books?.length || 0
  const totalAuthors = authors?.length || 0
  const totalCopies = copies?.length || 0
  
  // Contamos cuántos préstamos tienen el estado "Prestado" actualmente
  const activeLoans = loans?.filter(loan => loan.loanStatus === 'Prestado').length || 0

  return (
    <div>
      <h2>📊 Panel de Control (Dashboard)</h2>
      <p>Resumen general del estado del sistema de la biblioteca.</p>
      
      {/* Indicadores en formato de lista simple (HTML Puro) */}
      <ul>
        <li><strong>Total de Libros en Catálogo:</strong> {totalBooks} libros</li>
        <li><strong>Autores Registrados:</strong> {totalAuthors} autores</li>
        <li><strong>Copias Físicas en Inventario:</strong> {totalCopies} unidades</li>
        <li><strong>Préstamos Activos (No devueltos):</strong> {activeLoans} préstamos</li>
      </ul>

      <hr />

      <h3>📌 Últimos Préstamos Registrados</h3>
      {loans && loans.length > 0 ? (
        <table border={1} cellPadding={5} style={{ borderCollapse: 'collapse', width: '100%' }}>
          <thead>
            <tr>
              <th>Usuario ID</th>
              <th>Copia ID</th>
              <th>Fecha Préstamo</th>
              <th>Estado</th>
            </tr>
          </thead>
          <tbody>
            {loans.slice(-5).reverse().map(loan => (
              <tr key={loan.id}>
                <td>{loan.user}</td>
                <td>{loan.book_copy}</td>
                <td>{loan.loanDate}</td>
                <td>{loan.loanStatus}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No hay actividad de préstamos registrada en el sistema.</p>
      )}
    </div>
  )
}