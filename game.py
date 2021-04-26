
dict_ice = {
    "babamba" : "바밤바"
}



list_punch = [0,1,2,3,4,5]

name = input("이름을 입력하시오: ")
print(name, "님 반갑습니다. {0}(HP 100)으로 게임을 시작 합니다.".format(name))
print("길을 가다가 퉁퉁이를 만났습니다.")
print("퉁퉁이: 야 너 잘 만났다 몇대 맞을래?")
print(min(list_punch),"대에서",max(list_punch),"대까지만 골라봐")
num = int(input("선택: "))

if num == 0:
    print(list_punch[0],"대? 장난하나...(퉁퉁이가 단단히 화났다!)")

elif num == 1:
    print(list_punch[1],"대? 그래 그럼 쎄게 한 대")

elif num == 2:
    print(list_punch[2],"대 가지고 되겠냐..")

else :
    print("됐고, 저 가게 가서",dict_ice["babamba"],"있는지 확인해봐")
    icecream = dict_ice.get("babamba") 
    if icecream == "바밤바": 
        print("퉁퉁이에게 가서 있다고 말해주자...") 
    else:    
        print("퉁퉁이에게 가서 없다고 말해주자...")