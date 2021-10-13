class Grade:
    def __init__(self, date, grade):
        self.date = date
        self.grade = grade

    def __str__(self):
        return self.date + ": " + self.grade


class GradeList:
    def __init__(self, grade_list=None):
        if grade_list:
            for el in grade_list:
                self.check_grade_instance(el)
        self.grade_list = grade_list if grade_list else []

    def check_grade_instance(self, obj):
        if not isinstance(obj, Grade):
            raise TypeError("Only instance of class Grade can be added to GradeList")

    def add_grade(self, grade):
        self.check_grade_instance(grade)
        self.grade_list.append(grade)

    def remove_grade(self, grade):
        self.check_grade_instance(grade)
        self.grade_list.remove(grade)

    def __str__(self):
        return str([str(i) for i in self.grade_list] if self.grade_list else "No grades yet")


class Student:
    def __init__(self, name, grade_list=None):
        if grade_list is not None:
            self.check_grade_list_instance(grade_list)
        self.name = name
        self.grade_list = grade_list if grade_list else GradeList()

    def __str__(self):
        return self.name +": "+ str(self.grade_list)

    def check_grade_list_instance(self, obj):
        if not isinstance(obj, GradeList):
            raise TypeError("Only instance of class GradeList can be part of Student instance")

    def add_grade_list(self, grade_list):
        self.check_grade_list_instance(grade_list)
        self.grade_list = grade_list

    def change_name(self, new_name):
        self.name = new_name


class Journal:
    def __init__(self, student_list=None):
        if student_list:
            for el in student_list:
                self.check_student_instance(el)
        self.student_list = student_list if student_list else []

    def check_student_instance(self, obj):
        if not isinstance(obj, Student):
            raise TypeError("Only instance of class Student can be added to Journal")

    def add_student(self, student):
        self.check_student_instance(student)
        self.student_list.append(student)

    def display_journal(self):
        print("Students:")
        for el in self.student_list:
            print(el)

    def remove_student(self, student):
        self.check_student_instance(student)
        if student in self.student_list:
            self.student_list.remove(student)

student1 = Student("Alex",)
student2 = Student("Bob",)

grade_list1 = GradeList([Grade("11.12.21", "5"), Grade("01.12.21", "5"),Grade("11.02.21", "4"),Grade("01.07.21", "3"), ])
student3 = Student("Olga", grade_list1)
print(student3)
print(student2)
student2.grade_list.add_grade(Grade("03.03.21", "5"))
print(student2.grade_list)

journal = Journal([student1, student2])
journal.display_journal()
journal.add_student(student3)
journal.display_journal()
journal.remove_student(student2)
journal.display_journal()


