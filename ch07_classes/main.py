class WaffleMachine:
    pass
class Person:
    def set_info(self,name,age,tel,address):
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address

    def show_info(self):
        print(f' 이름 : {self.name}')
        print(f' 나이 : {self.age}')
        print(f' 연락처 : {self.tel}')
        print(f' 주소 : {self.address}')

    def show_info2(self):
        return (f'제 이름은 {self.name}이고, {self.age}살 입니다.\n'
                f'연락처는 {self.tel}인데, {self.address}에 살고 있습니다.')


waffle = WaffleMachine()
print(waffle)

person01 = Person()
person01.set_info('김일', 20, '010-1234-5678', '서울 특별시 마포구')
person01.show_info()

person02 = Person()
person02.set_info('오상현', 26, '010-****-****', '부산')
print(person02.show_info2())

