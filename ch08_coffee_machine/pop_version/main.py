MENU = {
    '에스프레소': {
        '재료': {
            '물': 50,
            '커피': 18,
        },
        '가격': 1.5,
    },
    '라떼': {
        '재료': {
            '물': 200,
            '커피': 24,
            '우유': 150,
        },
        '가격': 2.5,
    },
    '카푸치노': {
        '재료': {
            '물': 250,
            '커피': 24,
            '우유': 100,
        },
        '가격': 3.0,
    },
}

profit = 0
resources = {
    '물': 300,
    '우유': 200,
    '커피': 100,
}


def is_resource_enough(ingredient, order_ingredient):
    '''
    :param ingredient: 현재 가지고 있는 재료의 양
    :param order_ingredient: 확인해 볼 메뉴 의 재료
    :return: True or False
    '''
    common_keys = order_ingredient.keys() & ingredient.keys()
    for key in common_keys:
        if ingredient[key] < order_ingredient[key]:
            print(f'{key}이(가) 부족합니다.')
            return False
    return True


def process_coins():
    '''
    쿼터 = $0.25
    다임 = $0.10
    니켈 = $0.05
    페니 = $0.01
    '''
    sum = 0

    sum += float(input("쿼터 동전 갯수 : ")) * 0.25
    sum += float(input("다임 동전 갯수 : ")) * 0.10
    sum += float(input("니켈 동전 갯수 : ")) * 0.05
    sum += float(input("페니 동전 갯수 : ")) * 0.01

    return sum


def is_transaction_successful(money_received, drink_cost):
    """
    money_received 가 dirink_cost보다 크면 True 반환
    :param money_received:
    :param drink_cost:
    :return:
    """
    global profit
    change = money_received - drink_cost
    if change >= 0:
        profit += drink_cost
        print(f'잔돈 ${change}을(를) 반환합니다.')
        return True
    else:
        print(f'금액이 충분하지 않습니다. ${change}을(를) 반환합니다.')
        return False


# TODO - 1 : 커피머신이 반복적으로 돌아가야하는데, off를 입력 받으면 종류가 이루어져야합니다.
is_on = True
while is_on:
    choice = input('어떤 음료를 드시겠습니까? (에스프레소 / 라떼 / 카푸치노) >>> ')
    print(choice.lower())
    # TODO - 2 : off 확인 후 코드 작성
    # TODO - 3 : 사용자가 "report"를 입력하면 현재 자원 값을 보여주는 보고서를 생성
    # TODO - 4 : choice == 에스프레소 / 라떼 / 카푸치노 중 하나일 때 작성하는 부분
    # TODO - 5 : choice가 이상의 조건을 충족하지 않으 때 '잘봇 입력하셨습니다. 다시 입력하세요'를 출력하는 부분
    if choice.lower() in 'off':
        is_on = False
        print('자판기가 종료되었습니다.')
    elif choice.lower() in 'report':
        for resource in resources:
            print(f'{resource} : {resources[resource]}')
    elif choice in MENU:
        if is_resource_enough(resources, MENU[choice]['재료']):
            credit = process_coins()
            if is_transaction_successful(money_received=credit, drink_cost=MENU[choice]['가격']):
                for key in MENU[choice]['재료']:
                    resources[key] -= MENU[choice]['재료'][key]
                print(f'{choice}가 나왔습니다, 맛있게 드세요.')
    else:
        print('잘못 입력 하셨습니다. 다시 입력하세요.')
