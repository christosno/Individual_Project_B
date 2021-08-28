
import mysql.connector
import datetime
from print_func import *
from menu import *
from general_func import *
from info_func import *
from insert_func import *
from new_course import *
from def_func import *


 
config = {
    'host' : 'localhost',
    'user' : 'root',
    'passwd' : 'root',
    'database' : 'private_school'
} 

conn = mysql.connector.connect(**config)



#MAIN PROGRAM
#####################################################################################



if __name__ == "__main__":


    print("\t#################################")
    print("\t# WELCOME TO THE PRIVET SCHOOL! #")
    print("\t#################################")
    print("")



    Main_Menu_Choice = None
    Add_Menu_Choice = None
    Print_choice = None
    contin = None
    same_course = None

    while Main_Menu_Choice != "3":
        # check if the user want to exit
        if Add_Menu_Choice == "8" or Print_choice == "11":
            break

        Main_Menu_Choice = Main_Menu()
        
        
        if Main_Menu_Choice == "1":

            while True:


                Add_Menu_Choice = Add_menu()

                # check if the user want to leave from add menu
                if Add_Menu_Choice == "7" or Add_Menu_Choice == "8":

                    break
                
                # user choice -> add course
                elif Add_Menu_Choice == "0":

                    while True:

                        # get infos for course from the user
                        cour_info = course_info(conn)
                        # insert course to the database, in courses table
                        insert_course(conn, cour_info[0], cour_info[1], cour_info[2], cour_info[3])
                        # ask the user if he want to continue to add new courses
                        same_course = continue_in_the_same_menu("add courses", "Add Menu", "Main Menu")
                            
                        # check if the user want to leave from add new course
                        if same_course in ["2", "3"]:
                            break

                    # check if the user want to leave from add menu
                    if same_course == "3":
                        break

                # user choice -> add trainer
                elif Add_Menu_Choice == "1":

                    while True:
                        # get infos for trainer from the user
                        trainer_info = Trainer_info()
                        # insert trainer to the database, in trainers table
                        trainer_id = insert_trainer(conn, trainer_info[0], trainer_info[1])

                        while True:
                            # ask the user if he want to add course for the trainer
                            same_trainer = continue_menu("add courses for the trainer","add new trainer", "add menu")
                            # check if the user doesn't want to add course 
                            if same_trainer in ["2", "3", "4"]:
                                break
                            # asks about the course that the trainer will enroll
                            course_id = def_the_course(conn, message = "for trainer")
                            # ask for trainer's subject
                            subject_id = give_subject(conn)
                            # add the trainer and the course in trainers_courses table 
                            add_trainer_in_course(conn, course_id, trainer_id, subject_id)

                        # check if the user want to leave from add new trainer
                        if same_trainer in ["3", "4"]:
                            break

                    # check if the user want to leave from add menu
                    if same_trainer == "4":
                        break

                # user choice -> add student
                elif Add_Menu_Choice == "2":

                    while True:
                        # get infos for student from the user
                        student_info = Student_info()
                        # insert student to the database, in students table
                        student_id = insert_student(conn, student_info[0], student_info[1], student_info[2])

                        while True:
                            # ask the user if he want to add course for the student
                            same_student = continue_menu("Add courses for the student", "Add new student", "Add menu")
                            # check if the user want to leave from add courses for the student
                            if same_student in ["2", "3", "4"]:
                                break
                            # asks about the course that the student will enroll
                            course_id = def_the_course(conn, message = "for student")
                            # add the tuitions fees for this course 
                            tuition_fees = give_tuition_fees()
                            # add the student and the course in students_courses table
                            add_student_in_course(conn, course_id, student_id, tuition_fees)
                            

                        # check if the user want to leave from add new student
                        if same_student in ["3", "4"]:
                            break

                    # check if the user want to leave from add menu
                    if same_student == "4":
                        break



                # user choice -> add assignment
                elif Add_Menu_Choice == "3":

                    while True:
                        # get infos for assignment from the user
                        assignment_info = Assignment_info()
                        # insert assignment to the database, in assignments table
                        assignment_id = insert_assignment(conn, assignment_info[0], assignment_info[1], datetime.date.today(), assignment_info[2])

                        while True:
                            # ask the user if he want to add course for the assignment
                            same_assignment = continue_menu("Add courses for the assignment", "Add new assignment", "Add menu")
                            # check if the user want to leave from add courses for the assignment
                            if same_assignment in ["2", "3", "4"]:
                                break
                            # asks about the course for assignment
                            course_id = def_the_course(conn, message = "for the assignment")
                            # add the assignment and the course to assignments_courses table
                            add_assignment_in_course(conn, course_id, assignment_id)
                            
                        # check if the user want to leave from add new assignment
                        if same_assignment in ["3", "4"]:
                            break
                    # check if the user want to leave from add menu
                    if same_assignment == "4":
                        break

                # user choice -> Add New Course For Trainer
                elif Add_Menu_Choice == "4":

                    while True:
                        #print all trainers and ask for the trainer id
                        trainer_id = find_the_trainer(conn)
                        # asks about the course that the trainer will enroll
                        course_id = def_the_course(conn, message = "for trainer")
                        # ask for trainer's subject
                        subject_id = give_subject(conn)
                        # add the trainer and course in trainers_courses table
                        add_trainer_in_course(conn, course_id, trainer_id, subject_id)
                        # asks the user if he wants to keep adding trainers
                        contin = continue_in_the_same_menu("Add courses for trainer", "Add Menu", "Main Menu")
                        # check if the user want to leave from add new course
                        if contin in ["2", "3"]:
                            break

                    # check if the user want to leave from add menu
                    if contin == "3":
                        break

                # user choice -> Add New Course For Trainer
                elif Add_Menu_Choice == "5":

                    while True:
                        #print all students and ask for the student id
                        student_id = find_the_student(conn)
                        # asks about the course that the student will enroll
                        course_id = def_the_course(conn, message = "for student")
                        # add the tuitions fees for this course 
                        tuition_fees = give_tuition_fees()
                        # add the student and the course in students_courses table
                        add_student_in_course(conn, course_id, student_id, tuition_fees)
                        # asks the user if he wants to continue adding students
                        contin = continue_in_the_same_menu("Add courses for student", "Add Menu", "Main Menu")
                        # check if the user want to leave from add new course
                        if contin in ["2", "3"]:
                            break

                    # check if the user want to leave from add menu
                    if contin == "3":
                        break


                
                elif Add_Menu_Choice == "6":

                    while True:
                        insert_marks(conn)

                        # asks the user if he wants to continue adding students
                        contin = continue_in_the_same_menu("Add Marks", "Add Menu", "Main Menu")
                        # check if the user want to leave from add new course
                        if contin in ["2", "3"]:
                            break

                    # check if the user want to leave from add menu
                    if contin == "3":
                        break


        # user choice -> Request Info
        elif Main_Menu_Choice == "2":

            while True:
                # ask the user about the request
                Print_choice = Print_Menu()

                # check if the user want to exit or go to main menu
                if Print_choice == "10" or Print_choice == "11" :
                    break
                # user choice -> Collection of all the students
                elif  Print_choice == "1":
                    # print all students
                    all_students(conn)
                    # asks the user how he wants to continue(stay in the print menu or go to main menu or exit)
                    contin = continue_in_the_same_menu("in the print menu")
                    # check if the user want to leave from print menu
                    if contin in ["2", "3"]:
                        break


                # user choice -> Collection of all the trainers
                elif Print_choice == "2":
                    # print all trainers
                    all_trainers(conn)
                    # asks the user how he wants to continue(stay in the print menu or go to main menu or exit)
                    contin = continue_in_the_same_menu("in the print menu")
                    # check if the user want to leave from print menu
                    if contin in ["2", "3"]:
                        break

                # user choice -> Collection of all the assignments
                elif Print_choice == "3":
                    # print all asignments
                    all_assignments(conn)
                    # asks the user how he wants to continue(stay in the print menu or go to main menu or exit)
                    contin = continue_in_the_same_menu("in the print menu")
                    # check if the user want to leave from print menu
                    if contin in ["2", "3"]:
                        break

                # user choice -> Collection of all the courses
                elif Print_choice == "4":
                    # print all courses
                    all_courses(conn)
                    # asks the user how he wants to continue(stay in the print menu or go to main menu or exit)
                    contin = continue_in_the_same_menu("in the print menu")
                    # check if the user want to leave from print menu
                    if contin in ["2", "3"]:
                        break

                # user choice -> The students per course
                elif Print_choice == "5":
                    #print students per course
                    students_per_course(conn)
                    # asks the user how he wants to continue(stay in the print menu or go to main menu or exit)
                    contin = continue_in_the_same_menu("in the print menu")
                    # check if the user want to leave from print menu
                    if contin in ["2", "3"]:
                        break

                # user choice -> The trainers per course
                elif Print_choice == "6":
                    #print trainers per course 
                    trainers_per_course(conn)
                    # asks the user how he wants to continue(stay in the print menu or go to main menu or exit)
                    contin = continue_in_the_same_menu("in the print menu")
                    # check if the user want to leave from print menu
                    if contin in ["2", "3"]:
                        break

                # user choice -> The assignments per course
                elif Print_choice == "7":
                    # print assignments per course
                    assignments_per_course(conn)
                    # asks the user how he wants to continue(stay in the print menu or go to main menu or exit)
                    contin = continue_in_the_same_menu("in the print menu")
                    # check if the user want to leave from print menu
                    if contin in ["2", "3"]:
                        break

                # user choice -> The assignments per student per course
                elif Print_choice == "8":
                    # print assignments per courses per studens
                    assignments_per_course_per_student(conn)
                    # asks the user how he wants to continue(stay in the print menu or go to main menu or exit)
                    contin = continue_in_the_same_menu("in the print menu")
                    # check if the user want to leave from print menu
                    if contin in ["2", "3"]:
                        break

                # user choice -> List of students that belong to more than one courses
                elif Print_choice == "9":
                    more_than_one_courses(conn)
                    # asks the user how he wants to continue(stay in the print menu or go to main menu or exit)
                    contin = continue_in_the_same_menu("in the print menu")
                    # check if the user want to leave from print menu
                    if contin in ["2", "3"]:
                        break
            # check if the user want to leave from main menu
            if contin == "3":
                break


    print("")
    print("\t\tBYE BYE")

