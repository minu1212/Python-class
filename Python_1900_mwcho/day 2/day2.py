"""
    input, 연산자
    Version : 1.0
    Created : 2021.09.14
    Updated : 2021.09.14
    Author  : J.W.Lee
"""

# type() - 변수의 타입을 알려준다.
age = 10
name = "홍길동"
print(type(age))
print(type(name))
print(age, name)

# 더하기 빼기 연산자
print(type(10 + 5)) # int + int = int
print(type(10 + 3.2)) # int + float = float
print("Hi, " + "there") # str + str = str이 연결됨
# print("Hi, " + 100) # str + int => 오류
print("10 - 5 =", 10-5) # int - int = int
print("10 - 3.8 =", 10-3.8) # int - float = float
print("3.0 - 1.0 =", 3.0-1.0) # float - float = float
# print("Hi, there" - "there") # str - str => 오류

# 곱하기
print("10 * 2 =", 10*2) # int * int = int
print("10 * 3.1 =", 10*3.1) # int * float = float
print("1.1 * 1.2 =", 1.1*1.2) # float * float = float
print("*" * 40)
print("안녕"*5)
print("*" * 40)

# 나누기
print("10 / 5 =", 10/5) # int / int = float
print("10 / 2.0 =", 10/2.0) # int / float = float
print("1.4 / 2.9 =", 1.4/2.9) # float / float = float
# print("ddd" / 10) # str / int => 오류
# print("ddd" / "d") # str / str => 오류

# 입력받기 input()
# input()은 사용자가 입력한 값을 문자열로 받아온다.
name = input()
print("당신이 입력한 값은",name,"입니다")

# Day2 예제
# 파이썬, 자바, C 점수를 입력받아 평균을 출력하는 프로그램
score_p = input("파이썬 점수는? : ")
score_j = input("자바 점수는? : ")
score_c = input("C 점수는? : ")
#score_avg = (score_p + score_j + score_c) / 3 # input은 입력값을 문자열로 가져오기 때문에 오류
score_avg = (int(score_p) + int(score_j) + int(score_c)) / 3

print("*" * 40)
print(name,"성적표")
print("*" * 40)
print("평균점수 :", int(score_avg))

# 관계(비교)연산자
print(" 1 > 5 :", 1 > 5)
print(" 1 == 1 :", 1 == 1)
print(" 5 != 1 :", 5 != 1)
print(" 5 != 1 == True", 5 != 1 == True)

# 논리연산자
print("10 > 2 and 10 < 20 : ", 10 > 2 and 10 < 20)
print("10 != 0 or 10 >= 100 : ", 10 != 0 or 10 >= 100)
print("not 10 > 3 :", not 10 > 3)
print("not not 10 > 3 : ", not not 10 > 3)
# print("!(10 > 3) : ", !(10 > 3))

# int()
print("float() Test ", float(50))