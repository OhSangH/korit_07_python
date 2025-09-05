'''
python 대표 collection 종류
1. list 리스트 : 추가 / 수정 / 삭제가 언제나 가능 / 순서 있음
2. tuple 튜플 : 추가 / 수정 / 삭제가 불가능 / 순서 있음
3. set 세트 : 중복된 값의 저장이 불가능 / 순서 없음
4. dict 딕셔너리 : 키 + 값으로 관리
'''
# list_example = [30, 40, '김이', [100, '김삼']]
# tuple_example = (10, 20, 30, '김사')
# set_example = {100, 200, 300, 400, '김오'}
# dictionary_example = { '이름': '김일', '나이': 20, '학교': '코리아아이티'}
#
# print(list_example)
# print(tuple_example)
# print(set_example)
# print(dictionary_example)

# list
# li1 = 'hello'
# print(li1[1])
# print(li1[2])
# print(li1[3])
# print(li1[-1])
# print(li1[-2])
# print(li1[-3])
# print(li1[-4])
#
# li2 = [100, 3.14, 'hello']
# li3 = list([4, 5, 6, 7, 8, 9, 0])
# print(li3[0:4:2])
#
# scores = [30,40,50]
# print(scores)
# scores.append(100)
# print(scores)
# scores.insert(0,90)
# print(scores)
# scores.pop()
# print(scores)
# scores.remove(90)
# print(scores)

# li4 = []
# for i in range(10):
#     li4.append(i + 1)
# print(li4)
#
# for i in range(10):
#     li4[i] *= 2
# print(li4)
#
# li4.sort(reverse=True)
# for li in li4:
#     li4[li4.index(li)] *= 2
# li4.sort()
# print(li4)

# # tuple
# tu1 = (1, 2, 3)
# tu2 = tuple((4, 5, 6))
# tu3 = 7, 8, 9
# print(tu1, tu2, tu3)
#
# tu4 = (0)
# print(type(tu4))
#
# tu5 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# print(type(tu5))
#
# tu6 = 'hello.', 'good morning.', 'my name is', 'kim-il', 'i am', '20 ', 'years old.'
# for word in tu6:
#     print(word.title(), end=' ')
#
# print()
# print(tu6)
#
# # set
# set1 = {1, 2, 3}
# set2 = set({1, 2, 3})
# print(set1)
# print(set2)
#
# li = []
# tu = ()
# se = {}
# print(type(li))
# print(type(tu))
# print(type(se))
#
# se2 = set({})
# print(type(se2))
#
# se3 = {10, 20, 30}
# se3.add(50)
# print(se3)
# se3.remove(30)
# print(se3)
#
# se3.discard(70)
# print(se3)

## dictionary
# dict1 = {
#     '이름': '김일',
#     '나이': 20,
#     '주소': ['서울특별시', '마포구', '목동'],
# }
# dict2 = dict({})
#
# li01 = [10, 20, 30, 40]
# for num in li01:
#     print(num)
#
# for key in dict1:
#     print(key)
#     print(dict1[key])
#
# print(dict1.keys())
# print(type(dict1.keys()))
#
# print(dict1.values())
# print(type(dict1.values()))
#
# dict1['직업'] = '웹 퍼블리셔'
# print(dict1)
# dict1['직업'] = '웹 개발자'
# print(dict1)
#
# li001 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# li002 = li001[2 : 7]
# li003 = li002[1]
# print(li001)
# print(li002)
# print(li003)
'''
1~12 월까지 입력받아 몇일 까지 있는지 출력
실행 예 
1 ~ 12 사이의 월을 입력하세요 >>> 2
2월은 28일 까지입니다.
'''
# month_date = {
#     '1': 31,
#     '2': 28,
#     '3': 31,
#     '4': 30,
#     '5': 31,
#     '6': 30,
#     '7': 31,
#     '8': 31,
#     '9': 30,
#     '10': 31,
#     '11': 30,
#     '12': 31,
# }
# input_month = input("1 ~ 12 사이의 월을 입력하세요 >>> ")
# print(f'{input_month}월은 {month_date[input_month]}일 까지입니다.')
#
# month_31date = [1,3,5,7,8,10,12]
# date = [30,31,28]
# int_input_month = int(input("1 ~ 12 사이의 월을 입력하세요 >>> "))
# if input_month in month_31date:
#     print(f'{int_input_month}월은 {date[1]}일 까지입니다.')
# elif input_month == 2:
#     print(f'{int_input_month}월은 {date[2]}일 까지입니다.')
# else:
#     print(f'{int_input_month}월은 {date[0]}일 까지입니다.')


