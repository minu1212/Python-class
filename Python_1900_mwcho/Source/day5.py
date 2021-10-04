"""
    기타제어문
    Version : 1.0
    Created : 2021.09.23
    Updated : 2021.09.23
    Author  : M.W.CHO
"""

### 1. while 문
print("*"*40)
print("while statement")

i = 1
while i < 10:
    print(i)
    i = i + 1

### 2. for 문
print("*"*40)
print("for statement")
for i in range(1, 10):
     print(i)


### 3. break 문
print("*"*40)
print("break statement")

n = 1
while True:
    if n == 10:
        break
    print(n)
    n = n + 1

### 4. continue 문
print("*"*40)
print("continue statement - 1부터 9중에 3의 배수만 출력하지 않음")

n = 1
while True:
    if n == 10:
        break
    elif n % 3 == 0:
        n = n + 1
        continue
    print(n)
    n = n + 1

###5. list
print("*"*40)
print("list")

list_simple = [1,2,3]
list_bookjap = [[1,2,3],[4,5,6]]
list_thebookjap = [[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]]



print(list_simple)
print(list_simple[0])  #list_simple의 첫 번째 것
print(list_bookjap[1]) #lsit_boojap의 두 번째 것
print(list_bookjap[1][1]) #list-bookjap의 두번째 것의 두 번째 것
print(list_thebookjap)
print(list_thebookjap[0][1][2]) #음......
# print("list_simple") + list_simple # 불가, str과 list는 더해질 수 없음
print("lsit_simple : {}".format(list_simple))



