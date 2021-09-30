"""
    Day4 5 minute challenge
    Version : 1.0
    Created : 2021.09.17
    Updated : 2021.09.17
    Author  : M.W.CHO
"""
"""
    1. " 이름을 입력하세요 : "를 출력하고 입력을 받는다.
    2. " 최대 숫자를 입력하세요 : "를 출력하고 입력을 받는다.
        입력받은 수 이내로 임의의 수를 생성한다.
    3. 입력한 숫자 범위로 숫자를 맞추는 게임을 만든다.
        게임은 "정답은 몇일까요? :"를 출력하고 숫자 입력을 받는다.
        임의의 수와 입력한 수가 동일할 때까지 계속한다.
        5번까지 못맞추면 종료한다.
    4. 한 번에 정답을 맞추면 "***님 대단하십니다"
        세 번 이내에 정답을 맞추면 "***님 우수한 성적이십니다"
        다섯 번까지 못 맞추면 "정답은 *입니다, 아쉽네요.
"""
# 1-1 이름을 입력받아 nam에 저장한다.
nam = input("이름을 입력하세요 : ")

# 2-1 최대숫자를 입력하세요를 입력받아 num에 저장한다.
# 2-2 숫자인지 파악하고 , 숫자가 아니면 숫자가아니라는 메시지를 출력하고 숫자가 들어올때까지 무한반복
while True:
    num = input("최대 숫자를 입력하세요 : ")
    if num.isdecimal() ==  True:
        print("입력하신 값은 {}입니다.".format(num))
        num = int(num)
        break
    else:
        print("입력하신 값은 숫자가 아닙니다.다시 입력해주세요")

# 2-3 입력받은 수 이내로 임의의 수(난수)를 생성한다.
import random
r_num = random.randint(1,num) #1부터 num의 int(정수) 하나를 생성
print(r_num)

# 3-1 입력을 5번까지 숫자 범위로 받는다.
# 3-2 숫자가 들어왔다면 r_num과 비교해 같다면 loop를 탈출한다.

corr = False # 정답여부 확인

for cnt in range(1,6):
    a_num = input("정답은 몇일까요? : ")
    if a_num.isdecimal() == True:
        if r_num == int(a_num):
            corr = True
            break
        print(a_num)
    else:
        print(a_num)
        # if a_num == r_num:
        #     print("축하합니다 정답을 맞추셨어요")
        #     break
        # else:
        #     print("입력하신 답은 정답이 아닙니다.")

# 4-1. 도전횟수에 따라 텍스트를 출력한다.
# print(cnt) #= 데이터 확인 용도
if cnt == 1:
    print("{}님 1회 만에 정답을 맞추셨군요!대단하네요.".format(nam))
elif cnt <= 3:
    print("{}님 2~3회 만에 정답을 맞추셨군요!우수한 성적이십니다.".format(nam))
elif cnt <= 5 and corr == True:
    print("{}님 4~5회 만에 정답을 맞추셨군요!더 노력하세야 겠어요.".format(nam))
else:
    print("정답은 {}입니다. 아쉽네요".format(r_num))


