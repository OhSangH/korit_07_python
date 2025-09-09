candidates = []
num_of_candidates = int(input('후보자 수를 입력하시오 >>> '))
for i in range(num_of_candidates):
    candidates_name = input(f'{i + 1}번째 후보자의 이름을 입력하시오 >>> ')
    candidates.append(candidates_name)

votes = dict(zip(candidates, [0]*len(candidates)))
num_of_loop = int(input('전체 투표 횟수를 입력하시오 >>> '))
name_list = ''
for i in range(len(candidates)):
    if i == len(candidates) - 1:
        name_list += f'{i + 1}: {candidates[i]}'
    else:
        name_list += f'{i + 1}: {candidates[i]}, '

for i in range(num_of_loop):
    candidates_num = int(input(f'{i + 1}번째 투표 ({name_list}) >>>'))

    votes[candidates[candidates_num-1]] += 1
print('--- 투표 결과 ---')
for key, value in votes.items():
    print(f'{key}: {value}')