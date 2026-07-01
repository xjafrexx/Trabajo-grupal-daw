import { useState } from 'react'
import { AdminHeader } from '../components/AdminHeader'
import { Dashboard } from '../components/Dashboard'

export function AdminPage() {
  // Estado que controla las pestañas internas de la administración
  const [currentPage, setCurrentPage] = useState<string>('dashboard')

  return (
    <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      {/* Encabezado Administrativo */}
      <AdminHeader onNavigate={setCurrentPage} currentPage={currentPage} />

      {/* Contenido Dinámico del Panel de Administración */}
      <main>
        {currentPage === 'dashboard' && <Dashboard />}
        
        {currentPage === 'catalog' && (
          <div>
            <h2>📚 Módulo de Catálogo</h2>
            <p>Sección en desarrollo (Tablas de Libros, Autores y Categorías).</p>
          </div>
        )}
        
        {currentPage === 'inventory' && (
          <div>
            <h2>📦 Módulo de Inventario</h2>
            <p>Sección en desarrollo (Gestión de Copias Físicas).</p>
          </div>
        )}
        
        {currentPage === 'loans' && (
          <div>
            <h2>💼 Módulo de Préstamos</h2>
            <p>Sección en desarrollo (Salidas y Devoluciones).</p>
          </div>
        )}
      </main>
    </div>
  )
}