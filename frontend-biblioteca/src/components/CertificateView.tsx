import { CoursesTable } from './CoursesTable'
import { StudentInfo } from './StudentInfo'

export function CertificateView({ data }: any) {
  const formatIssueDate = () => {
    return new Intl.DateTimeFormat('es-PE', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric',
    }).format(new Date())
  }

  const student = data.results[0]?.student

  if (!student) {
    return <div>No se encontraron matrículas para el C.U.I. consultado.</div>
  }

  return (
    <article className="certificate-card">
      <header>
        <h1>CONSTANCIA DE MATRÍCULA DE LABORATORIO</h1>
        <p>Escuela Profesional de Ingeniería de Sistemas EPIS</p>
        <p>Emitido el: {formatIssueDate()}</p>
      </header>
      <StudentInfo student={student} />
      <CoursesTable enrollments={data.results} total={data.count} />
      <footer>
        Documento generado digitalmente por el Sistema de Matrícula de Laboratorio EPIS
      </footer>
    </article>
  )
}