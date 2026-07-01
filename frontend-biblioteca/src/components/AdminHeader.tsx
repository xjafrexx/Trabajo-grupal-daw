interface HeaderProps {
  onNavigate: (page: string) => void;
  currentPage: string;
}

export function AdminHeader({ onNavigate, currentPage }: HeaderProps) {
  return (
    <header style={{ borderBottom: '1px solid #000', padding: '10px 0', marginBottom: '20px' }}>
      <strong style={{ marginRight: '30px' }}>📚 Sistema Biblioteca Admin</strong>
      
      <nav style={{ display: 'inline' }}>
        <button 
          onClick={() => onNavigate('dashboard')}
          style={{ marginRight: '10px', fontWeight: currentPage === 'dashboard' ? 'bold' : 'normal' }}
        >
          Dashboard
        </button>
        <button 
          onClick={() => onNavigate('catalog')}
          style={{ marginRight: '10px', fontWeight: currentPage === 'catalog' ? 'bold' : 'normal' }}
        >
          Catálogo (Libros/Autores/Cat)
        </button>
        <button 
          onClick={() => onNavigate('inventory')}
          style={{ marginRight: '10px', fontWeight: currentPage === 'inventory' ? 'bold' : 'normal' }}
        >
          Inventario (Copias)
        </button>
        <button 
          onClick={() => onNavigate('loans')}
          style={{ fontWeight: currentPage === 'loans' ? 'bold' : 'normal' }}
        >
          Préstamos
        </button>
      </nav>
    </header>
  )
}