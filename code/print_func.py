
# prints all the students from the students table plus the totla fees
def all_students(conn):

    myCursor = conn.cursor()
    myCursor.callproc('all_students')

    for result in myCursor.stored_results():
        all_students = result.fetchall()

    for student in all_students:
        print("id:", student[0])
        print("First Name:", student[1])
        print("Last Name:", student[2])
        print("Date of Birth:", student[3])
        print("Total Fees:", student[4])
        print("-----------------------------------")



# prints all the trainers from the trainers table
def all_trainers(conn):

    myCursor = conn.cursor()
    myCursor.callproc('all_trainers')

    for result in myCursor.stored_results():
        all_trainers = result.fetchall()

    for trainer in all_trainers:
        print("id:", trainer[0])
        print("First Name:", trainer[1])
        print("Last Name:", trainer[2])
        print("------------------------------------")



# prints all the courses from the courses table
def all_courses(conn):

    myCursor = conn.cursor()
    myCursor.callproc('all_courses')

    for result in myCursor.stored_results():
        all_courses = result.fetchall()

    for course in all_courses:
        print("id:", course[0], "| Course Title:",course[1])
        print("Course Description:", course[2])
        print("Course Language:", course[3])
        print("Course Type:", course[4])
        print("----------------------------------")
    print()




# prints all the assignments from the assignments table
def all_assignments(conn):

    myCursor = conn.cursor()
    myCursor.callproc('all_assignments')

    for result in myCursor.stored_results():
        all_assignmnets = result.fetchall()

    for assignmnet in all_assignmnets:
        print ("id:", assignmnet[0]) 
        print("Title:", assignmnet[1])
        print("Description:", assignmnet[2])
        print("Date of Submision:", assignmnet[3])
        print("Rate of Code Mark:", assignmnet[4])
        print("Rete of Oral Mark:", assignmnet[5])
        print("-------------------------------------")



# prints students per course
def students_per_course(conn):

    myCursor = conn.cursor()
    myCursor.callproc('students_per_course')

    for result in myCursor.stored_results():
        course_students = result.fetchall()

    last_course = None
    num = 1
    for info in course_students:
        # check if the course title is the same as the previous one
        if info[0] != last_course:
            # if not prints the new course title
            num = 1
            last_course = info[0]
            print("Course Title:", info[0])
        
        print("\t", num, ".", info[1], info[2], "| Tuition Fees:", info[3])
        num += 1
    print()

        


# prints trainers per course 
def trainers_per_course(conn):

    myCursor = conn.cursor()
    myCursor.callproc('trainers_per_course')

    for result in myCursor.stored_results():
        course_trainers = result.fetchall()

    last_course = None
    num = 1
    # check if the course title is the same as the previous one
    for info in course_trainers:
        if info[0] != last_course:
            # if not prints the new course title
            num = 1
            last_course = info[0]
            print("Course Title:", info[0])
        
        print("\t", num, ".", info[1], info[2], "| Subject:", info[3])
        num += 1
    print()
 


# prints assignments per course
def assignments_per_course(conn):

    myCursor = conn.cursor()
    myCursor.callproc('assignmnets_per_course')

    for result in myCursor.stored_results():
        course_assignments = result.fetchall()

    last_course = None
    num = 1
    for info in course_assignments:
        # check if the course title is the same as the previous one
        if info[0] != last_course:
            # if not prints the new course title
            num = 1
            last_course = info[0]
            print("Course Title:", info[0])
        
        print("\t", num, ".", "Title:", info[1])
        num += 1
    print()
 



# prints asiignments per student per course
def assignments_per_course_per_student(conn):

    myCursor = conn.cursor()
    myCursor.callproc('asiignments_per_course_per_student')

    for result in myCursor.stored_results():
        course_student_assignments = result.fetchall()

    last_course = None
    last_student = 0
    s_num = 1
    a_num = 1

    for info in course_student_assignments:
        # check if the course title is the same as the previous one
        if info[0] != last_course:
            # if not prints the new course title
            s_num = 1
            last_course = info[0]
            print("Course Title:", info[0])
        # check if the student_id is the same as the previous one
        if info[1] != last_student:
            # if not prints the new student
            a_num = 1
            last_student = info[1]
            print("   ", s_num, ".", info[2], info[3])
            s_num += 1
        
        print("\t", a_num, ".", "Assignment:", info[4], " | Code Mark:" , info[5], " | Oral Mark:", info[6])

        a_num += 1
         
    print()



# prints students who have enrolled in two or more courses
def more_than_one_courses(conn):

    myCursor = conn.cursor()
    myCursor.callproc('students_with_more_than_one_courses')

    for result in myCursor.stored_results():
        students = result.fetchall()
    
    num = 1

    for student in students:
        print (num,".", student[0], student[1], " | Number of Courses:", student[2]) 
        num += 1
