import { useParams } from 'react-router-dom'
import { useEnrollmentCertificate } from '../hooks/useEnrollmentCertificate'
import { CertificateView } from '../components/CertificateView'

export function CertificatePage() {
  const { cui } = useParams()
  const { data, isLoading, isError } = useEnrollmentCertificate(cui || '')

  if (isLoading) return <div>Cargando...</div>
  if (isError) return <div>Error al cargar</div>
  if (!data) return null

  return <CertificateView data={data} />
}