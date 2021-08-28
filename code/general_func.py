import datetime

#  checks the date input from the user
def validated_date(string):
    print("")
    print(string)
    while True:
        try:

            while True:
                try:
                    year = int(input("give the year (in four digits e.g 1990) : ").strip())
                    break
                except :
                    print("Has be digits")

            while True:
                try:
                    month = int(input("give the month : ").strip())
                    break
                except:
                    print("Has be digits")

            while True:
                try:
                    day = int(input("give the day : ").strip())
                    break
                except:
                    print("Has be digits")


            return datetime.date(year,month,day)

        except ValueError:
            print("### Out of range!! ###")
            print("### Please try again ##")
            print("")



# ask the user how to proceed
def continue_menu(string1, string2, string3, string4 = "Main Menu"):
    contin = input("\t1: Continue {}\n\t2: {}\n\t3: {}\n\t4: {}\n\t ->".format(string1, string2, string3, string4))
    while contin not in ["1", "2", "3", "4"]:
        contin = input("\t1: Continue {}\n\t2: {}\n\t3: {}\n\t4: {}\n\t ->".format(string1, string2, string3, string4))
    print()
    return contin
    


# ask the user to continue in the same menu
def continue_in_the_same_menu(string1, string2 = "Main Menu", string3 = "Exit"):
    contin = input("\t1: Continue {}\n\t2: {}\n\t3: {}\n\t ->".format(string1,string2, string3))
    while contin not in ["1", "2", "3"]:
        contin = input("\t1: Continue {}\n\t2: {}\n\t3: {}\n\t ->".format(string1,string2, string3))
    print()
    return contin





