class Candy2:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def show_info(self):
        print(f'사탕읜 모양은 {self.shape}이고, 색깔은 {self.color}이다.')


# satang1 = Candy2('정육면체', '흰색')
# satang1.show_info()
#
# class Sample:
#     def __init__(self):
#         print('인스턴스가 생성되었습니다.')
#     # 소멸자
#     def __del__(self):
#         print('인스턴스가 소멸되었습니다.')
#
# sample = Sample()
# print()
# # 객체 소멸자 호출 방법
# del sample          # del 객체명
# print('객체 지운 후의 코드라인입니다.')
'''
usb 인스턴스를 만드는 프로그램 작성
1. 클래스 USB를 정의
2. 생성자를 정의하여 매개변수로 capacity를 받을 것
3. get_info() 메서드를 정의 할 것

main 단계 코드
usb = USB(64)
usb.get_info()

실행 예
USB 객체가 생성되었습니다.
64GB USB
'''


class USB:
    def __init__(self, capacity):
        self.capacity = capacity
        print('USB 객체가 생성되었습니다.')

    def get_info(self):
        print(f'{self.capacity}GB USB')


usb = USB(64)
usb.get_info()

'''
1. 다음 지시 사항을 읽고 이름을 저장하는 Person 클래스를 생성하시오.

지시 사항

1. 다음과 같은 방법으로 man과 woman 인스턴스를 생성하시오.
man = Person("james")
woman = Person("emily")
2. man과 woman 인스턴스가 생성되면 다음과 같은 메시지를 출력할 수 있도록 작성하시오.
james is born.
emily is born.

3. 다음과 같은 방법으로 man 인스턴스를 삭제하시오.
del man

4. man 인스턴스가 삭제되면 다음과 같은 메시지를 출력할 수 있도록 작성하시오.
james is dead.
'''

# class Person:
#     def __init__(self, name):
#         self.name = name
#         print(f'{self.name} is born')
#
#     def __del__(self):
#         print(f'{self.name} is dead')
#
#
# man = Person("james")
# woman = Person("emily")
# del man


'''
지시사항 name/ age/ address / score 속성을 setter통해서 추가하시오
이상의 속성에 맞는 getter도 추가하시오

student1 객체를 생성
김일, 20 , 4.5 를 각각 이름/나이/점수에 대입

getter만 활용하여
김일 학생의 나이는 20살로 , 파이썬 과목의 점수는 4.5 점입니다.

'''


class Student:
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        if 0 <= age <= 200:
            self.age = age

    def set_address(self, address):
        self.address = address

    def set_score(self, score):
        if 0.0 <= score <= 4.5:
            self.score = score

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_address(self):
        return self.address

    def get_score(self):
        return self.score


student1 = Student()
student1.set_name('김일')
student1.set_age(20)
student1.set_score(4.5)
print(f'{student1.get_name()}학생의 나이는{student1.get_age()}살로, 파이썬 과목의 점수는{student1.get_score()}점 입니다.')

student1.set_age(300)
print(f'{student1.get_age()}')
