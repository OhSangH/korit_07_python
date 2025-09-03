print("Hello, Python! ❤️!")

# 주석 처리 방법

print(1)  # 숫자 자료형
print('1')  # 문자열 자료형

print(1 + 2)  # 결과값 : 3
print('1' + '2')  # 결과값 : 12

print(type(1))  # 결과값 :<class 'int'>
print(type('1'))  # 결과값 :<class 'str'>
print(type(1.0))  # 결과값 :<class 'float'>

print('python 수업을 시작했습니다. 파이팅')
print('''
이렇게 다중으로 쓰고 싶을 때에는 \'\'\'\'\'\'으로
작성하는 방법도 있습니다.
''')

# 변수 선언 및 초기화
# 변수명 = 데이터
name = '김일'
age = 20

print('안녕하세요 제 이름은 ' + name + '입니다. 나이는 ' + str(age) + '살입니다.')
# fstring
print(f'안녕하세요 제 이름은 {name}입니다. 나이는 {age}살입니다.')

'''
자바에서의 Scanner 기능 -> input()

1. 지금 입은 하의 색깔을 물어보는 input 함수를 작성하고 pants_color라는 변수에 젖아합니다
2. 마지막으로 먹은 음식을 물어보는 input 함수를 작성하고 last_food라는 변수에 저장
3. f-string을 활용하여 콘솔창에 다음과 같이 출력 될 수 있도록 작성합니다.

'''
