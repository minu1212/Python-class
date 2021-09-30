"""
    str.format, 조건문
    Version : 1.0
    Created : 2021.09.16
    Updated : 2021.09.16
    Author  : M.W.CHO
"""

"""
    1. "이름을 입력하세요"를 출력하고 입력을 받는다.
    2. "주민번호 맨 뒷자리를 입력하세요"를 출력하고 입력을 받는다.
    3. 뒷자리가 1,6이면 "월" 2,7이면 "화", 3,8이면 "수"
        4,9면 "목", 5,0이면 "금"
    4. "***님의 접종일은 *요일입니다. 요일 지켜서 오세요"
"""

# 1-1. 이름을 입력받아 nam에 저장한다
nam = input("성함을 입력해주세요 : ")

# 2-1. 주민번호 끝자리를 입력받아 final_num에 저장한다.
final_num = input("주민번호 끝자리를 입력해 주세요 : ")

# 2-2. 입력을 잘 받았는지 출력해본다.(최종본에서는 주석처리)
print("이름 = {},뒷자리 = {}".format(nam,final_num))

#3. 월화수목금을 분류해서 str에 넣는다
#수학을 좋아하는 사람들의 로직
mod = int(final_num) % 5
if mod == 1:
    str = "월"


elif mod == 2:
    str = "화"
elif mod == 3:
    str = "수"
elif mod == 4:
    str = "목"
else:
    str = "금"

#수학을 좋아하지 않는 사람들의 로직
if final_num in ["1","6"]:
    str = "월"
if final_num in ["2","7"]:
    str = "화"
if final_num in ["3","8"]:
    str = "수"
if final_num in ["4","9"]:
    str = "목"
else:
    str = "금"

#4. 결과문장을 출력한다.
print("{}님의 접종일은 {}요일입니다. 요일 지켜서 오세요".format(nam,str))