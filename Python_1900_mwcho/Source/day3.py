"""
    str.format, 조건문
    Version : 1.0
    Created : 2021.09.16
    Updated : 2021.09.16
    Author  : M.W.CHO
"""

### 1. print 하나 더 (str.format 알아보기)
print("{}은 도 하나의 {}함수 {}입니다.".format("이것","print","사용법"))
print("숫자도 되는지 해보죠 {}".format(10))
print("되네요 괄호보다 입력이 더 많을 때 {}".format("되네","이게 되나"))
# print("괄호보다 입력이 더 적을 때 {} {}".format(10)) # 괄호가 입력보다 많을 시 오류 발생

print("#"*10)
print("이름={name}\n주소={addr}".format(name="조민우",addr="미입력"))
print("#"*10)
print("이름:{0}\n주소:{1}".format("조민우",100))
print("이름:{1}\n주소:{0}".format("조민우",100))
print("#"*10)

### 조건문 -if
print("#*40")
print("조건문 if 연습")
print("#*40")

print("*** a = 1 ***")
a = 1
if a > 0:
    print("a는 양수")
if a == 1:
    print("a는 1임")
if not a != 1:
    print("a는 1이 아닌게 아님")

a = 100
if a > 0:
    print("a는 양수2")
    print("a는 양수3")

if a > 0: print("a는 양수4")
          # print("a는 양수5") #if문 중에 실행문을 넣으면 줄을 맞춰도 오류
if a > 0: print("a는 양수4"); print("a는 양수7") #코드를 한 줄로 만들고 싶을 경우


# if a = 2: #대입연산자는 결과가 bool 타입이 아님
#     print("a는 2입니다")

### 조건문 -if-else
print("#*40")
print("조건문 if-else 연습")
print("#*40")

b = -1
if b > 0:
    print("b는 양수")
else:
    print("b는 양수가 아님")

if b > 0:
    print("b는 양수")
else:
    print("b는 양수가 아님")
    print("b는 양수가 아님")

### 조건문 -if-elif
print("#*40")
print("조건문 if-elif 연습")
print("#*40")

c = 0
if c > 0:
    print("c는 양수")
elif c == 0: # 조건문 해석 - c > 0은 아니고 0과 같을때
    print("c는 0")

d = 60
if d > 50:
    print("d는 큰 양수")
elif d > 0:
    print("d는 그냥 양수")

### 조건문 -if-elif-else
print("#*40")
print("조건문 if-elif-else 연습")
print("#*40")

e = -30
if e > 0:
    print("e는 양수")
elif e == 0:
    print("e는 0")
else:
    print("e는 음수")