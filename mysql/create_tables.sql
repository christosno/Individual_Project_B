CREATE TABLE IF NOT EXISTS course_types (
  type_id INT NOT NULL AUTO_INCREMENT,
  type   VARCHAR(45) NOT NULL,
  PRIMARY KEY (type_id));
  

CREATE TABLE IF NOT EXISTS languages (
  language_id INT NOT NULL AUTO_INCREMENT,
  language    VARCHAR(45) NOT NULL,
  PRIMARY KEY (language_id));
  

CREATE TABLE IF NOT EXISTS courses (
  course_id INT NOT NULL AUTO_INCREMENT,
  course_title CHAR(8) NULL DEFAULT NULL,
  course_description VARCHAR(255) NULL DEFAULT NULL,
  language_id INT NOT NULL,
  course_types_type_id INT NOT NULL,
  PRIMARY KEY (course_id),
  CONSTRAINT fk_courses_course_types1
    FOREIGN KEY (course_types_type_id)
    REFERENCES private_school.course_types (type_id),
  CONSTRAINT fk_courses_languages1
    FOREIGN KEY (language_id)
    REFERENCES private_school.languages (language_id));
    

CREATE TABLE IF NOT EXISTS assignments (
  assignment_id INT NOT NULL AUTO_INCREMENT,
  assignment_title VARCHAR(45) NOT NULL,
  assignment_description VARCHAR(255) NULL DEFAULT NULL,
  date_of_submision DATE NULL DEFAULT NULL,
  rate_of_code_mark INT NULL DEFAULT NULL,
  PRIMARY KEY (assignment_id));


    
CREATE TABLE IF NOT EXISTS assignments_courses (
  course_id INT NOT NULL,
  assignment_id INT NOT NULL,
  PRIMARY KEY (course_id, assignment_id),
  CONSTRAINT fk_assignments_courses_assignments
    FOREIGN KEY (assignment_id)
    REFERENCES private_school.assignments (assignment_id),
  CONSTRAINT fk_assignments_courses_courses
    FOREIGN KEY (course_id)
    REFERENCES private_school.courses (course_id));
    
    

CREATE TABLE IF NOT EXISTS students (
  student_id INT NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(45) NOT NULL,
  last_name VARCHAR(45) NOT NULL,
  date_of_birth DATE NULL DEFAULT NULL,
  PRIMARY KEY (student_id));
  
  
CREATE TABLE IF NOT EXISTS students_courses (
  course_id INT NOT NULL,
  student_id INT NOT NULL,
  tuition_fees INT NOT NULL,
  PRIMARY KEY (course_id, student_id),
  CONSTRAINT fk_students_courses_courses
    FOREIGN KEY (course_id)
    REFERENCES private_school.courses (course_id),
  CONSTRAINT fk_students_courses_students
    FOREIGN KEY (student_id)
    REFERENCES private_school.students (student_id));
    
    

CREATE TABLE IF NOT EXISTS assignments_students_courses (
  course_id INT NOT NULL,
  student_id INT NOT NULL,
  assignment_id INT NOT NULL,
  code_mark INT NULL DEFAULT NULL,
  oral_mark INT NULL DEFAULT NULL,
  PRIMARY KEY (course_id, student_id, assignment_id),
  CONSTRAINT fk_assignments_students_courses_assignments
    FOREIGN KEY (assignment_id)
    REFERENCES private_school.assignments (assignment_id),
  CONSTRAINT fk_assignments_students_courses_students_courses
    FOREIGN KEY (course_id , student_id)
    REFERENCES private_school.students_courses (course_id , student_id));
   
   
   
CREATE TABLE IF NOT EXISTS subjects (
  subject_id INT NOT NULL AUTO_INCREMENT,
  subject VARCHAR(45) NOT NULL,
  PRIMARY KEY (subject_id));
  
  
CREATE TABLE IF NOT EXISTS trainers (
  trainer_id INT NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(45) NOT NULL,
  last_name VARCHAR(45) NOT NULL,
  PRIMARY KEY (trainer_id));
  
  
 CREATE TABLE IF NOT EXISTS trainers_courses (
  course_id INT NOT NULL,
  trainer_id INT NOT NULL,
  subject_id INT NOT NULL,
  PRIMARY KEY (course_id, trainer_id, subject_id),
  CONSTRAINT fk_trainers_courses_courses1
    FOREIGN KEY (course_id)
    REFERENCES private_school.courses (course_id),
  CONSTRAINT fk_trainers_courses_subjects1
    FOREIGN KEY (subject_id)
    REFERENCES private_school.subjects (subject_id),
  CONSTRAINT fk_trainers_courses_trainers1
    FOREIGN KEY (trainer_id)
    REFERENCES private_school.trainers (trainer_id));


    