'''
수학 여행을 어디로 갈 지 결정하기 위해 학생들이 희망하는 모든 수학여행 장소를 조사하기로 했습니다.
학생들이 원하는 장소를 입력 받아 동일한 입력을 무시하고 모든 입력을 저장하려고 합니다.
학생들 3명으로 가정하고 실행 예와 같이 동작하는 프로그램을 작성하시오

실행 예
희망하는 수학여행지를 입력하세요 >>> 제주
희망하는 수학여행지를 입력하세요 >>> 제주
희망하는 수학여행지를 입력하세요 >>> 민속촌

조사된 수학여행지는 {'제주', '민속촌'}입니다.
조사된 수학여행지는 ['제주', '민속촌']입니다.
'''
#
# location_set = set({})
# location_list = []
# cnt = 3
# for i in range(cnt):
#     location_set.add(input('희망하는 수학여행지를 입력하세요 >>> '))
#
# location_list = list(location_set)
# print(f'조사된 수학여행지는 {location_set}입니다.')
# print(f'조사된 수학여행지는 {location_list}입니다.')
#

'''
사용자로부터 임의의 양의 정수를 입력받고, 그 정수만큼 숫자를 입력 받아 list에 저장
이 후 저장된 숫자 중 짝수만 새로운 lost에 저장하여 출력하는 프로그램 작성 하세요

실행 예
몇 개의 숫자를 입력할까요? >>> 5
1번째 숫자를 입력하세요 >>> 10
2번째 숫자를 입력하세요 >>> 15
3번째 숫자를 입력하세요 >>> 20
4번째 숫자를 입력하세요 >>> 25
5번째 숫자를 입력하세요 >>> 30
입력 받은 숫자는 [10, 15, 20 ,25, 30]
입력 받은 숫자 중 짝수는 [10, 20 , 30] 입니다.
'''
# cnt = int(input('몇 개의 숫자를 입력할까요? >>> '))
# num_li = []
# even_li = []
# for i in range(cnt):
#     num_li.append(int(input(f'{i+1}번째 숫자를 입력하세요 >>> ')))
#     if num_li[i] % 2 == 0:
#         even_li.append(num_li[i])
# print(f'입력 받은 숫자는 {num_li}입니다.')
# print(f'입력 받은 숫자 중 짝수는 {even_li}입니다.')

'''
3명의 이름과 전화번호를 받아 딕셔너리에 저장 후 입력한 정보를 추출

실행 예
1 번째 사람의 이름을 입력하세요 >>> 김일
1 번째 사람의 연락처를 입력하세요 >>> 010-1234-5678
2 번째 사람의 이름을 입력하세요 >>> 김이
2 번째 사람의 연락처를 입력하세요 >>> 010-2345-6789
3 번째 사람의 이름을 입력하세요 >>> 김삼
3 번째 사람의 연락처를 입력하세요 >>> 010-3456-7890

입력 받은 연락처는 {'김일':'010-1234-5678', '김이': '010-2345-6789', '김삼' : '010-3456-7890'}입니다.
'''
# cnt = 3
# person_dict = {}
# for i in range(cnt):
#     name = input(f'{i + 1}번째 사람의 이름을 입력하세요 >>> ')
#     phone_number = input(f'{i + 1}번째 사람의 연락처를 입력하세요 >>> ')
#     person_dict[name] = phone_number
#
# print()
# print(f'입력 받은 연락처는 {person_dict}입니다.')

'''
숫자를 입력한 횟수만큼 비어있는 list에 숫자 추가하기
문제 : 비어있는 numbers1을 선언하고, 그 안에 입력 받은 횟수 만큼 숫자를 추가하시오

함수정의 : add_numbers()
매개변수 : 정수 n
add_numberts1(last_num)
print(add_numbers2(last_num))
'''

#
# def add_numbers1(num):
#     print(add_numbers2(num))
#
# def add_numbers2(num):
#     li = []
#     for i in range(num):
#         li.append(i + 1)
#     return li
#
# last_num = int(input(('숫자를 몇 까지 입력하시겠습니까? >>> ')))
# add_numbers1(last_num)
# print(add_numbers2(last_num))
#
# hello = ['안','녕','하','세','요']
# def add_numbers3(num , list_hello):
#     li = []
#     for i in range(num):
#         li.append(i + 1)
#     li.extend(list_hello)
#     print(li)
#
# add_numbers3(last_num, hello)
#
# def add_numbers4(num , list_hello):
#     for i in range(num):
#         list_hello.insert(i, i + 1)
#     print(list_hello)
#
# add_numbers4(last_num, hello)

'''
짝수와 홀수의 개수 세기

함수이름 : count_even_odd
매개변수 : list numbers(요소는 모두 정수 일 것)

실행 예
count_even_odd([1,2,3,4,5,6,7,8,9,10])
짝수의 개수 : 5개
홀수의 개수 : 5개
'''


def count_even_odd(nums):
    cnt_odd = 0
    for n in nums:
        if n % 2 == 1:
            cnt_odd += 1
    print(f'짝수의 개수 : {len(nums) - cnt_odd}개')
    print(f'홀수의 개수 : {cnt_odd}개')


count_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
