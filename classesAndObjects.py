# classes and objects

from student import Student

student1 = Student("Mike", "Business", 3.2, False)
student2 = Student("Harry", "Magic", 3.8, False)

print("Student Name: ", student1.name)
print("Student Major: ", student1.major)
print("Student GPA: ", student1.gpa)

print(student2.on_honor_roll())

# ...end
