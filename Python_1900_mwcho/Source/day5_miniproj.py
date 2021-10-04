"""
    Mini project
    Version : 1.0
    Created : 2021.09.23
    Updated : 2021.09.23
    Author  : M.W.CHO
"""
"""
    1. 보물상자에서 무기를 5종류 중 랜덤으로 하나를 획득한다.
    2. 길을 가다가 늑대, 산적, 드래곤  중 하나를 랜덤으로 만나다.
    3. 무기를 가지고 둘 중 하나의 에너지가 0이 될때까지 싸운다.
        사용자(user)는 공격, 회복 중 하나를 선택하며 상대는 공격만 합니다.
    4. 승리 또는 패배에 따라 메시지를 출력합니다.
"""
import random

# 1-1. 보물상자를 발견햇다는 메시지를 출력하고 사용자가 아무키를 누르기를 기다린다.
#       print,input 익히기
print("당신은 길을 가다가 [보물상자]를 발견했습니다.")
# input()


# 1-2. 보물상자에서 랜덤으로 1개 무기를 획득한다.  random 함수 및 리스트 활용법 익히기
#        각 무기는 [무기이름, 최소공격력, 최대공격]의 데이터를 가짐

weapons = [['휴지',1,3],['목검',3,5],['대검',5,10],['대포',1,50],['에픽벨붕검',50,100]]
# print(weapons[1])

sel = random.randint(0,4)
print("당신은 [{}]을(를) 획득하였습니다.".format(weapons[sel][0]))
my_weapon = weapons[sel]
print(my_weapon)

# 2-1. 길을 가다 랜덤으로 몬스터를 만난다. random 함수 및 리스트 활용법 익히기
#       각 몬스터는 [몬스터명, 최소공격력, 최대공격력]의 데이터를 가짐
mons = [['늑대',1,3],['산적',5,10],['드래곤',1,100]]
sel = random.randint(0,2)
print("당신은 길을 가다가 [{}]을(를) 만났습니다".format(mons[sel][0]))
my_mon = mons[sel]

# 3-1. 초기 양쪽의 에너지는 100이다. my_energy, mon_energy에 저장한다.
my_energy = 100
mon_energy = 100

# 3-2. 무한루프로 전투를 한다. 무한루프는 둘 중 하나의 에너지가 0이하가 되면 탈출한다.
#      > while, break 익히기
while True: #전투 무한루프
    # 3-3. 사용자는 공격 또는 회복을 선택한다. > input 익히기
    while True: #사용자 입력 무한루프
        user_input = input("행동을 선택하십시오. 1.공격 2.회복 : ")
        if user_input in ['1','2']:
            break
        else:
            print("잘못 선택하셨습니다.")

    # 3-4. 공격인 경우 최소, 최대 공격력 사이로 공격, 회복인 경우 0에서 30사이의 회복을 한다.
    #   > 조건문(if)
    if user_input == '1': #공격이면
        damage = random.randint(my_weapon[1],my_weapon[2]) #my_weaoib[1] : 최소공격력
        mon_energy = mon_energy - damage
        print("당신은 {}으로 {}의 데미지를 입혔습니다. {}의 체력 : {}".format(my_weapon[0],damage,my_mon[0],mon_energy))
        if mon_energy < 0:
            break

    elif user_input == '2': #회복이면
        heal = random.randint(0,30)
        my_energy = my_energy + heal
        print("당신은 회복으로 {}의 에너지가 회복되었습니다. 당신의 체력 : {}".format(heal,my_energy))

    # 3-5. 몬스터가 공격을 한다.
    damage = random.randint(my_mon[1],my_mon[2])
    my_energy = my_energy - damage
    print("당신은 {}의 공격으로 {}의 피해를 입었습니다. 당신의 체력 : {}".format(my_mon[0],damage,my_energy))
    if my_energy < 0:
        break


    # break

# 4-1. 승리 또는 패배에 따라 화면에 메시지를 출력한다.
if mon_energy < 0:
    print("{}이(가) 말했습니다. 강하군".format(my_mon[0]))
else:
    print("{}이(가) 말했습니다. 하하하 상대도 안되는군 ㅋㅋㅋ".format(my_mon[0]))

