'''
python 대표 collection 종류
1. list 리스트 : 추가 / 수정 / 삭제가 언제나 가능 / 순서 있음
2. tuple 튜플 : 추가 / 수정 / 삭제가 불가능 / 순서 있음
3. set 세트 : 중복된 값의 저장이 불가능 / 순서 없음
4. dict 딕셔너리 : 키 + 값으로 관리
'''
list_example = [30, 40, '김이', [100, '김삼']]
tuple_example = (10, 20, 30, '김사')
set_example = {100, 200, 300, 400, '김오'}
dictionary_example = { '이름': '김일', '나이': 20, '학교': '코리아아이티'}

print(list_example)
print(tuple_example)
print(set_example)
print(dictionary_example)