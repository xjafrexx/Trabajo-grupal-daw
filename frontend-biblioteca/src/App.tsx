import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { HomePage } from './pages/HomePage'
import { CertificatePage } from './pages/CertificatePage'
import './App.css'

function App() {
  return (
    <BrowserRouter>
      <main>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/constancia/:cui" element={<CertificatePage />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </main>
    </BrowserRouter>
  )
}

export default App
