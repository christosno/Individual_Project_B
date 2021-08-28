


def insert_student(conn, first_name, last_name, date_of_birth):

    myCursor = conn.cursor()

    query = """INSERT INTO students
               VALUES (%s, %s, %s, %s)"""

    data = (myCursor.lastrowid, first_name, last_name, date_of_birth)

    try:
        myCursor.execute(query, data)
        conn.commit()
        print()
        print("Successful Registration")
    except:
        conn.rollback()
        print()
        print("Oops, Something went wrong!")
    
    print()

    return myCursor.lastrowid




def insert_trainer(conn, first_name, last_name):

    myCursor = conn.cursor()

    query = """
        INSERT INTO trainers
        VALUES (%s, %s, %s)
    """

    data = (myCursor.lastrowid, first_name, last_name)

    try:
        myCursor.execute(query, data)
        conn.commit()
        print()
        print("Successful Registration")
    except:
        conn.rollback()
        print()
        print("Oops, Something went wrong!")

    print()
    
    return myCursor.lastrowid




def insert_assignment(conn, assignment_title, assignmnets_destription, date_of_submision, rate_of_code_mark):

    myCursor = conn.cursor()

    query = """
        INSERT INTO assignments
        VALUES (%s, %s, %s, %s, %s)
    """

    data = (myCursor.lastrowid, assignment_title, assignmnets_destription, date_of_submision, rate_of_code_mark)

    try:
        myCursor.execute(query, data)
        conn.commit()
        print()
        print("Successful Registration")
    except:
        conn.rollback()
        print()
        print("Oops, Something went wrong!")

    print()

    return myCursor.lastrowid





def insert_course(conn, course_title, course_discription, course_language, course_type):

    myCursor = conn.cursor()

    query = """
        INSERT INTO courses
        VALUES (%s, %s, %s, %s, %s)
    """

    data = (myCursor.lastrowid, course_title, course_discription, course_language, course_type)

    try:
        myCursor.execute(query, data)
        conn.commit()
        print()
        print("Successful Registration")

    except:
        conn.rollback()
        print()
        print("Oops, Something went wrong!")
        

    print()

    return myCursor.lastrowid




def add_student_in_course(conn, course_id, student_id, tuition_fees):

    myCursor = conn.cursor()

    query = """
        INSERT INTO students_courses
        VALUES (%s, %s, %s)
    """

    data = (course_id, student_id, tuition_fees)

    try:
        myCursor.execute(query, data)
        conn.commit()
        print()
        print("Successful Registration")
        
    except:
        conn.rollback
        print()
        print("Oops, Something went wrong!")
        

    print()





def add_trainer_in_course(conn, course_id, trainer_id, subject_id):

    myCursor = conn.cursor()

    query = """
        INSERT INTO trainers_courses
        VALUES (%s, %s, %s)
    """

    data = (course_id, trainer_id, subject_id)

    try:
        myCursor.execute(query, data)
        conn.commit()
        print("Successful Registration")
        print()
    except:
        conn.rollback
        print("Oops, Something went wrong!")
        print()

    print()




def add_assignment_in_course(conn, course_id, assignment_id):

    myCursor = conn.cursor()

    query = """
        INSERT INTO assignments_courses
        VALUES (%s, %s)
    """

    data = (course_id, assignment_id)

    try:
        myCursor.execute(query, data)
        conn.commit()
        print("Successful Registration")
        print()
    except:
        conn.rollback
        print("Oops, Something went wrong!")
        print()
    
    print()



def insert_marks(conn):

    myCursor = conn.cursor()
    myCursor.callproc('all_students')

    for result in myCursor.stored_results():
        all_students = result.fetchall()

    for student in all_students:
        print("id:", student[0], student[1], student[2])

    print()

    while True:
        try:
            stud_id = int(input("Please enter the student id of the student you choose: "))
            break
        except:
            print("Student id must be digit")

    student_with_courses(conn, stud_id)

    while True:
        try:
            cour_id = int(input("Please enter the course id of the course you choose: "))
            break
        except:
            print("Student id must be digit")

    student_with_course_with_assignment(conn, stud_id, cour_id)

    while True:
        try:
            ass_id = int(input("Please enter the assignment id of the assignment you choose: "))
            break
        except:
            print("Assignment id must be digit")

    code_mark = input("Code Mark: ")
    while (not code_mark.isdigit()) or int(code_mark) > 100 or int(code_mark) < 0:
        print("The input must be digit and between 0 and 100 ")
        code_mark = input("Code Mark: ")

    oral_mark = input("Oral Mark: ")
    while (not oral_mark.isdigit()) or int(oral_mark) > 100 or int(oral_mark) < 0:
        print("The input must be digit and between 0 and 100 ")
        oral_mark = input("Oral Mark: ")

    query = """
        UPDATE assignments_students_courses
        SET code_mark = %s, oral_mark = %s
        WHERE course_id = %s AND student_id = %s AND assignment_id = %s;
    """

    data = (code_mark, oral_mark, cour_id, stud_id, ass_id)

    try:
        myCursor.execute(query, data)
        conn.commit()
        print("Successful Update")
    except:
        conn.rollback
        print("Oops, Something went wrong!")
        print()








def student_with_courses(conn, stud_id):

    myCursor = conn.cursor()

    query = """
        SELECT course_id, course_title 
        FROM assignments_students_courses
        JOIN courses USING(course_id)
        WHERE student_id = %s
        GROUP BY course_id;
    """

    data = (stud_id, )

    try:
        myCursor.execute(query, data)
    
    except:
        conn.rollback
        print("Oops, Something went wrong!")
        print()
    
    for c_id, c_title in myCursor:
        print("Course id:", c_id, " | Course Title:", c_title)
    



def student_with_course_with_assignment(conn, stud_id, cour_id):

    myCursor = conn.cursor()

    query = """
        SELECT assignment_id, assignment_title
        FROM assignments_students_courses
        JOIN assignments USING(assignment_id)
        WHERE student_id = %s AND course_id = %s;
    """

    data = (stud_id, cour_id)

    try:
        myCursor.execute(query, data)
        
    except:
        conn.rollback
        print("Oops, Something went wrong!")
        print()
    
    for a_id, a_title in myCursor:
        print("Assignment id:", a_id, " | Assignment Title:", a_title)
