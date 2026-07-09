class School:
    def __init__(self, name, rollno, student_class, marks):
        self.name = name
        self.rollno = rollno
        self.student_class = student_class
        self.marks = marks

    def show_student_marks(self):
        print("Name:", self.name)
        print("Rollno:", self.rollno)
        print("Class:", self.student_class)
        print("Marks:", self.marks)

    def marks_list(self):
        if self.marks >= 60:
            print("PASS")
        else:
            print("FAIL")

    def student_grade(self):
        if self.marks >= 90:
            print("Grade A+")
        elif self.marks >= 80:
            print("Grade A")
        elif self.marks >= 70:
            print("Grade B")
        elif self.marks >= 60:
            print("Grade C")
        else:
            print("Fail")


s1 = School("Funny", 12, 9, 73)
s2 = School("Sunny", 12, 9, 56)
s3 = School("Suman", 26, 9, 62)
s4 = School("Anas", 9, 9, 97)

s1.show_student_marks()
s1.marks_list()
s1.student_grade()

print("--------------------")

s2.show_student_marks()
s2.marks_list()
s2.student_grade()

print("--------------------")

s3.show_student_marks()
s3.marks_list()
s3.student_grade()

print("--------------------")

s4.show_student_marks()
s4.marks_list()
s4.student_grade()
