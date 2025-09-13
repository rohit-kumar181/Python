student_dictionary = {'Alice':85, 'Bob':78, 'Charles':87}

name = input("Enter the student's name: ")

if((name in student_dictionary) == True):
    print(f"{name}'s marks: {student_dictionary[name]}")
else:
    print("Student not found.")
