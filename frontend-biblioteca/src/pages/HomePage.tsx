import { useState } from 'react'
import { useNavigate } from 'react-router-dom'

export function HomePage() {
  const [cui, setCui] = useState('')
  const navigate = useNavigate()

  const handleSubmit = (e: any) => {
    e.preventDefault()
    if (cui) {
      navigate(`/constancia/${cui}`)
    }
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input 
          type="text" 
          value={cui} 
          onChange={(e) => setCui(e.target.value)} 
        />
        <button type="submit">Buscar</button>
      </form>
    </div>
  )
}