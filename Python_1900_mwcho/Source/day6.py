import colors
"""
   color Expression
    Version : 1.0
    Created : 2021.09.28
    Updated : 2021.09.28
    Author  : M.W.CHO
"""

BLACK = '\033[90m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'

RED_BG = '\033[101m'
GREEN_BG = '\033[102m'

END = '\033[0m'

#1. 8색 적용해보기
print("*"*40)
print("8 color statement")

str1 = colors.YELLOW + "노란색" + colors.END
str2 = colors.CYAN + "하늘색" + colors.END
str3 = colors.RED_BG + "빨간바탕" + colors.END
str4 = colors.BLACK + colors.GREEN_BG + "녹색바탕에 검정색 글씨" + colors.END

print(str1)
print(str2)
print(str3)
print(str4)

#2. 256색 적용해보기
print("*"*40)
print("256 color statement")

DEEPSKYBLUE2 = '\033[38;5;38m'
str5 = DEEPSKYBLUE2 + "딥스카이블루" + colors.END
print(str5)

str6 = ""
for i in range(1,100):
    str6 = str6 + '\033[48;5;{}m'.format(i) +' '
str6 = str6 + colors.END

print(str6)

#3. True Color색 적용해보기
print("*"*40)
print("True color statement")

str_list = ["","","",""]
for i in range(0,256):
    # str_list[0] = str_list[0] + ' \033[48;2;{};0;0m'.format(i) + ' '
    # += 을 사용하면 기존에 갖고있던 값을 포함하여 대입
    str_list[0] += ' \033[48;2;{};0;0m'.format(i) + ' '
    str_list[1] += ' \033[48;2;0;{};0m'.format(i) + ' '
    str_list[2] += ' \033[48;2;0;0;{}m'.format(i) + ' '
    str_list[3] += ' \033[48;2;{};{};{}m'.format(i,i,i) + ' '

for i in range(0,4):
    str_list[i]  += colors.END
    print(str_list[i])

print(colors.CNAME)
colors = 256
print(colors)