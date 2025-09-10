# # class Korean:
# #     country = '한국'
# #     def __init__(self, name, age, address):
# #         self.name = name
# #         self.age = age
# #         self.address = address
# #     @classmethod
# #     def trip(cls, travelling_site):
# #         if cls.country == travelling_site :
# #             print('국내 여행중')
# #         else:
# #             print(f'{travelling_site}를 여행 중')
# #
# # man1 = Korean('김일', 21, '서울 특별시 종로구')
# # print(man1.name)
# # print(man1.age)
# # print(man1.address)
# #
# # print(man1.country)
# # Korean.country = '대한민국'
# # print(man1.country)
# # Korean.trip('대한민국')
# #
# # class Korean2:
# #     country = '한국'
# #
# #     @staticmethod
# #     def slogan():
# #         print('Imagine Your Korea! ')
# #
# #     @staticmethod
# #     def slogan2(str_ex):
# #         """매개변수가 있는 메서드입니다."""
# #         print('Imagine Your Korea! ' + str_ex)
# #
# #
# # Korean2.slogan()
# # Korean2.slogan2(' 근데 너무 덥다')
#
# '''
# 기본 예제
# 가방을 만들 때마다 현재 만들어진 가방이 몇 개인지 계산할 수 있는 Bag 클래스를 정의 할 겁니다.
# '''
#
# class Bag:
#     count = 0
#     def __init__(self):
#         Bag.count += 1
#         print('가방 객체가 생성되었습니다.')
#
#     @classmethod
#     def sell(cls):
#         print('가방이 팔렸습니다.')
#         cls.count -= 1
#
#     @classmethod
#     def remain_bag(cls):
#         return cls.count
#
#     def __del__(self):
#         Bag.count -= 1
#
# print(f'현재 가방 재고: {Bag.count}')
# print(f'현재 가방 재고: {Bag.remain_bag()}')
# bag1 = Bag()
# print(f'현재 가방 재고: {Bag.remain_bag()}')
# bag2 = Bag()
# bag3 = Bag()
# print(f'현재 가방 재고: {Bag.remain_bag()}')
# bag1.sell()
# print(f'현재 가방 재고: {Bag.remain_bag()}')
# del bag1
# print(f'현재 가방 재고: {Bag.remain_bag()}')
'''
정적 메서드 연습
'''
'''
응용예제
1. 다음 지시사항을 읽고 이름과 전체 인구수를 저장할 수있는 Person 클래스를 작성하시오

지시사항
1. 다음과 같은 방법으로 man과 woman 인스턴스를 생성하시오
man = Person('김일')
woman = Person('김이')

2. man 과 woman 인스턴스가 생성되면 다음과 같은 메시지를 출력할 수 있도록 작성하시오.
김일이(가) 태어났습니다.
김이이(가) 태어났습니다.

3. 다음 코드를 통해서 정체 인구수를 조회할 수 있도록 작성하시오.
print(f'전체 인구수 : {Person.get_population()})

4. 다음과 같은 명령어로 man 인스턴스를 삭제하시오.
del man

5. man 인스턴스가 삭제되면 다음과 같은 메시지를 출력할 수 있도록 소멸자를 정의하시오.
RIP 김일
'''
# class Person:
#     population = 0
#     def __init__(self, name):
#         self.name = name
#         Person.population += 1
#         print(f'{self.name}이(가) 태어났습니다.')
#
#     @staticmethod
#     def get_population():
#         return Person.population
#
#     def __del__(self):
#         print(f'RIP {self.name}')
#         Person.population -= 1
#
# man = Person('김일')
# woman = Person('김이')
# print(f'전체 인구수 : {Person.get_population()}')
# del man
# print(f'전체 인구수 : {Person.get_population()}')
'''
다음 지시 Shop 클래스 정의
지시 사항
1. Shop 클래스는 다음과 같은 변수를가지고 있다.
    total : 가게 전체 매출액
    menu_list : {매뉴명 : 가격}으로 이루어진 dictionary 요소를 가진 list
    
    menu_list = [{'떡볶이':3000},{'순대':4000},{'튀김':500},{'김밥':2000}]

2. 매출이 생기면 다음과 같은 방식으로 판매량을 작성합니다.
    Shop.sales('떡볶이',1) 
    Shop.sales('김밥',1) 
    Shop.sales('튀김',5) 
    
3. 모든 매출을 작성한 뒤 다음과 같은 방식으로 전체 매출액을 확인합니다.
print(f'매출 : {Shop.get_total()원'})
'''


class Shop:
    total = 0
    menu_list = [{'떡볶이': 3000, '라면' : 4000}, {'순대': 4000}, {'튀김': 500}, {'김밥': 2000}]

    @classmethod
    def sales(cls,name,num):
        for item in cls.menu_list:
            if name in item.keys():
                print(item.keys())
                cls.total += item[name] * num
                print(f'{name} {num}개 판매 !')

    @classmethod
    def get_total(cls):
        return cls.total

Shop.sales('떡볶이',1)
Shop.sales('김밥',1)
Shop.sales('튀김',5)
print(f'매출 : {Shop.get_total()}원')
