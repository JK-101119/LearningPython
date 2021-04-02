class Student:
    def __init__(self, rollNo, name, course):
        self.rollNo = rollNo
        self.name = name
        self.course = course

    def myFun(self):
        print("Hello", self.name)


student1 = Student('1011', 'Jhon', 'MCA')
student2 = Student('1012', 'Danny', 'Bsc. Math')
student3 = Student('1013', 'Kathrin', 'MBA')

print("Name : ", student1.name)
print("Roll No. : ", student1.rollNo)
print("Course : ", student1.course)
print("----------------------------------------------------------------")
print("Name : ", student2.name)
print("Roll No. : ", student2.rollNo)
print("Course : ", student2.course)
print("----------------------------------------------------------------")
print("Name : ", student3.name)
print("Roll No.: ", student3.rollNo)
print("Course : ", student3.course)

student1.myFun()
 