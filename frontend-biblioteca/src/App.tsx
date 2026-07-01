import { useBooks } from './hooks/useBooks'
import { useAuthors, useCreateAuthor, useUpdateAuthor, useDeleteAuthor } from './hooks/useAuthors'
import { useCategories } from './hooks/useCategories'

function App() {
  const { data: books, isLoading: loadingBooks, isError: errorBooks } = useBooks()
  const { data: authors, isLoading: loadingAuthors, isError: errorAuthors } = useAuthors()
  const { data: categories, isLoading: loadingCategories, isError: errorCategories } = useCategories()

  // Inicializamos todas las mutaciones disponibles
  const createAuthorMutation = useCreateAuthor()
  const updateAuthorMutation = useUpdateAuthor()
  const deleteAuthorMutation = useDeleteAuthor()

  // 1. Manejo del POST
  const handleTestCreateAuthor = () => {
    const randomName = `Autor de Prueba #${Math.floor(Math.random() * 1000)}`
    createAuthorMutation.mutate({
      fullName: randomName,
      nationality: 'Prueba Local',
      status: true,
      created_id: null as any,
      modified_id: null as any
    })
  }

  // 2. Manejo del PATCH (Edita la nacionalidad a "Editado Mundial")
  const handleTestUpdateAuthor = (id: string, currentName: string) => {
    updateAuthorMutation.mutate({
      id,
      data: {
        fullName: `${currentName} (Editado)`,
        nationality: 'Editado Mundial',
        modified_id: null as any
      }
    })
  }

  // 3. Manejo del DELETE
  const handleTestDeleteAuthor = (id: string) => {
    if (window.confirm('¿Seguro que quieres eliminar este autor de prueba en Django?')) {
      deleteAuthorMutation.mutate(id)
    }
  }

  const anyLoading = loadingBooks || loadingAuthors || loadingCategories
  if (anyLoading) {
    return <div style={{ padding: '30px', fontFamily: 'sans-serif' }}>⏳ Cargando datos del sistema...</div>
  }

  if (errorBooks || errorAuthors || errorCategories) {
    return (
      <div style={{ padding: '30px', fontFamily: 'sans-serif', color: 'red' }}>
        <h2>❌ Error al conectar con el Backend de Django</h2>
      </div>
    )
  }

  return (
    <div style={{ padding: '30px', fontFamily: 'sans-serif', backgroundColor: '#f9f9f9', minHeight: '100vh' }}>
      <header style={{ borderBottom: '2px solid #ccc', paddingBottom: '10px', marginBottom: '20px' }}>
        <h1>🧪 Super Consola de Pruebas: CRUD de Autores</h1>
        <p>Probando operaciones de Lectura, Creación, Modificación y Eliminación con TanStack Query.</p>
      </header>

      {/* BOTÓN PARA CREAR */}
      <section style={{ backgroundColor: '#fff', padding: '20px', borderRadius: '8px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)', marginBottom: '20px' }}>
        <h2>⚡ Acciones Globales</h2>
        <button 
          onClick={handleTestCreateAuthor}
          disabled={createAuthorMutation.isPending}
          style={{ backgroundColor: '#4CAF50', color: 'white', padding: '10px 20px', border: 'none', borderRadius: '4px', cursor: 'pointer' }}
        >
          {createAuthorMutation.isPending ? 'Guardando...' : '➕ Crear Autor Aleatorio'}
        </button>
      </section>

      {/* RENDERIZADO DE COLUMNAS */}
      <div style={{ display: 'grid', gridTemplateColumns: '1.5fr 1fr 1fr', gap: '20px' }}>
        
        {/* COLUMNA AUTORES INTERACTIVOS */}
        <div style={{ backgroundColor: '#fff', padding: '20px', borderRadius: '8px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
          <h3>✍️ Gestión de Autores ({authors?.length})</h3>
          <ul style={{ paddingLeft: '0', listStyle: 'none' }}>
            {authors?.map(author => (
              <li key={author.id} style={{ padding: '10px 0', borderBottom: '1px solid #eee', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <div>
                  <strong style={{ display: 'block' }}>{author.fullName}</strong>
                  <small style={{ color: '#666' }}>🌍 Nacionalidad: {author.nationality}</small>
                </div>
                <div style={{ display: 'flex', gap: '5px' }}>
                  <button 
                    onClick={() => handleTestUpdateAuthor(author.id, author.fullName)}
                    style={{ backgroundColor: '#008CBA', color: 'white', border: 'none', padding: '5px 10px', borderRadius: '4px', cursor: 'pointer', fontSize: '12px' }}
                  >
                    ✏️ Editar
                  </button>
                  <button 
                    onClick={() => handleTestDeleteAuthor(author.id)}
                    style={{ backgroundColor: '#f44336', color: 'white', border: 'none', padding: '5px 10px', borderRadius: '4px', cursor: 'pointer', fontSize: '12px' }}
                  >
                    🗑️ Borrar
                  </button>
                </div>
              </li>
            ))}
          </ul>
        </div>

        {/* COLUMNA CATEGORÍAS */}
        <div style={{ backgroundColor: '#fff', padding: '20px', borderRadius: '8px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
          <h3>🏷️ Categorías ({categories?.length})</h3>
          <ul>
            {categories?.map(cat => <li key={cat.id}>{cat.categoryName}</li>)}
          </ul>
        </div>

        {/* COLUMNA LIBROS */}
        <div style={{ backgroundColor: '#fff', padding: '20px', borderRadius: '8px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
          <h3>📚 Libros ({books?.length})</h3>
          <ul>
            {books?.map(book => <li key={book.id}>{book.title}</li>)}
          </ul>
        </div>

      </div>
    </div>
  )
}

export default App