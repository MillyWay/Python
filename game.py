
dict_ice = {
    "name" : "수박바"
    "price": "500"
}
list_punch[0,1,2,3,4,5]

name = input("이름을 입력하시오: ")
print(name, "님 반갑습니다. {0}(HP 100)으로 게임을 시작 합니다.".format(name))
print("길을 가다가 퉁퉁이를 만났습니다.")
print("1.싸운다 2.도망간다")
num = int(input("선택: "))

if num == 1:
    print("퉁퉁이에게 흠씬 두들겨 맞았다...")
elif num == 2:
    print("도망가다 도랑에 빠져서 잡혔다!")
else:
    print("입력을 잘못해서 게임오버!")       