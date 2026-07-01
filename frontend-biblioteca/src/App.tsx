import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import { HomePage } from './pages/HomePage'
import { AdminPage } from './pages/AdminPage'

function App() {
  return (
    <BrowserRouter>
      <div style={{ backgroundColor: '#eee', padding: '5px 20px', fontSize: '12px', borderBottom: '1px solid #ccc' }}>
        <span>Enrutador activo: </span>
        <Link to="/" style={{ marginRight: '15px' }}>Ir a Inicio Público</Link>
        <Link to="/admin">Ir a Panel Administrador</Link>
      </div>

      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/admin" element={<AdminPage />} />
        <Route 
          path="*" 
          element={
            <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
              <h2>❌ Error 404: Página no encontrada</h2>
              <Link to="/">Volver al Inicio</Link>
            </div>
          } 
        />
      </Routes>
    </BrowserRouter>
  )
}

export default App