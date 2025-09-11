"""
ch11_exeption
main

1. 예외 처리의 필요성
"""
from typing import get_args

from prettytable import PrettyTable, TableStyle

exceptions = [
    (1, 'BaseException', '최상위 예외 클래스'),
    (2, 'Exception', '대부분 예외 클래스의 슈퍼 클래스'),
    (3, 'ArithmeticError', '산술 연산에 문제가 있을 때'),
    (4, 'AttributeError', '잘못된 속성을 참조할 때'),
    (5, 'EOFError', '파일에서 더 이상 읽어 들일 데이터가 없을 때'),
    (6, 'ModuleNotFoundError', 'import할 모듈이 없을 때'),
    (7, 'FileNotFoundError', '존재하지 않는 파일일 때'),
    (8, 'IndexError', '잘못된 인덱스를 사용할 때'),
    (9, 'NameError', '잘못된 이름(변수)을 사용할 때'),
    (10, 'SyntaxError', '문법이 틀렸을 때'),
    (11, 'TypeError', '계산하려는 데이터의 유형이 잘못되었을 때'),
    (12, 'ValueError', '계산하려는 데이터의 값이 잘못되었을 때'),
]

pt = PrettyTable()
pt.field_names = ['순번', '예외 클래스', '의미']
pt.add_rows(exceptions)
# print(pt)


# try:
#     a = int(input('나누는 수(제수)를 입력하세요. >> '))  # 0 입력
#     b = int(input('나눠지는 수(피제수)를 입력하세요. >> '))
#     print(f'b/a = {b/a}')
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print(f'b / a = {b/a}')
# finally:
#     print('프로그램이 종료되었습니다.')


# age = int(input('나이를 입력하세요 >>>'))
# print(f'당신의 나이는 {age}살 입니다.')

# try:
#     age = int(input('나이를 입력하세요 >>>'))
#     raise Exception('강제로 발생시킨 예외입니다.')
# except Exception as e:
#     print('발생한 예외 메시지는 다음과 같습니다.')
#     print(e)
'''
raise로 강제로 예외 발생시키기 때문에 예외 처리로 넘어가게 된다.
이러한 방식을 사용하여 특정 조건일 때 예외로 넘기는 추가코드가 필요하다는 것을 할 수 있다.
'''
# class NegativeAgeError(Exception):
#     pass
# # Exception 클래스를 상속 받았으면 슈퍼 클래스의 속성 / 메서드를 사용 할 수 있다.
# class TooManyAgeError(Exception):
#     pass


# try:
#     age = int(input('나이를 입력하세요 >>>'))
#     if age < 0:
#         raise NegativeAgeError('나이는 음수일 수 없습니다.')
#     if age > 200:
#         raise TooManyAgeError('나이가 너무 많습니다.')
# except NegativeAgeError as e:
#     print(e)
# except TooManyAgeError as e:
#     print(e)
# else:
#     print(f'당신의 나이는 {age}살 입니다.')
# finally:
#     print('프로그램 종료되었습니다.')

'''
과제 :
사용자의 점수를 0 이상 100 이하로 입력받아서 점수가 80점 이상이면 합격, 아니면 불합격을
출력하는 프로그램 작성하는데, 0 이 100 이하의 유효한 값이 아니라면 예외를 발생 시키고
'점수는 0 이상 100이하입니다.'라ㅏ는 예외 메시지를 출력하시오 
ScoreOutOfRangeError 클래스를 정의해서 사용

입력 받는데 예를 들어 백점이라고 입력하면 '점수는 숫자로 입력해야 합니다.'라는 메시지를 출력
실수로 입력하면 '정수로 입력해야합니다.'라는 메시지를 출력

예상할 수 없는 예외가 발생 시 Exception을 적용하여 디폴트 에러 메시지 출력

프로그램이 종료 되었다는 메시지를 맨 마지막에 작성

'''


class ScoreOutOfRangeError(Exception):
    pass


def check_float(s):
    if '.' in s:
        try:
            float(s)
            return True
        except ValueError:
            return False
        except TypeError:
            return False
    else:
        return False


