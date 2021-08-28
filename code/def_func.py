
# prints all courses and asks the user to give the ID of the course of their choice
def def_the_course(conn, message = ""):

    myCursor = conn.cursor()
    print("Give the course {}".format(message))

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

    my_cour = int(input("Give the course_id for the course tha you chouse: "))

    return my_cour



# prints all students and asks the user to give the ID of the student of their choice
def find_the_student(conn):

    myCursor = conn.cursor()

    query = """
        SELECT * FROM students
    """
    myCursor.execute(query)

    for s_id, s_fn, s_ln, d_birth in myCursor:
        print("id:",s_id, s_fn, s_ln, d_birth)
    
    student_id = int(input("Give the student_id that you choose: "))

    return student_id



# prints all trainers and asks the user to give the ID of the trainer of their choice
def find_the_trainer(conn):

    myCursor = conn.cursor()

    query = """
        SELECT * FROM trainers
    """
    myCursor.execute(query)

    for t_id, t_fn, t_ln  in myCursor:
        print("id:",t_id, t_fn, t_ln)
    
    trainer_id = int(input("Give the trainer_id that you choose: "))

    return trainer_id

