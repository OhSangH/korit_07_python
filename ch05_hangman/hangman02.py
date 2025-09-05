import random

word_list = ['apple', 'banana', 'camel']
chosen_word = random.choice(word_list)
print(chosen_word)

#todo - 1 : 비어있는 list인 display를 만드시오.
display = []
# print(display)
# display.append('김')
# print(display)
# display.append(1)
# print(display)
# display[1] = 2
# print(display)
#todo - 2: 이상의 코드라인을 참조하여 chosen_word의 각 문자 개수 마다 '_'를 추가하시오. 예를 들어 chosen_word == 'apple'이라면 display = [ '_', '_', '_', '_', '_' ]이 되어야 합니다. 즉, chosen_word의 문자 개수 만큼 '_'가 있어야 합니다.
for _ in range(len(chosen_word)):
    display.append('_')
    # 반복실행문에서 변수 i가 쓰이지 않아서 그냥 반복횟수가 len(chosen_word)만큼이라는 것을 알 수 있습니다. 그 경우에는 i와 같은 특정 변수를 쓰기보다는 _ 를 써서 반복횟수만 통제한다고 표시해주는 편입니다.

#todo - 3 : chosen_word의 각 문자들을 반복시키시오. 만약 그 위치의 문자가 guess와 일치하면, 해당 위치의 display에서 문자를 공개하시오. 예를 들어, 사용자가 'p'를 입력했고, chosen_word가 apple이라면 display = [ '_', 'p', 'p', '_', '_' ] 로 바뀌어야 합니다.

guess = input('알파벳을 입력하세요 >>> ').lower()
for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
        display[i] = guess          # guess라는 데이터를 display의 인덱스넘버 i인 위치에 재대입

print(display) # hangman03