phone_num = input('전화번호를 입력하시오 >>> ')

if len(phone_num) == 13 and phone_num.count('-') == 2:
    print(f'전화의 중간 4자리는 {phone_num[4:8]}입니다')
else:
    print('유효하지 않은 전화번호 양식입니다.')