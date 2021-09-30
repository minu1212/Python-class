"""
    반복문
    Version : 1.0
    Created : 2021.09.17
    Updated : 2021.09.17
    Author  : M.W.CHO
"""

### 1.while 문
print("#"*40)
print("while statement")
print("#"*40)

print("노가다")
print("1번 출력")
print("2번 출력")
print("3번 출력")
print("4번 출력")
print("5번 출력")
print("6번 출력")
print("7번 출력")
print("8번 출력")
print("9번 출력")
print("10번 출력")
print("\n")


print("자동화")
i = 1
while i < 10:
    print("{}번 출력".format(i))
    i = i + 1


#infinite test
# while True:
#     print("무한 루프")

#무한입력 테스트
print("#"*40)
print("무한 입력 테스트")
print("#"*40)
# while True:
#     num = input("1부터 10까지의 숫자를 입력하세요 : ")
#     if num.isdecimal() == True: #bool #isdecimal = 10진수를 찾는 ~~
#         if int(num) >= 1 and int(num) <= 10:
#             print("입력하신 값은 {}입니다.".format(num))
#             break
#         else:
#             print("숫자 범위가 잘못되었습니다 다시입력해주세요.")
#     else:
#         print("{}는 숫자가 아닙니다 다시 업력해주세요".format(num))
#

#for
print("#"*40)
print("for stetement")
print("#"*40)





for n in [1,2,3]:
    print(n)

print("1")
print("2")
print("3")


print("###문자열 for 테스트")
for str in '문자열집합':  # 문자열
    print(str)

print("###리스트 for 테스트")
for lst in ['첫번째', '두번째', '세번째']:
    print(lst)

print("###튜플 for 테스트")
vivaldi_season4 = ('Sprint', 'Summer', 'Fall', 'winter') # 튜플
# tuple은 수정, 삭제가 안됨
for season in vivaldi_season4:
    print(season)

print("###세트 for 테스트") #순서없이 출력
vivaldi_season4 = {'Sprint', 'Summer', 'Fall', 'winter'} #셋트
for season in vivaldi_season4:
    print(season)

print("###레인지 for 테스트")
for n in range(1,10,1):
    print(n)

print("")

for n in range(5):
    print(n)


print("###딕셔너리 for 테스트")
person =  {'name':'jwlee','age':100}
for item in person:
    print(item)
    print(person[item])  # value를 얻는 첫번째 방법
    print(person.get(item)) # value를 얻는 두번째 방법









