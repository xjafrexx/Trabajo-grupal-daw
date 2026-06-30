export function CoursesTable({ enrollments, total }: any) {
  return (
    <section>
      <h3>ASIGNATURAS MATRICULADAS</h3>
      <table>
        <thead>
          <tr>
            <th>N°</th>
            <th>Código</th>
            <th>Curso</th>
            <th>Año</th>
            <th>Grupo</th>
            <th>Laboratorio</th>
            <th>Docente</th>
          </tr>
        </thead>
        <tbody>
          {enrollments.map((item: any, index: number) => (
            <tr key={item.id}>
              <td>{index + 1}</td>
              <td>{item.workload.code}</td>
              <td>{item.workload.course.name} ({item.workload.course.acronym})</td>
              <td>{item.workload.course.year_display}</td>
              <td>{item.workload.group}</td>
              <td>{item.workload.laboratory}</td>
              <td>{item.workload.teacher.full_name}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <p>Total de cursos matriculados: {total}</p>
    </section>
  )
}