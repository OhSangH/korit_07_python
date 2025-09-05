import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
'''
이상의 코드라인을 확인하면 내부의 element가 복수의 라인으로 이루어진 str인 list라고 할 수 있습니다.
'''
#todo - 1 : 남은 기회 숫자를 추적하기 위한 lives 변수를 선언하고 6으로 초기화하세요.
lives = 6       # stages의 index number 역할을 하게 될 겁니다.
#todo - 2 : hangman03을 참조하여 while 반복문 바깥을 완성하시오.
word_list = [ 'apple', 'banana', 'camel' ]
chosen_word = random.choice(word_list)
print(chosen_word)
display = []
for _ in range(len(chosen_word)):
    display.append('_')
print(display)
#todo - 3 : while문의 조건을 수정하여 6 번의 기회가 소진되면 반복문이 종료될 수 있도록 작성하시오.
end_of_game = False
while not end_of_game:      # 어느 시점에 end_of_game = True
    print(stages[lives])
    guess = input('알파벳을 입력하세요 >>> ').lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess: # 선택된 단어의 알파벳이 일치할 때
            display[i] = guess
        # else:                       # 틀렸을 때는 else고, display에는 변동 없음
        #     lives -= 1
        #     if lives == 0:
        #         print('모든 기회를 잃었습니다.')
        #         print(stages[lives])
        #         end_of_game = True
        # 라고 작성하시면 안됩니다. 반복문 내부에서 guess가 일치하는지 여부를 따지는 중입니다. 예를 들어 chosen_word가 apple이고, guess가 a라고 가정했을 때, 첫 번째 반복에서는 display의 0번지가 a로 바뀝니다. 그런데 반복문 내부에 위치해 있기 때문에 1, 2, 3, 4번지에 대해서도 a가 display의 인덱스와 인치하는 element인지를 확인하게 됩니다. 그 결과 p p l e가 a와 다르기 때문에 lives -= 1 이 4 번 적용되어서 맞는 답을 입력했음에도 불구하고 행맨이 완성되는 것을 확인할 수 있게 됩니다.

    # 우리는 이상을 이유로 for 반복문의 바깥에서 guess가 chosen_word에 속하지 않는지를 확인하는 조건문을 '별개로' 작성해야만 합니다.

    # 틀렸을 때 lives를 1씩 감하고 0이 되었을 때 game over 시키는 부분
    if guess not in chosen_word:
        lives -= 1
        print(f'당신의 기회는 {lives} 번 남았습니다.')
        if lives == 0:
            print('모든 기회를 잃었습니다.')
            end_of_game = True
            print(stages[lives])
            print(f'정답은 {chosen_word}입니다.')

    if '_' not in display:
        print('정답입니다 !! 💌')
        end_of_game = True # 이 시점에 end_of_game이 True가 되었으므로 다음 반복문이 실행되지 않음 -> 105번 코드라인이 실행된다는 것을 의미합니다.
        # break              # 바로 반복문 정지 -> 105 번 코드라인이 실행 x
        print(f'정답은 {chosen_word}입니다.')

    # 현재 상황이 콘솔창에 출력돼서 user에게 안내가 가면 좋겠네요
    print(' '.join(display))
#todo - 4 : lives의 변수와 stages 리스트의 관계를 파악하여 guess를 입력할 때 마다 올바른 stages의 element가 출력될 수 있도록 작성하시오.

# 현재 기준에서 아까 완성판과 차이점 : logo 유무 / word_list가 부족함 / 혹시나 리팩토링 가능한지 여부
# hangman05 파일 생성 -> 필요한 부분들 다 복사 하고 주석들 좀 다 지워서 정리해놓겠습니다.
# logo를 text to ascii arts를 검색해서 하나 받아와서 맨 처음에 로고를 출력할 수 있도록 코드를 작성하겠습니다.









