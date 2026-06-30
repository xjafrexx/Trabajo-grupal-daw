export function StudentInfo({ student }: any) {
  return (
    <section>
      <h3>DATOS DEL ALUMNO</h3>
      <div>
        <p><strong>C.U.I.:</strong> {student.cui}</p>
        <p><strong>Nombre completo:</strong> {student.full_name}</p>
        <p><strong>Email:</strong> {student.email}</p>
      </div>
    </section>
  )
}