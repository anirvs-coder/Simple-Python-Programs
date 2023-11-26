def calc_gpa():
    return None


class Student:
    def __init__(self, first_name, last_name, age, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grade = grade


Anirv = Student("Anirv", "S", 11, 6)
Advaith = Student("Advaith", "S", 16, 12)
Pete = Student("Pete", "Gar", 14, 9)
Pranav = Student("Pranav", "Mad", 12, 7)
Rachel = Student("Rachel", "Mad", 15, 11)

student_list = {
    'Anirv': Anirv,
    'Advaith': Advaith,
    'Pete': Pete,
    'Pranav': Pranav,
    'Rachel': Rachel
}


def student_attribute_finder(student, attribute):
    if attribute == "age":
        print(f"{student.first_name} is {student.age} years old.")
    elif attribute == "grade":
        print(f"{student.first_name} is in {student.grade}'th grade.")
    elif attribute == "first name":
        print(f"{student.first_name} first name is {student.first_name}.")
    elif attribute == "last name":
        print(f"{student.first_name} last name is {student.last_name}.")
    else:
        print("ERROR.ERROR.ERROR.ERROR.")


name_of_student_to_find = input("What student would you like to access:")
att_of_student_to_find = input("Of " + name_of_student_to_find + ", which attribute would you like to see:")

if name_of_student_to_find in student_list:
    student_attribute_finder(student_list[name_of_student_to_find], att_of_student_to_find)
else:
    print(f'Student {name_of_student_to_find} is not found in our database')
