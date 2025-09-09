numbers = []
positive_cnt = 0
negative_cnt = 0
zero_cnt = 0

number_of_times = int(input('몇 개의 숫자를 입력하시겠습니까? >>> '))
for i in range(number_of_times):
    ipt_num = int(input(f'{i + 1}번째 숫자를 입력하시오 >>> '))
    numbers.append(ipt_num)
    if ipt_num == 0:
        zero_cnt += 1
    elif ipt_num < 0:
        negative_cnt += 1
    else:
        positive_cnt += 1

print(f'양수 : {positive_cnt}개')
print(f'음수 : {negative_cnt}개')
print(f'0 : {zero_cnt}개')