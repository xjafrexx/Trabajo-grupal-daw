export interface Student {
  cui: number;
  email: string;
  full_name: string;
}

export interface Teacher {
  full_name: string;
  email: string | null;
}

export interface Course {
  id: string;
  name: string;
  acronym: string;
  credits: string;
  year_display: string;
  semester_display: string;
}

export interface Workload {
  id: number;
  code: string;
  course: Course;
  group: string;
  laboratory: string;
  teacher: Teacher;
}

export interface EnrollmentResult {
  id: number;
  student: Student;
  workload: Workload;
}

export interface EnrollmentCertificateResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: EnrollmentResult[];
}