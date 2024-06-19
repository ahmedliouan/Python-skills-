firstname = input("Enter the first student's name: ")
firstid = input("Enter the first student's ID: ")
firstgrade = float(input("Enter the first student's grade: "))  # Convert to float

secondname = input("Enter the second student's name: ")
secondid = input("Enter the second student's ID: ")
secondgrade = float(input("Enter the second student's grade: "))  # Convert to float

print("Information for students and their Math grades:")
print(firstname, "(ID", firstid, ")", "got grade:", firstgrade)
print(secondname, "(ID", secondid, ")", "got grade:", secondgrade)
print("Average math grade is", (firstgrade + secondgrade) / 2)
