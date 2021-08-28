

# generates a unique course code as a key in private school dictionary, also creates a new  Course instance as value
def course_info(conn):

    myCursor = conn.cursor()
    # chouses the course language
    course_language = give_language(conn)
    
    # chouses the course type
    course_type = give_type(conn)

    description = input("Give the description of the course:\n")

    # put in a variable the last four digits for the course code, using the course_discription function
    course_code_discription = course_discription(course_language, course_type)
    # determines the number of the new course in relation to the number of the most recent same course
    courseCode = course_code(myCursor, course_code_discription)
    # add in private school dictionary as key the course_code also create a new Course instance for the dict value
    return (courseCode, description, course_language, course_type)



# return the last four characters from the course code (e.g. "CB13FTPY")
def course_discription(course_language, course_type):

    if course_language == 1:
        if course_type == 1:
            return ("FTPY")
        else:
            return ("PTPY")

    elif course_language == 2:
        if course_type == 1:
            return ("FTJV")
        else:
            return ("PTJV")

    elif course_language == 3:
        if course_type == 1:
            return ("FTC#")

        else:
            return ("PTC#")
    else:
        if course_type == 1:

            return ("FTJS")
        else:
            return ("PTJS")



# generates the final course code
def course_code(myCursor, course_code_discription):
    num = 1
    # I call the function through myCursor the procedure all_courses
    myCursor.callproc('all_courses')
    # I get all the results of the procedure
    for result in myCursor.stored_results():
        all_courses = result.fetchall()
    # I'm looking for the largest number of the last course and adding one to the variable num
    for course in all_courses:
        if course[1][4:] == course_code_discription:
            while num <= int(course[1][2:4]):
                num += 1
    # I examine if the number is single digit and its additional 0 in front of it
    if num < 10 :
        course_code = "CB" + "0" + str(num) + course_code_discription
    else:
        course_code = "CB" + str(num) + course_code_discription
    # return the final course code
    return course_code



# prints all available languages and asks the user to select one of them
def give_language(conn):

    myCursor = conn.cursor()

    query = """
        SELECT * FROM languages
    """
    myCursor.execute(query)

    for lang_id, lang in myCursor:
        print("id:",lang_id,"|language:", lang)
    print()
    language_id = int(input("Give the language_id for the language tha you choose: "))
    print()
    return language_id

# prints all available types and asks the user to select one of them
def give_type(conn):

    myCursor = conn.cursor()

    query = """
        SELECT * FROM course_types
    """
    myCursor.execute(query)

    for type_id, type in myCursor:
        print("id:",type_id,"|Type:", type)
    print()
    type_id = int(input("Give the type_id for the language tha you choose: "))
    print()
    return type_id