# 78 ex2) 숫자 맞추기
import  random as rnd

print('=============숫자 맞추기 GA============')
com = rnd.randrange(1,10)
while True :
    my = int(input('예상 숫자를 입력해 :'))
    if my == com :
        print("정답입니당")
        break
    else :
        print('다시 입력해주쎼용')
print('======================================')

magic = rnd.randint(1,10) # 난수 초기화
while True :
    key = int(input('숫자 하나 입력하심 : '))

    if magic == key :
        print('성공')
        break
    elif magic < key: print("숫자가 커요")
    else : print("숫자가 작아")


# ex3) 숫자 맞추기 (1~100)
import  random as rnd
b = rnd.randrange(1,100)

while True :
    a = int(input('예상 숫자 입력해줄래요'))
    if a == b :
        print('정답이오')
        break
    else :
        print("다시다시")

while True:
    num1 = rnd.randint(1,100)
    num2 = int(input('1~100사이 숫자 하나 입력할래?'))

    if num1 < num2 : print('숫자가 큰듯')
    elif num1 > num2 : print('숫자가 작은듯?')
    else :
        print('BINGO !')
        break


# ex25) 복권 프로그램 = 3자리수 입력
# 난수 범위 = 100 ~ 999, 위치는 상관없이 숫자만 일치여부 판단
# ex) 123 => 345(1), 317(2), 312(3)
# 문자열 슬라이싱을 위한 문자열 변환 str 함수 사용
# 3개 일치 = 상금 백 만 원
# 2개 일치 = 상금 오 천 원
# 1개 일치 = 상금 1 천 원
# 0개 일치 = 다 음 기 회 에
import  random as rnd


lotto = rnd.randint(100, 999)
# lotto1 = str(rnd.randint(1,9))

# lotto = lotto1 + lott2 + lotto3

mykey = input('3자리 복권 번호가 !? ( 100 ~ 999) ')
match = 0 # 일치여부를 저장

# 첫째 자리 비교
#if lotto[0] == mykey[0] or lotto[0] == mykey[1] or lotto[0] == mykey[2] :
#    match += 1
# 둘째 자리 비교
#if lotto[1] == mykey[0] or lotto[0] == mykey[1] or lotto[0] == mykey[2]:
   # match += 1
#셋째 자리 비교
#if lotto[2] == mykey[0] or lotto[0] == mykey[1] or lotto[0] == mykey[2] :
   # match += 1

# 개선된 코드 1
for i in range(3):
    if lotto[i] == mykey[0] or lotto[i] == mykey[1] or lotto[i] == mykey[2] :
        match += 1
# 개선된 코드 1b
for i in range(3):
    if lotto[i] == mykey[0] : match += 1
    if lotto[i] == mykey[1] : match += 1
    if lotto[i] == mykey[2] : match += 1

#개선된 코드 2
for i in range(3):
    for j in range(3):
        if lotto[i] == mykey[j]:
            match += 1

# 당첨 여부 판단
if match == 3 :
    print('1등 당첨 상금 백 만 원 ! ')
elif match == 2 :
    print('2등 당첨 상금 만 원')
elif match == 1 :
    print(' 3등 당첨 천 원')
else: print('아쉽지만 담주에봐')