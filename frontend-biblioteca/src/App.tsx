import { useEffect } from 'react';
import { libraryApi } from './api/libraryApi';

//Prueba rapida del API, con un clon de Servidor backend
function App() {
  useEffect(() => {
    console.log('🧪 Iniciando prueba de endpoints...');

    // Llamamos a todos los GET al mismo tiempo para probar la API cliente
    libraryApi.getBooks()
      .then(data => console.log('📚 Libros recibidos:', data))
      .catch(err => console.error('❌ Error en Libros:', err));

    libraryApi.getCategories()
      .then(data => console.log('📁 Categorías recibidas:', data))
      .catch(err => console.error('❌ Error en Categorías:', err));

    libraryApi.getAuthors()
      .then(data => console.log('✍️ Autores recibidos:', data))
      .catch(err => console.error('❌ Error en Autores:', err));

    libraryApi.getLoans()
      .then(data => console.log('🤝 Préstamos recibidos:', data))
      .catch(err => console.error('❌ Error en Préstamos:', err));

    libraryApi.getBookCopies()
      .then(data => console.log('🎫 Copias recibidas:', data))
      .catch(err => console.error('❌ Error en Copias:', err));

    libraryApi.getUsers()
      .then(data => console.log('👥 Usuarios recibidos:', data))
      .catch(err => console.error('❌ Error en Usuarios:', err));

  }, []);

  return (
    <div style={{ padding: '2rem', fontFamily: 'sans-serif' }}>
      <h1>Sistema de Gestión de Librería</h1>
      <p>Prueba de endpoints activa. Abre la consola del navegador (F12) para ver los resultados.</p>
    </div>
  );
}

export default App;