class Class:
    students = []
    grades = []
    __students_count = 22

    def __init__(self, name):
        self.name = name

    def add_student(self, name: str, grade: float):
        if Class.__students_count > 0:
            Class.students.append(name)
            Class.grades.append(grade)
            Class.__students_count -= 1

    def get_average_grade(self):
        average_grade = sum(Class.grades) / len(Class.grades)
        return f'{average_grade:.2f}'

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(Class.students)}. Average grade:" \
               f" {Class.get_average_grade(self)} "


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)

