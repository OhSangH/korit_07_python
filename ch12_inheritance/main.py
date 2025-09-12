'''
상속

형식 :
class 슈퍼클래스:
    본문

class 서브클래스(슈퍼클래스):
    본문
'''
from pyclbr import Class
from typing import override

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self, food):
#         print(f'{self.name}이(가) {food}를 먹습니다.')
#
#
# class Student(Person):
#
#     def __init__(self, name, school):
#         super().__init__(name)
#         self.school = school
#
#     def study(self):
#         print(f'{self.name}은(는) {self.school}에서 공부를 합니다.')
#
#     def eat(self, food):
#         print(f'{self.school}에서', end=' ')
#         super().eat(food)
#
#
# # 객체 생성
# potter = Student('해리 포터', '호그와트')
# potter.eat('감자')
# potter.study()
#
# print(isinstance(potter, Person))
# print(isinstance(potter, Student))

"""
지시사항
1. 다음과 같은 슈퍼 클래스 Car를 가지고 있는 Hybrid 클래스 구현
2. 서브 클래스 Hybrid는 다음과 같은 특징을 지니고 있습니다.
    1) 최대 배터리 충전량은 30
    2) 배터리를 충전하는 charge() 메서드가 존재. 최대 충전량을 초과할 수 없고, 0보다 작은 값으로 충전 할 수 없습니다.
    3) 현재 주유량과 충전량을 모두 확인할 수 있느 hybrid_info() 메서드가 존재.
3. 다음과 같은 방식으로 전체 동작 확인 가능.
car = Hybrid(oil = 0, amount = 0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()

실행 예
하이브리드 차량이 생산되었습니다.
기름을 50 주유 했습니다.
전기를 30 충전 했습니다.
현재 주유 상태 : 50
현재 충전 상태 : 30
"""

# class Car:
#     max_oil = 50
#
#     def __init__(self, oil=0):
#         self.oil = oil
#
#     def add_oil(self, oil):
#         if oil <= 0:
#             return
#         if self.oil + oil > Car.max_oil:
#             print(f'기름을 {Car.max_oil - self.oil} 주유 했습니다.')
#             self.oil = Car.max_oil
#         else:
#             print(f'기름을 {oil} 주유 했습니다.')
#             self.oil += oil
#
#     def car_info(self):
#         print(f'현재 주유 상태 : {self.oil}')
#
#
# class Hybrid(Car):
#     max_amount = 30
#
#     def __init__(self, oil=0, amount=0):
#         super().__init__(oil)
#         self.amount = amount
#         print('하이브리드 차량이 생산되었습니다.')
#
#     def charge(self, amount):
#         if amount <= 0:
#             return
#         if self.amount + amount > Hybrid.max_amount:
#             print(f'전기를 {Hybrid.max_amount - self.amount} 충전 했습니다.')
#             self.amount = Hybrid.max_amount
#         else:
#             print(f'전기를 {amount} 충전 했습니다.')
#             self.amount += amount
#
#     def hybrid_info(self):
#         super().car_info()
#         print(f'현재 충전 상태 : {self.amount}')
#
#
# car = Hybrid(0, 0)
# car.add_oil(100)
# car.charge(50)
# car.hybrid_info()

'''
지시사항 
1. 슈퍼클래스 Shape 정의
    - 생성자에 name을 인스턴스 변수로 설정
    - draw() 메서드 정의하여 self.name을 출력
2. Shape 클래스를 상속받는 서브 클래스 Circle을 정의
    - Cricle은 radius(반지름) 속성을 추가
    - 생성자에서 radius도 추가할 것
    - area() 메서드를 정의하여 원의 넓이를 계산하고 return
3. Shape 클래스 상속받는 서브 클래스 Rectangle 정의
    - Rectangle 은 width / height 속성을 추가
    - 생성자에서 width / height 추가할 것
    - area() 메서드 정의하여 사각형의 넓이를 계산하고 retunr 할 것. 
4. Circle과 Rectangle의 draw() 메서드를 오버라이딩 하여 각각의 넓이를 출력

circle = Circle('원1', 5)
circle.draw()
print(f'원의 넓이 : {circle.area()}')

rectangle = Rectangle('직사각형1', 10, 8)
rectangle.draw()
print(f'직사각형의 넓이: {rectangle.area()}')

실행 예
반지름이 5인 원1이 생성되었습니다.
이름이 원1인 원의 넓이는 ____ 입니다.
원의 넓이 : ____
너비가 10, 높이가 9인 직사각형1이 생성되었습니다.
이름이 직사각형1인 직사각형의 넓이는 ____ 입니다.
직사각형의 넓이 : ____
'''


class Shape:
    def __init__(self, name):
        self.name = name

    def draw(self):
        print(f'이름이 {self.name}인', end=' ')


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def draw(self):
        super().draw()
        print(f'원의 넓이는 {self.area()} 입니다.')


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def draw(self):
        super().draw()
        print(f'직사각형의 넓이는 {self.area()} 입니다.')


circle = Circle('원1', 5)
circle.draw()
print(f'원의 넓이 : {circle.area()}')

rectangle = Rectangle('직사각형1', 10, 8)
rectangle.draw()
print(f'직사각형의 넓이: {rectangle.area()}')
