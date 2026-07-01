import { HomeHeader } from '../components/HomeHeader'
import { BookTable } from '../components/BookTable'

export function HomePage() {
  return (
    <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      <HomeHeader />
      <main>
        <h2>Bienvenido al catálogo público</h2>
        <p>Aquí puedes consultar los libros disponibles y sus detalles en tiempo real.</p>
        <hr style={{ margin: '20px 0' }} />
        <BookTable />
      </main>
    </div>
  )
}