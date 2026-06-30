import type { EnrollmentCertificateResponse } from '../types/enrollment'

export async function fetchEnrollmentCertificate(cui: string): Promise<EnrollmentCertificateResponse> {
  const url = `https://sisacad-enrollments-backend.vercel.app/restful/enrollment-certificate/?cui=${cui}`
  const response = await fetch(url)
  
  if (!response.ok) {
    throw new Error('Error al obtener la constancia')
  }
  
  return response.json()
}