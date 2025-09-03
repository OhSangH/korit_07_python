str_example = 'hello, python!'
print(str_example[0])
print(str_example[1])
print(str_example[2])
print(str_example[3])
print(str_example[4])
print(str_example[5])
print(str_example[6])
print(str_example[7])

for alphabet in str_example:
    print(alphabet, end=' ')

print(str_example[-1])
str_slicing = str_example[3: 10: 1]
print(str_slicing)

for i in range(0,10,1):
    print(i, end=' ')


for s in str_example:
    print(s, end=' ')

print()
num = input('네 자리 숫자를 입력하세요 >>> ')
print(f'맨 마지막 숫자는 {num[-1]}입니다.')
if int(num[-1]) % 2 == 0:
    print(f'맨 마지막 숫자는 {num[-1]}이며, 짝수입니다.')
else:
    print(f'맨 마지막 숫자는 {num[-1]}이며, 홀수입니다.')
