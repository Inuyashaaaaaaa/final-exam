from prettytable import PrettyTable


# please import prettytable at python packages. if you don't have any, pls install it. Thank you!

def strand():
    print("Enter a strand option: \n"
          "1 - STEM (Science, Technology, Engineering and Mathematics)\n"
          "2 - HUMSS (Humanities and Social Sciences)\n"
          "3 - ABM (Accountancy and Business Management)\n"
          "4 - EIM(Electrical Installation Management)\n"
          "5 - CBF (Cookery, Bread and Pastries, Food and Beverages)\n"
          "6 - AS (Automotive Servicing) \n"
          "7 - Exit")


def intro():
    print("Welcome to the Student Database of DIHS!\n"
          "1. Login as Student\n"
          "2. Login as Faculty\n"
          "3. Exit")


def gradelevel():
    print("What Grade level?\n"
          "1 - Grade 11\n"
          "2 - Grade 12\n"
          "3 - Back")


def semester():
    print("What Semester?\n"
          "1 - First Semester\n"
          "2 - Second Semester\n"
          "3 - Back")


def ap():
    print("What should we do today?\n"
          "1 - Add Subject\n"
          "2 - Modify Subject\n"
          "3 - Delete Subject\n"
          "4 - Exit")


# grade level, sem at strand

