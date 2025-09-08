class Student:

    def __init__(self, name, student_id):
        self.age = None
        self.score = None
        self._name = name
        self._student_id = student_id
        self._grade = {}

    # python 버전의 getter에 해당
    @property
    def name(self):
        return self._name

    # python 버전의 setter
    @name.setter
    def name(self,value):
        self._name = value

    def set_score(self, score):
        if 0.0 <= score <= 4.5:
            self.score = score

    def set_age(self, age):
        if 0 <= age <= 200:
            self.age = age

student1 = Student('김일', 2025001)

print(f'학생 이름 : {student1.name}')

student1.name = '김영'
print(f'변경된 학생 이름 : {student1.name}')