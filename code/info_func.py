import datetime
from general_func import validated_date

#asks for the necessary inputs for a trainer and returns a tuple with that inputs
def Trainer_info():
    first_name = input("Give the Trainer's first name: ").strip().capitalize()
    last_name = input("Give the trainer's Last name: ").strip().capitalize()

    return (first_name, last_name)



# prints all the subjects and asks the user to give the ID of the subject of their choice
def give_subject(conn):

    myCursor = conn.cursor()

    query = """
        SELECT * FROM subjects
    """
    myCursor.execute(query)

    for sub_id, sub in myCursor:
        print("id:", sub_id, "|Subject:", sub)
    print()
    subject_id = int(input("Give the subject_id for the subject tha you choose: "))
    print()
    return subject_id



#asks for the necessary inputs for a student and returns a tuple with that inputs
def Student_info():
    first_name = input("Give student's first name: ").strip().capitalize()
    last_name = input("Give student's Last name: ").strip().capitalize()
    date_of_birth = validated_date("Give the day birth: ")

    return (first_name, last_name, date_of_birth)



# ask for the tuitions fees, validate the input and return it
def give_tuition_fees():
    while True:
        try:
            tuition_fees = int(input("Tuition fees: ").strip())
            break
        except:
            print("Fees must be digits!!")

    return tuition_fees


# validate the mark_code , it must be up to 100, returns mark_coda and mark_oral
def validate_mark():
    mark_code = input("Mark for the submitted code: ")
    while (not mark_code.isdigit()) or int(mark_code) > 100 or int(mark_code) < 0:
        print("The input must be digit and between 0 and 100 ")
        mark_code = input("Mark for the submitted code: ")
   
    return (mark_code)


#asks for the necessary inputs for a assignment and returns a tuple with that inputs
def Assignment_info():
    title = input("Give the title: ").strip().capitalize()
    discription = input("Give the Discription: ").strip().capitalize()
    mark_code_oral = validate_mark()

    return (title, discription, mark_code_oral)