intro()
opt1 = input("Login as: ")
while opt1 != 4:
    # OPTION 1 FOR STUDENTS
    if opt1 == "1":
        gradelevel()
        gradelevelopt = input("Enter an option: ")  # grade level option. choose if 1 - grade 11 or 2 - grade 12
        while gradelevelopt != 4:
            if gradelevelopt == "1":  # grade 11
                semester()
                semesteropt = input("Enter an option: ")  # choose what semester
                while semesteropt != 4:
                    if semesteropt == "1":  # this directs to first semester subject view
                        strand()
                        strandopt = input("Enter an option: ")
                        while strandopt != "8":  # G11 FIRST SEM SUBJECTS VIEW , Users will choose strand
                            if strandopt == "1":
                                with open('Stem1stSemG11.txt', 'r') as gg:
                                    contents = gg.read()
                                myTable = PrettyTable(["Grade 11 STEM FIRST SEMESTER"])
                                myTable.add_row([contents])
                                print(myTable)
                                opt33 = input("Type any key to exit. ")
                                break
                            elif strandopt == "2":
                                with open('Humss1stSemG11.txt', 'r') as gg:
                                    contents = gg.read()
                                myTable = PrettyTable(["Grade 11 HUMSS FIRST SEMESTER"])
                                myTable.add_row([contents])
                                print(myTable)
                                opt33 = input("Type any key to exit. ")
                                break
                            elif strandopt == "3":
                                with open('Abm1stSemG11.txt', 'r') as gg:
                                    contents = gg.read()
                                myTable = PrettyTable(["Grade 11 ABM FIRST SEMESTER"])
                                myTable.add_row([contents])
                                print(myTable)
                                opt33 = input("Type any key to exit. ")
                                break
                            elif strandopt == "4":
                                with open('Eim1stSemG11.txt', 'r') as gg:
                                    contents = gg.read()
                                myTable = PrettyTable(["Grade 11 EIM FIRST SEMESTER"])
                                myTable.add_row([contents])
                                print(myTable)
                                opt33 = input("Type any key to exit. ")
                                break
                            elif strandopt == "5":
                                with open('Cbf1stSemG11.txt', 'r') as gg:
                                    contents = gg.read()
                                myTable = PrettyTable(["Grade 11 CBF FIRST SEMESTER"])
                                myTable.add_row([contents])
                                print(myTable)
                                opt33 = input("Type any key to exit. ")
                                break
                            elif strandopt == "6":
                                with open('AS1stSemG11.txt', 'r') as gg:
                                    contents = gg.read()
                                myTable = PrettyTable(["Grade 11 AS FIRST SEMESTER"])
                                myTable.add_row([contents])
                                print(myTable)
                                opt33 = input("Type any key to exit. ")
                                break
                            elif strandopt == "7":
                                print("Exiting...")
                                exit()
                            else:
                                print("Invalid Choice!")
                                strand()
                            strandopt = input("Enter an option: ")
                    # G11 second semester
                    if semesteropt == "2":
                        strand()
                        strandopt = input("Enter an option: ")  # they will choose their strand
                        while strandopt != "8":
                            if strandopt == "1":
                                with open('Stem2ndSemG11.txt', 'r') as gg:
                                    contents = gg.read()
                                myTable = PrettyTable(["Grade 11 STEM SECOND SEMESTER"])
                                myTable.add_row([contents])
                                print(myTable)
                                opt33 = input("Type any key to exit. ")
                                break
                            elif strandopt == "2":
                                with open('Humss2ndSemG11.txt', 'r') as gg:
                                    contents = gg.read()
                                myTable = PrettyTable(["Grade 11 HUMSS SECOND SEMESTER"])
                                myTable.add_row([contents])
                                print(myTable)
                                opt33 = input("Type any key to exit. ")
                                break
                            elif strandopt == "3":
                                with open('Abm2ndSemG11.txt', 'r') as gg:
                                    contents = gg.read()
                                myTable = PrettyTable(["Grade 11 ABM SECOND SEMESTER"])
                                myTable.add_row([contents])
                                print(myTable)
                                opt33 = input("Type any key to exit. ")
                                break
                            elif strandopt == "4":
                                with open('Eim2ndSemG11.txt', 'r') as gg:
                                    contents = gg.read()
                                myTable = PrettyTable(["Grade 11 EIM SECOND SEMESTER"])
                                myTable.add_row([contents])
                                print(myTable)
                                opt33 = input("Type any key to exit. ")
                                break
                            elif strandopt == "5":
                                with open('Cbf2ndSemG11.txt', 'r') as gg:
                                    contents = gg.read()
                                myTable = PrettyTable(["Grade 11 CBF SECOND SEMESTER"])
                                myTable.add_row([contents])
                                print(myTable)
                                opt33 = input("Type any key to exit. ")
                                break
                            elif strandopt == "6":
                                with open('AS2ndSemG11.txt', 'r') as gg:
                                    contents = gg.read()
                                myTable = PrettyTable(["Grade 11 AS SECOND SEMESTER"])
                                myTable.add_row([contents])
                                print(myTable)
                                opt33 = input("Type any key to exit. ")
                                break
                            elif strandopt == "7":
                                print("Exiting...")
                                exit()
                            else:
                                print("Invalid Choice!")
                                strand()
                            strandopt = input("Enter an option: ")
                    if semesteropt == "3":
                        print("Exiting")
                        quit()

            elif gradelevelopt == "2":  # grade 12 view record
                semester()
                semesteropt = input("Enter an option: ")
                while semesteropt != 4:
                    if semesteropt == "1":  # GRADE 12 1ST SEMESTER
                        strand()
                        strandopt = input("Enter an option: ")
                        while strandopt != "8":
                            if strandopt == "1":
                                with open('Stem1stSemG12.txt', 'r') as gg:
                                    contents = gg.read()
                                myTable = PrettyTable(["Grade 12 STEM FIRST SEMESTER"])
                                myTable.add_row([contents])
                                print(myTable)
                                opt33 = input("Type any key to exit. ")
                                break
                            elif strandopt == "2":
                                with open('Humss1stSemG12.txt', 'r') as gg:
                                    contents = gg.read()
                                myTable = PrettyTable(["Grade 12 HUMSS FIRST SEMESTER"])
                                myTable.add_row([contents])
                                print(myTable)
                                opt33 = input("Type any key to exit. ")
                                break
                            elif strandopt == "3":
                                with open('Abm1stSemG12.txt', 'r') as gg:
                                    contents = gg.read()
                                myTable = PrettyTable(["Grade 12 ABM FIRST SEMESTER"])
                                myTable.add_row([contents])
                                print(myTable)
                                opt33 = input("Type any key to exit. ")
                                break
                            elif strandopt == "4":
                                with open('Eim1stSemG12.txt', 'r') as gg:
                                    contents = gg.read()
                                myTable = PrettyTable(["Grade 12 EIM FIRST SEMESTER"])
                                myTable.add_row([contents])
                                print(myTable)
                                opt33 = input("Type any key to exit. ")
                                break
                            elif strandopt == "5":
                                with open('Cbf1stSemG12.txt', 'r') as gg:
                                    contents = gg.read()
                                myTable = PrettyTable(["Grade 12 CBF FIRST SEMESTER"])
                                myTable.add_row([contents])
                                print(myTable)
                                opt33 = input("Type any key to exit. ")
                                break
                            elif strandopt == "6":
                                with open('AS1stSemG12.txt', 'r') as gg:
                                    contents = gg.read()
                                myTable = PrettyTable(["Grade 12 AS FIRST SEMESTER"])
                                myTable.add_row([contents])
                                print(myTable)
                                opt33 = input("Type any key to exit. ")
                                break
                            elif strandopt == "7":
                                print("Exiting...")
                                exit()
                            else:
                                print("Invalid Choice!")
                                strand()
                            strandopt = input("Enter an option: ")
                        # G12 2ND SEMESTER VIEW RECORD
                    if semesteropt == "2":
                        strand()
                        strandopt = input("Enter an option: ")
                        while strandopt != "8":
                            if strandopt == "1":
                                with open('Stem2ndSemG12.txt', 'r') as gg:
                                    contents = gg.read()
                                myTable = PrettyTable(["Grade 12 STEM SECOND SEMESTER"])
                                myTable.add_row([contents])
                                print(myTable)
                                opt33 = input("Type any key to exit. ")
                                break
                            elif strandopt == "2":
                                with open('Humss2ndSemG12.txt', 'r') as gg:
                                    contents = gg.read()
                                myTable = PrettyTable(["Grade 12 HUMSS SECOND SEMESTER"])
                                myTable.add_row([contents])
                                print(myTable)
                                opt33 = input("Type any key to exit. ")
                                break
                            elif strandopt == "3":
                                with open('Abm2ndSemG12.txt', 'r') as gg:
                                    contents = gg.read()
                                myTable = PrettyTable(["Grade 12 ABM SECOND SEMESTER"])
                                myTable.add_row([contents])
                                print(myTable)
                                opt33 = input("Type any key to exit. ")
                                break
                            elif strandopt == "4":
                                with open('Eim2ndSemG12.txt', 'r') as gg:
                                    contents = gg.read()
                                myTable = PrettyTable(["Grade 12 EIM SECOND SEMESTER"])
                                myTable.add_row([contents])
                                print(myTable)
                                opt33 = input("Type any key to exit. ")
                                break
                            elif strandopt == "5":
                                with open('Cbf2ndSemG12.txt', 'r') as gg:
                                    contents = gg.read()
                                myTable = PrettyTable(["Grade 12 CBF SECOND SEMESTER"])
                                myTable.add_row([contents])
                                print(myTable)
                                opt33 = input("Type any key to exit. ")
                                break
                            elif strandopt == "6":
                                with open('AS2ndSemG12.txt', 'r') as gg:
                                    contents = gg.read()
                                myTable = PrettyTable(["Grade 12 AS SECOND SEMESTER"])
                                myTable.add_row([contents])
                                print(myTable)
                                opt33 = input("Type any key to exit. ")
                                break
                            elif strandopt == "7":
                                print("Exiting...")
                                exit()
                            else:
                                print("Invalid Choice!")
                                strand()
                            strandopt = input("Enter an option: ")
                    if semesteropt == "3":
                        print("Exiting")
                        quit()

    # Faculty
    if opt1 == "2":  # select faculty option
        facultyu = input("Enter Username: ")
        facultyp = input("Enter Password: ")
        if facultyu == "admin":  # correct user
            print("Correct User")
            if facultyp == "password":  # correct password
                print("Correct Password.. Redirecting to login")
                print("Welcome to Admin Panel!")
                ap()
                # ap - admin panel
                ao = input("Please Enter an option: ")  # enters an option when you can add the record, delete records
                while ao != 5:
                    if ao == "1":  # this is add option
                        gradelevel()
                        ag = input("What Grade Level? ")  # asks user what grade level wants to add subject
                        while ag != 4:
                            if ag == "1":  # this is for grade 11 option
                                semester()
                                asem = input("Enter Semester: ")  # asks the user what semester wants to add subject
                                while asem != 4:
                                    if asem == "1":  # this is for first semester Grade 11
                                        strand()
                                        astrand = input("Enter Strand: ")  # asks what strand wants to add record
                                        while astrand != 8:
                                            if astrand == "1":
                                                with open('Stem1stSemG11.txt', 'a+') as f:
                                                    with open('Stem1stSemG11.txt', 'r') as gg:
                                                        contents = gg.read()
                                                        print(contents)
                                                    a = input("Type any subject you want to add: ")
                                                    f.write('\n' + a)
                                                    print("Credential Successfully Added!", )
                                                    break
                                            elif astrand == "2":
                                                with open('Humss1stSemG11.txt', 'a+') as f:
                                                    with open('Humss1stSemG11.txt', 'r') as gg:
                                                        contents = gg.read()
                                                        print(contents)
                                                    a = input("Type any subject you want to add: ")
                                                    f.write('\n' + a)
                                                    print("Credential Successfully Added!", )
                                                    break
                                            elif astrand == "3":
                                                with open('Abm1stSemG11.txt', 'a+') as f:
                                                    with open('Abm1stSemG11.txt', 'r') as gg:
                                                        contents = gg.read()
                                                        print(contents)
                                                    a = input("Type any subject you want to add: ")
                                                    f.write('\n' + a)
                                                    print("Credential Successfully Added!", )
                                                    break
                                            elif astrand == "4":
                                                with open('Eim1stSemG11.txt', 'a+') as f:
                                                    with open('Eim1stSemG11.txt', 'r') as gg:
                                                        contents = gg.read()
                                                        print(contents)
                                                    a = input("Type any subject you want to add: ")
                                                    f.write('\n' + a)
                                                    print("Credential Successfully Added!", )
                                                    break
                                            elif astrand == "5":
                                                with open('Cbf1stSemG11.txt', 'a+') as f:
                                                    with open('Cbf1stSemG11.txt', 'r') as gg:
                                                        contents = gg.read()
                                                        print(contents)
                                                    a = input("Type any subject you want to add: ")
                                                    f.write('\n' + a)
                                                    print("Credential Successfully Added!", )
                                                    break
                                            elif astrand == "6":
                                                with open('AS1stSemG11.txt', 'a+') as f:
                                                    with open('AS1stSemG11.txt', 'r') as gg:
                                                        contents = gg.read()
                                                        print(contents)
                                                    a = input("Type any subject you want to add: ")
                                                    f.write('\n' + a)
                                                    print("Credential Successfully Added!", )
                                                    break
                                            elif astrand == "7":
                                                print("Exiting...")
                                                exit()
                                            else:
                                                print("Invalid Choice!")
                                                strand()

                                            astrand = input("Enter Strand: ")
                                    elif asem == "2":  # second sem g11 add subject
                                        strand()
                                        astrand = input("Enter Strand: ")
                                        while astrand != 8:
                                            if astrand == "1":
                                                with open('Stem2ndSemG11.txt', 'a+') as f:
                                                    with open('Stem2ndSemG11.txt', 'r') as gg:
                                                        contents = gg.read()
                                                        print(contents)
                                                    a = input("Type any subject you want to add: ")
                                                    f.write('\n' + a)
                                                    print("Credential Successfully Added!", )
                                                    break
                                            elif astrand == "2":
                                                with open('Humss2ndSemG11.txt', 'a+') as f:
                                                    with open('HumssSemG11.txt', 'r') as gg:
                                                        contents = gg.read()
                                                        print(contents)
                                                    a = input("Type any subject you want to add: ")
                                                    f.write('\n' + a)
                                                    print("Credential Successfully Added!", )
                                                    break
                                            elif astrand == "3":
                                                with open('Abm2ndSemG11.txt', 'a+') as f:
                                                    with open('Abm2ndSemG11.txt', 'r') as gg:
                                                        contents = gg.read()
                                                        print(contents)
                                                    a = input("Type any subject you want to add: ")
                                                    f.write('\n' + a)
                                                    print("Credential Successfully Added!", )
                                                    break
                                            elif astrand == "4":
                                                with open('Eim2ndSemG11.txt', 'a+') as f:
                                                    with open('Eim2ndSemG11.txt', 'r') as gg:
                                                        contents = gg.read()
                                                        print(contents)
                                                    a = input("Type any subject you want to add: ")
                                                    f.write('\n' + a)
                                                    print("Credential Successfully Added!", )
                                                    break
                                            elif astrand == "5":
                                                with open('Cbf2ndSemG11.txt', 'a+') as f:
                                                    with open('Cbf2ndSemG11.txt', 'r') as gg:
                                                        contents = gg.read()
                                                        print(contents)
                                                    a = input("Type any subject you want to add: ")
                                                    f.write('\n' + a)
                                                    print("Credential Successfully Added!", )
                                                    break
                                            elif astrand == "6":
                                                with open('AS2ndSemG11.txt', 'a+') as f:
                                                    with open('AS2ndSemG11.txt', 'r') as gg:
                                                        contents = gg.read()
                                                        print(contents)
                                                    a = input("Type any subject you want to add: ")
                                                    f.write('\n' + a)
                                                    print("Credential Successfully Added!", )
                                                    break
                                            elif astrand == "7":
                                                print("Exiting...")
                                                exit()
                                            else:
                                                print("Invalid Choice!")
                                                strand()

                                            astrand = input("Enter Strand: ")
                                    elif asem == "3":
                                        exit()
                                    else:
                                        print("Invalid Option!")
                                        semester()
                                        asem = input("Enter Semester: ")
                            elif ag == "2":  # grade 12 option add sem
                                semester()
                                asem = input("Enter Semester: ")
                                while asem != 4:
                                    if asem == "1":  # first semester grade 12 add subject
                                        strand()
                                        astrand = input("Enter Strand: ")
                                        while astrand != 8:
                                            if astrand == "1":
                                                with open('Stem1stSemG12.txt', 'a+') as f:
                                                    with open('Stem1stSemG12.txt', 'r') as gg:
                                                        contents = gg.read()
                                                        print(contents)
                                                    a = input("Type any subject you want to add: ")
                                                    f.write('\n' + a)
                                                    print("Credential Successfully Added!", )
                                                    break
                                            elif astrand == "2":
                                                with open('Humss1stSemG12.txt', 'a+') as f:
                                                    with open('Humss1stSemG12.txt', 'r') as gg:
                                                        contents = gg.read()
                                                        print(contents)
                                                    a = input("Type any subject you want to add: ")
                                                    f.write('\n' + a)
                                                    print("Credential Successfully Added!", )
                                                    break
                                            elif astrand == "3":
                                                with open('Abm1stSemG12.txt', 'a+') as f:
                                                    with open('Abm1stSemG12.txt', 'r') as gg:
                                                        contents = gg.read()
                                                        print(contents)
                                                    a = input("Type any subject you want to add: ")
                                                    f.write('\n' + a)
                                                    print("Credential Successfully Added!", )
                                                    break
                                            elif astrand == "4":
                                                with open('Eim1stSemG12.txt', 'a+') as f:
                                                    with open('Eim1stSemG12.txt', 'r') as gg:
                                                        contents = gg.read()
                                                        print(contents)
                                                    a = input("Type any subject you want to add: ")
                                                    f.write('\n' + a)
                                                    print("Credential Successfully Added!", )
                                                    break
                                            elif astrand == "5":
                                                with open('Cbf1stSemG12.txt', 'a+') as f:
                                                    with open('Cbf1stSemG12.txt', 'r') as gg:
                                                        contents = gg.read()
                                                        print(contents)
                                                    a = input("Type any subject you want to add: ")
                                                    f.write('\n' + a)
                                                    print("Credential Successfully Added!", )
                                                    break
                                            elif astrand == "6":
                                                with open('AS1stSemG12.txt', 'a+') as f:
                                                    with open('AS1stSemG12.txt', 'r') as gg:
                                                        contents = gg.read()
                                                        print(contents)
                                                    a = input("Type any subject you want to add: ")
                                                    f.write('\n' + a)
                                                    print("Credential Successfully Added!", )
                                                    break
                                            elif astrand == "7":
                                                print("Exiting...")
                                                exit()
                                            else:
                                                print("Invalid Choice!")
                                                strand()
                                            astrand = input("Enter Strand: ")
                                    elif asem == "2":  # second semester g12 add subject
                                        strand()
                                        astrand = input("Enter Strand: ")
                                        while astrand != 8:
                                            if astrand == "1":
                                                with open('Stem2ndSemG12.txt', 'a+') as f:
                                                    with open('Stem2ndSemG12.txt', 'r') as gg:
                                                        contents = gg.read()
                                                        print(contents)
                                                    a = input("Type any subject you want to add: ")
                                                    f.write('\n' + a)
                                                    print("Credential Successfully Added!", )
                                                    break
                                            elif astrand == "2":
                                                with open('Humss2ndSemG12.txt', 'a+') as f:
                                                    with open('Humss2ndSemG12.txt', 'r') as gg:
                                                        contents = gg.read()
                                                        print(contents)
                                                    a = input("Type any subject you want to add: ")
                                                    f.write('\n' + a)
                                                    print("Credential Successfully Added!", )
                                                    break
                                            elif astrand == "3":
                                                with open('Abm2ndSemG12.txt', 'a+') as f:
                                                    with open('Abm2ndSemG12.txt', 'r') as gg:
                                                        contents = gg.read()
                                                        print(contents)
                                                    a = input("Type any subject you want to add: ")
                                                    f.write('\n' + a)
                                                    print("Credential Successfully Added!", )
                                                    break
                                            elif astrand == "4":
                                                with open('Eim2ndSemG12.txt', 'a+') as f:
                                                    with open('Eim2ndSemG12.txt', 'r') as gg:
                                                        contents = gg.read()
                                                        print(contents)
                                                    a = input("Type any subject you want to add: ")
                                                    f.write('\n' + a)
                                                    print("Credential Successfully Added!", )
                                                    break
                                            elif astrand == "5":
                                                with open('Cbf2ndSemG12.txt', 'a+') as f:
                                                    with open('Cbf2ndSemG12.txt', 'r') as gg:
                                                        contents = gg.read()
                                                        print(contents)
                                                    a = input("Type any subject you want to add: ")
                                                    f.write('\n' + a)
                                                    print("Credential Successfully Added!", )
                                                    break
                                            elif astrand == "6":
                                                with open('AS2ndSemG12.txt', 'a+') as f:
                                                    with open('AS2ndSemG12.txt', 'r') as gg:
                                                        contents = gg.read()
                                                        print(contents)
                                                    a = input("Type any subject you want to add: ")
                                                    f.write('\n' + a)
                                                    print("Credential Successfully Added!", )
                                                    break
                                            elif astrand == "7":
                                                print("Exiting...")
                                                exit()
                                            else:
                                                print("Invalid Choice!")
                                                strand()
                                            astrand = input("Enter Strand: ")
                                    elif asem == "3":
                                        exit()
                                    else:
                                        print("Invalid Option!")
                                        semester()
                                        asem = input("Enter Semester: ")
                            elif ag == "3":
                                exit()
                            else:
                                print("Invalid Choice!")
                                gradelevel()
                                ag = input("Enter Grade Level: ")
                    elif ao == "2":
                        # modifies subject records
                        gradelevel()
                        mg = input("What Grade Level? ")
                        while mg != 4:
                            if mg == "1":  # user selects grade 11
                                semester()
                                msem = input("Enter Semester: ")
                                while msem != 4:
                                    if msem == "1":  # user selects first semester
                                        strand()
                                        mstrand = input("Enter Strand: ")  # user chooses strands for grade 12 first sem
                                        while mstrand != 8:
                                            if mstrand == "1":
                                                with open('Stem1stSemG11.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Stem1stSemG11.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to modify: ")
                                                    b = input("Enter Subject do you want to be replaced: ")
                                                    new_text = text.replace(a, b)
                                                    file.write(new_text)
                                                    print("Credentials successfully modified!")
                                                    break
                                            elif mstrand == "2":
                                                with open('Humss1stSemG11.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Humss1stSemG11.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to modify: ")
                                                    b = input("Enter Subject do you want to be replaced: ")
                                                    new_text = text.replace(a, b)
                                                    file.write(new_text)
                                                    print("Credentials successfully modified!")
                                                    break
                                            elif mstrand == "3":
                                                with open('Abm1stSemG11.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Abm1stSemG11.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to modify: ")
                                                    b = input("Enter Subject do you want to be replaced: ")
                                                    new_text = text.replace(a, b)
                                                    file.write(new_text)
                                                    print("Credentials successfully modified!")
                                                    break
                                            elif mstrand == "4":
                                                with open('Eim1stSemG11.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Eim1stSemG11.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to modify: ")
                                                    b = input("Enter Subject do you want to be replaced: ")
                                                    new_text = text.replace(a, b)
                                                    file.write(new_text)
                                                    print("Credentials successfully modified!")
                                                    break
                                            elif mstrand == "5":
                                                with open('Cbf1stSemG11.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Cbf1stSemG11.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to modify: ")
                                                    b = input("Enter Subject do you want to be replaced: ")
                                                    new_text = text.replace(a, b)
                                                    file.write(new_text)
                                                    print("Credentials successfully modified!")
                                                    break
                                            elif mstrand == "6":
                                                with open('AS1stSemG11.txt', 'r') as file:
                                                    text = file.read()
                                                with open('AS1stSemG11.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to modify: ")
                                                    b = input("Enter Subject do you want to be replaced: ")
                                                    new_text = text.replace(a, b)
                                                    file.write(new_text)
                                                    print("Credentials successfully modified!")
                                                    break
                                            elif mstrand == "7":
                                                print("Exiting...")
                                                exit()
                                            else:
                                                print("Invalid Choice!")
                                                strand()

                                            dstrand = input("Enter Strand: ")
                                    elif msem == "2":  # user selects second sem for grade 11
                                        strand()
                                        mstrand = input("Enter Strand: ")
                                        while mstrand != 8:
                                            if mstrand == "1":
                                                with open('Stem2ndSemG11.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Stem2ndSemG11.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to modify: ")
                                                    b = input("Enter Subject do you want to be replaced: ")
                                                    new_text = text.replace(a, b)
                                                    file.write(new_text)
                                                    print("Credentials successfully modified!")
                                                    break
                                            elif mstrand == "2":
                                                with open('Humss2ndSemG11.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Humss2ndSemG11.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to modify: ")
                                                    b = input("Enter Subject do you want to be replaced: ")
                                                    new_text = text.replace(a, b)
                                                    file.write(new_text)
                                                    print("Credentials successfully modifed!")
                                                    break
                                            elif mstrand == "3":
                                                with open('Abm2ndSemG11.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Abm2ndSemG11.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to modify: ")
                                                    b = input("Enter Subject do you want to be replaced: ")
                                                    new_text = text.replace(a, b)
                                                    file.write(new_text)
                                                    print("Credentials successfully modified!")
                                                    break
                                            elif mstrand == "4":
                                                with open('Eim2ndSemG11.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Eim2ndSemG11.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to modify: ")
                                                    b = input("Enter Subject do you want to be replaced: ")
                                                    new_text = text.replace(a, b)
                                                    file.write(new_text)
                                                    print("Credentials successfully modified!")
                                                    break
                                            elif mstrand == "5":
                                                with open('Cbf2ndSemG11.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Cbf2ndSemG11.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to modify: ")
                                                    b = input("Enter Subject do you want to be replaced: ")
                                                    new_text = text.replace(a, b)
                                                    file.write(new_text)
                                                    print("Credentials successfully modified!")
                                                    break
                                            elif mstrand == "6":
                                                with open('AS2ndSemG11.txt', 'r') as file:
                                                    text = file.read()
                                                with open('AS2ndSemG11.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to modify: ")
                                                    b = input("Enter Subject do you want to be replaced: ")
                                                    new_text = text.replace(a, b)
                                                    file.write(new_text)
                                                    print("Credentials successfully modified!")
                                                    break
                                            elif mstrand == "7":
                                                print("Exiting...")
                                                exit()
                                            else:
                                                print("Invalid Choice!")
                                                strand()
                                            mstrand = input("Enter Strand: ")
                                    elif msem == "3":
                                        exit()
                                    else:
                                        print("Invalid Choice!")
                                        semester()
                                        msem = input("Enter Semester: ")
                            elif mg == "2":  # grade 12 modify records
                                semester()
                                msem = input("Enter Semester: ")
                                while msem != 4:
                                    if msem == "1":  # grade 12 first semester
                                        strand()
                                        mstrand = input("Enter Strand: ")
                                        while mstrand != 8:
                                            if mstrand == "1":
                                                with open('Stem1stSemG12.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Stem1stSemG12.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to modify: ")
                                                    b = input("Enter Subject do you want to be replaced: ")
                                                    new_text = text.replace(a, b)
                                                    file.write(new_text)
                                                    print("Credentials successfully modified!")
                                                    break
                                            elif mstrand == "2":
                                                with open('Humss1stSemG12.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Humss1stSemG12.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to modify: ")
                                                    b = input("Enter Subject do you want to be replaced: ")
                                                    new_text = text.replace(a, b)
                                                    file.write(new_text)
                                                    print("Credentials successfully modified!")
                                                    break
                                            elif mstrand == "3":
                                                with open('Abm1stSemG12.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Abm1stSemG12.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to modify: ")
                                                    b = input("Enter Subject do you want to be replaced: ")
                                                    new_text = text.replace(a, b)
                                                    file.write(new_text)
                                                    print("Credentials successfully modified!")
                                                    break
                                            elif mstrand == "4":
                                                with open('Eim1stSemG12.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Eim1stSemG12.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to modify: ")
                                                    b = input("Enter Subject do you want to be replaced: ")
                                                    new_text = text.replace(a, b)
                                                    file.write(new_text)
                                                    print("Credentials successfully modified!")
                                                    break
                                            elif mstrand == "5":
                                                with open('Cbf1stSemG12.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Cbf1stSemG12.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to modify: ")
                                                    b = input("Enter Subject do you want to be replaced: ")
                                                    new_text = text.replace(a, b)
                                                    file.write(new_text)
                                                    print("Credentials successfully modified!")
                                                    break
                                            elif mstrand == "6":
                                                with open('AS1stSemG12.txt', 'r') as file:
                                                    text = file.read()
                                                with open('AS1stSemG12.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to modify: ")
                                                    b = input("Enter Subject do you want to be replaced: ")
                                                    new_text = text.replace(a, b)
                                                    file.write(new_text)
                                                    print("Credentials successfully modified!")
                                                    break
                                            elif mstrand == "7":
                                                print("Exiting...")
                                                exit()
                                            else:
                                                print("Invalid Choice!")
                                                strand()

                                            mstrand = input("Enter Strand: ")
                                    elif msem == "2":  # grade 12 second sem modify record
                                        strand()
                                        mstrand = input("Enter Strand: ")
                                        while mstrand != 8:
                                            if mstrand == "1":
                                                with open('Stem2ndSemG12.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Stem2ndSemG12.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to modify: ")
                                                    b = input("Enter Subject do you want to be replaced: ")
                                                    new_text = text.replace(a, b)
                                                    file.write(new_text)
                                                    print("Credentials successfully modified!")
                                                    break
                                            elif mstrand == "2":
                                                with open('Humss2ndSemG12.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Humss2ndSemG12.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to modify: ")
                                                    b = input("Enter Subject do you want to be replaced: ")
                                                    new_text = text.replace(a, b)
                                                    file.write(new_text)
                                                    print("Credentials successfully modified!")
                                                    break
                                            elif mstrand == "3":
                                                with open('Abm2ndSemG12.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Abm2ndSemG12.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to modify: ")
                                                    b = input("Enter Subject do you want to be replaced: ")
                                                    new_text = text.replace(a, b)
                                                    file.write(new_text)
                                                    print("Credentials successfully modified!")
                                                    break
                                            elif mstrand == "4":
                                                with open('Eim2ndSemG12.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Eim2ndSemG12.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to modify: ")
                                                    b = input("Enter Subject do you want to be replaced: ")
                                                    new_text = text.replace(a, b)
                                                    file.write(new_text)
                                                    print("Credentials successfully modified!")
                                                    break
                                            elif mstrand == "5":
                                                with open('Cbf2ndSemG12.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Cbf2ndSemG12.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to modify: ")
                                                    b = input("Enter Subject do you want to be replaced: ")
                                                    new_text = text.replace(a, b)
                                                    file.write(new_text)
                                                    print("Credentials successfully modified!")
                                                    break
                                            elif mstrand == "6":
                                                with open('AS2ndSemG12.txt', 'r') as file:
                                                    text = file.read()
                                                with open('AS2ndSemG12.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to modify: ")
                                                    b = input("Enter Subject do you want to be replaced: ")
                                                    new_text = text.replace(a, b)
                                                    file.write(new_text)
                                                    print("Credentials successfully modified!")
                                                    break
                                            elif mstrand == "7":
                                                print("Exiting...")
                                                exit()
                                            else:
                                                print("Invalid Choice!")
                                                strand()
                                            mstrand = input("Enter Strand: ")
                                    elif msem == "3":
                                        exit()
                                    else:
                                        print("Invalid Choice!")
                                        semester()
                                        dsem = input("Enter Semester: ")
                            elif mg == "3":
                                exit()
                            else:
                                print("Invalid Choice!")
                                gradelevel()
                                mg = input("What Grade Level? ")
                    elif ao == "3":
                        # deletes subject records
                        gradelevel()
                        dg = input("What Grade Level? ")
                        while dg != 4:
                            if dg == "1":  # user selects grade 11
                                semester()
                                dsem = input("Enter Semester: ")
                                while dsem != 4:
                                    if dsem == "1":  # user selects first semester
                                        strand()
                                        dstrand = input("Enter Strand: ")  # user chooses strands for grade 12 first sem
                                        while dstrand != 8:
                                            if dstrand == "1":
                                                with open('Stem1stSemG11.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Stem1stSemG11.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to remove: ")
                                                    new_text = text.replace("\n" + a, '')
                                                    file.write(new_text)
                                                    print("Credentials successfully removed!")
                                                    break
                                            elif dstrand == "2":
                                                with open('Humss1stSemG11.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Humss1stSemG11.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to remove: ")
                                                    new_text = text.replace("\n" + a, '')
                                                    file.write(new_text)
                                                    print("Credentials successfully removed!")
                                                    break
                                            elif dstrand == "3":
                                                with open('Abm1stSemG11.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Abm1stSemG11.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to remove: ")
                                                    new_text = text.replace("\n" + a, '')
                                                    file.write(new_text)
                                                    print("Credentials successfully removed!")
                                                    break
                                            elif dstrand == "4":
                                                with open('Eim1stSemG11.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Eim1stSemG11.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to remove: ")
                                                    new_text = text.replace("\n" + a, '')
                                                    file.write(new_text)
                                                    print("Credentials successfully removed!")
                                                    break
                                            elif dstrand == "5":
                                                with open('Cbf1stSemG11.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Cbf1stSemG11.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to remove: ")
                                                    new_text = text.replace("\n" + a, '')
                                                    file.write(new_text)
                                                    print("Credentials successfully removed!")
                                                    break
                                            elif dstrand == "6":
                                                with open('AS1stSemG11.txt', 'r') as file:
                                                    text = file.read()
                                                with open('AS1stSemG11.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to remove: ")
                                                    new_text = text.replace("\n" + a, '')
                                                    file.write(new_text)
                                                    print("Credentials successfully removed!")
                                                    break
                                            elif dstrand == "7":
                                                print("Exiting...")
                                                exit()
                                            else:
                                                print("Invalid Choice!")
                                                strand()

                                            dstrand = input("Enter Strand: ")
                                    elif dsem == "2":  # user selects second sem for grade 11
                                        strand()
                                        dstrand = input("Enter Strand: ")
                                        while dstrand != 8:
                                            if dstrand == "1":
                                                with open('Stem2ndSemG11.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Stem2ndSemG11.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to remove: ")
                                                    new_text = text.replace("\n" + a, '')
                                                    file.write(new_text)
                                                    print("Credentials successfully removed!")
                                                    break
                                            elif dstrand == "2":
                                                with open('Humss2ndSemG11.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Humss2ndSemG11.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to remove: ")
                                                    new_text = text.replace("\n" + a, '')
                                                    file.write(new_text)
                                                    print("Credentials successfully removed!")
                                                    break
                                            elif dstrand == "3":
                                                with open('Abm2ndSemG11.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Abm2ndSemG11.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to remove: ")
                                                    new_text = text.replace("\n" + a, '')
                                                    file.write(new_text)
                                                    print("Credentials successfully removed!")
                                                    break
                                            elif dstrand == "4":
                                                with open('Eim2ndSemG11.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Eim2ndSemG11.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to remove: ")
                                                    new_text = text.replace("\n" + a, '')
                                                    file.write(new_text)
                                                    print("Credentials successfully removed!")
                                                    break
                                            elif dstrand == "5":
                                                with open('Cbf2ndSemG11.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Cbf2ndSemG11.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to remove: ")
                                                    new_text = text.replace("\n" + a, '')
                                                    file.write(new_text)
                                                    print("Credentials successfully removed!")
                                                    break
                                            elif dstrand == "6":
                                                with open('AS2ndSemG11.txt', 'r') as file:
                                                    text = file.read()
                                                with open('AS2ndSemG11.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to remove: ")
                                                    new_text = text.replace("\n" + a, '')
                                                    file.write(new_text)
                                                    print("Credentials successfully removed!")
                                                    break
                                            elif dstrand == "7":
                                                print("Exiting...")
                                                exit()
                                            else:
                                                print("Invalid Choice!")
                                                strand()
                                            dstrand = input("Enter Strand: ")
                                    elif dsem == "3":
                                        exit()
                                    else:
                                        print("Invalid Choice!")
                                        semester()
                                        dsem = input("Enter Semester: ")
                            elif dg == "2":  # grade 12 delete records
                                semester()
                                dsem = input("Enter Semester: ")
                                while dsem != 4:
                                    if dsem == "1":  # grade 12 first semester
                                        strand()
                                        dstrand = input("Enter Strand: ")
                                        while dstrand != 8:
                                            if dstrand == "1":
                                                with open('Stem1stSemG12.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Stem1stSemG12.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to remove: ")
                                                    new_text = text.replace("\n" + a, '')
                                                    file.write(new_text)
                                                    print("Credentials successfully removed!")
                                                    break
                                            elif dstrand == "2":
                                                with open('Humss1stSemG12.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Humss1stSemG12.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to remove: ")
                                                    new_text = text.replace("\n" + a, '')
                                                    file.write(new_text)
                                                    print("Credentials successfully removed!")
                                                    break
                                            elif dstrand == "3":
                                                with open('Abm1stSemG12.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Abm1stSemG12.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to remove: ")
                                                    new_text = text.replace("\n" + a, '')
                                                    file.write(new_text)
                                                    print("Credentials successfully removed!")
                                                    break
                                            elif dstrand == "4":
                                                with open('Eim1stSemG12.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Eim1stSemG12.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to remove: ")
                                                    new_text = text.replace("\n" + a, '')
                                                    file.write(new_text)
                                                    print("Credentials successfully removed!")
                                                    break
                                            elif dstrand == "5":
                                                with open('Cbf1stSemG12.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Cbf1stSemG12.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to remove: ")
                                                    new_text = text.replace("\n" + a, '')
                                                    file.write(new_text)
                                                    print("Credentials successfully removed!")
                                                    break
                                            elif dstrand == "6":
                                                with open('AS1stSemG12.txt', 'r') as file:
                                                    text = file.read()
                                                with open('AS1stSemG12.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to remove: ")
                                                    new_text = text.replace("\n" + a, '')
                                                    file.write(new_text)
                                                    print("Credentials successfully removed!")
                                                    break
                                            elif dstrand == "7":
                                                print("Exiting...")
                                                exit()
                                            else:
                                                print("Invalid Choice!")
                                                strand()

                                            dstrand = input("Enter Strand: ")
                                    elif dsem == "2":  # grade 12 second sem del record
                                        strand()
                                        dstrand = input("Enter Strand: ")
                                        while dstrand != 8:
                                            if dstrand == "1":
                                                with open('Stem2ndSemG12.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Stem2ndSemG12.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to remove: ")
                                                    new_text = text.replace("\n" + a, '')
                                                    file.write(new_text)
                                                    print("Credentials successfully removed!")
                                                    break
                                            elif dstrand == "2":
                                                with open('Humss2ndSemG12.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Humss2ndSemG12.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to remove: ")
                                                    new_text = text.replace("\n" + a, '')
                                                    file.write(new_text)
                                                    print("Credentials successfully removed!")
                                                    break
                                            elif dstrand == "3":
                                                with open('Abm2ndSemG12.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Abm2ndSemG12.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to remove: ")
                                                    new_text = text.replace("\n" + a, '')
                                                    file.write(new_text)
                                                    print("Credentials successfully removed!")
                                                    break
                                            elif dstrand == "4":
                                                with open('Eim2ndSemG12.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Eim2ndSemG12.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to remove: ")
                                                    new_text = text.replace("\n" + a, '')
                                                    file.write(new_text)
                                                    print("Credentials successfully removed!")
                                                    break
                                            elif dstrand == "5":
                                                with open('Cbf2ndSemG12.txt', 'r') as file:
                                                    text = file.read()
                                                with open('Cbf2ndSemG12.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to remove: ")
                                                    new_text = text.replace("\n" + a, '')
                                                    file.write(new_text)
                                                    print("Credentials successfully removed!")
                                                    break
                                            elif dstrand == "6":
                                                with open('AS2ndSemG12.txt', 'r') as file:
                                                    text = file.read()
                                                with open('AS2ndSemG12.txt', 'w') as file:
                                                    a = input("Enter Subject do you want to remove: ")
                                                    new_text = text.replace("\n" + a, '')
                                                    file.write(new_text)
                                                    print("Credentials successfully removed!")
                                                    break
                                            elif dstrand == "7":
                                                print("Exiting...")
                                                exit()
                                            else:
                                                print("Invalid Choice!")
                                                strand()
                                            dstrand = input("Enter Strand: ")
                                    elif dsem == "3":
                                        exit()
                                    else:
                                        print("Invalid Choice!")
                                        semester()
                                        dsem = input("Enter Semester: ")
                            elif dg == "3":
                                exit()
                            else:
                                print("Invalid Choice!")
                                gradelevel()
                                dg = input("What Grade Level? ")
                    elif ao == "4":
                        exit()
                    else:
                        print("Invalid Choice")
                        ap()
                        ao = input("Please Enter an option: ")
            else:
                print("Correct user, but incorrect password!")
        else:
            print("Incorrect User")
    elif opt1 == "3":
        quit()
    else:
        print("Invalid Option!")
