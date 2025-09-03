dan = 1
while dan < 11:
    print(dan)
    dan += 1

# 10 ~ 1 까지 역순 출력
number = 10
while number > 0:
    print(number)
    number -= 1

dan = 1
number = 1
while dan < 10:
    while number < 10:
        print(f'{dan} X {number} = {dan * number}')
        number += 1
    dan += 1
    number = 1