# try:
#     inp = input('점수를 입력하세요 >>> ')
#     if check_float(inp):
#         raise TypeError('정수로 입력해야합니다.')
#     score = int(inp)
#     if score < 0 or score > 100:
#         raise ScoreOutOfRangeError('점수는 0 이상 100이하입니다.')
# except ScoreOutOfRangeError as e:
#     print(e)
# except ValueError as e:
#     print('점수는 숫자로 입력해야 합니다.')
# except TypeError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     if score >= 80:
#         print('합격입니다.')
#     else:
#         print('불합격입니다.')
# finally:
#     print('프로그램이 종료되었습니다.')

'''
지시사항
1. 사용자로부터 숫자 입력
2. 입력 받은 숫자로 100을 나누어 결과를 출력
3. 입력 값이 0일 경우 적절한 예외처리하여 '0으로 나눌 수 없습니다.' 메시지 출력
4. 입력 값이 숫자가 아닌경우 적절한 예외를 처리 '숫자만 입력 할 수 있습니다.' 출력
5. 예외가 발생하지 않는 경우 '정상적으로 처리되었습니다.' 라는 메시지를 출력하고 결과도 출력
6. 프로그램 종료 메시지를 출력한다.
'''

# try:
#     inp_int = int(input('숫자를 입력해 주세요 >>> '))
#     print( f'100 / {inp_int} = {100 // inp_int}')
# except ZeroDivisionError as e:
#     print('0으로 나눌 수 없습니다.')
# except ValueError as e:
#     print('숫자만 입력 할 수 있습니다.')
# except TypeError as e:
#     print('숫자만 입력 할 수 있습니다.')
# except Exception as e:
#     print(e)
# else:
#     print('정상적으로 처리되었습니다.')
# finally:
#     print('프로그램이 종료되었습니다.')


'''
지시 사항
1. 미리 정의된 리스트
2. 사용자로부터 리스트의 인덱스를 입력
3. 입력받은 인덱스를 사용하여 리스트의 값을 출력
4, 인덱스가 리스트의 범위를 벗어나면 적절한 메시지를 출력
5. 사람을 의심하고 예상되는 예외를 적용
6. 예외가 발생하지 않는 경우 "정상적으로 처리되었습니다." 메시지 출력
7. 프로그램 종료 메시지를 출력
8. 마이너스 인덱스는 적용시키지 않는다. -> 사용자 정의 예외 클래스를 통해서 적용
    -> NegativeNumIndexError
'''


# class NegativeNumIndexError(Exception):
#     pass
#
#
# my_list = [10, 20, 30, 40, 50]
#
# try:
#     inp_idx = int(input("인덱스를 숫자를 선택해 주세요 >>> "))
#     if inp_idx < 0 :
#         raise NegativeNumIndexError("마이너스는 입력이 안됩니다.")
#     print(my_list[inp_idx])
# except NegativeNumIndexError as e:
#     print(e)
# except ValueError as e:
#     print("숫자 정수를 입력해 주세요.")
# except IndexError as e:
#     print("인덱스 범위가 아닙니다.")
# except Exception as e:
#     print("사람 아니야...")
#     print(e)
# else:
#     print('정상적으로 처리되었습니다.')
# finally:
#     print('프로그램이 종료되었습니다.')

'''
지시사랑
1. 미리 정의된 클래스 와 속성
2. 사용자로부터 속성명을 입력받는다.
3. 입력받은 '속성명'을 사용하여 객체의 '속성값'을 출력한다.
4. 잘못된 속성명을 입력하면 '존재하지 않는 속성입니다.'라는 메시지를 출력한다.
5. 예외가 발생하지 않은 경우 '정상적으로 처리되었습니다.'라는 메시지와 속성값을 출력한다.
6. 프로그램 종료 메시지를 출력한다.
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person(name ='김일', age = 21)
print(getattr(person1, 'age'))
# getattr()의 두 번째 argument는 인스턴스 변수명을 받습니다. -> 그 데이터를 str로 받는다.
print(getattr(person1, 'name'))
print(vars(person1))                    # 속성명과 속성값을 딕셔너리로 반환

try:
    attr = input("속성명을 입력해 주세요. >>> ")
    print(getattr(person1, attr))
except AttributeError:
    print('존재하지 않는 속성입니다.')
except NameError:
    print('존재하지 않는 속성입니다.')
else:
    print('정상적으로 처리되었습니다.')
finally:
    print('프로그램이 종료되었습니다.')