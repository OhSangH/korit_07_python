class Student():
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grade = {}

    def add_grade(self, subject,grade):
        self.grade[subject] = grade

    def get_average_grade(self):
        return sum(self.grade.values()) / len(self.grade)

    def show_info(self):
        print(f'이름 : {self.name}')
        print(f'성적 평균 : {Student.get_average_grade(self)}')

student1 = Student('김일', 2025001)
student1.add_grade('korean', 80)
student1.add_grade('english', 90)
student1.add_grade('math', 100)

student1.show_info()