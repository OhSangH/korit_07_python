# age = 21
# if age >20:
#     print('성인입니다.')
# elif age <= 20 and age >13 :
#     print("청소년입니다.")
# else:
#     print("미성년자 입니다.")

# age1 = input('나이를 입력하세요 >>> ')
# print(age1)
# print(age1 + '10')
# print(type(age1))
#
# age2 = int(age1)
# print(age2 + 10)
# print(type(age2))

# age = int(input('당신의 나이를 입력하세요 >>> '))
# print(f"당신의 나이는 {age}살이고, 내년에는 {age + 1}살이 됩니다.")
# if age >19:
#     print('성인입니다.')
# elif age <= 19 and age >14:
#     print("청소년입니다.")
# elif age <= 14 and age >5:
#     print("어린이입니다.")
# else:
#     print("유아입니다.")

# 중첩 if
age = 21
has_ticket =False # boolean 자료형은 True False가 대문자로 시작
# print(type(has_ticket)) #결과값 : <class 'bool'>
if age >= 19:
    if has_ticket:
        print('영화관 입장이 가능합니다.')
    else:
        print('티켓을 구매하세요')
else:
    print('미성년자는 출입할 수 없습니다.')

age = float(age)
print(age)
