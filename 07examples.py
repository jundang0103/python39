# ex) 주민번호에서 생년과 월,일, 성별을 추출해서
# 각 변수에 적절히 저장하세요

jumin ='202205092123456'
        #2022.05.09
year = int(jumin[0:4])
month = int(jumin[4:6])
day = int(jumin[6:8])
gender ="남" if jumin[8:9] == '1'or  jumin[8:9] =='3'  else '여'

print(year,month,day,gender)


# 14 - 시간계산
time = 1234567890
dats = time // 86400  # 정수부만 추출

time = 98765
hours = time // 3600

time =12345
mins = time // 60



# 16 - 잔돈계산
# 비용과 지불금액을 입력받아 잔돈 계산

#지불금액은 ? 원 이고,
#받은금액은 ? 원 이고,
#잔액은 ???원 입니다

#50,000원권은 ?장, 10,000원권은 ?장,
#5,000원권은 ?장 1,000원권은 ?장,
#500원은 ?개 , 100원은 ?개,
#50원은 ?개, 10원은 ?개

cost = int(input("지불비용:"))
pay = int(input("받은금액:"))
back0 = cost - pay
back = back0

num50000 = back//50000 ; back = back % 50000
num10000 = back//10000 ; back = back % 10000
num5000 = back//5000 ; back = back % 5000
num1000 = back//1000 ; back = back % 1000
num500 = back//500 ; back = back % 500
num100 = back//100 ; back = back % 100
num50 = back//50 ; back = back % 50
num10 = back//10 ; back = back % 10


text = f'''\
지불비용은 {cost:,d}원이고,
받은금액은 {pay:,d}원이고,
잔액은 {back0:,d}원입니다.\n
50,000원권은 {num50000}장, 10,000원권은 {num10000}장,
5,000원권은 {num5000}장, 1,000원권은 {num1000}장,
500원은 {num500}개, 100원은 {num100}개,
50원은 {num50}개, 10원은 {num10}개입니다.'''
print(text)

# 파이썬에서 제공하는 몫/나머지 연산자를 이용하면
# 수식이 좀 더 간단해짐

cost = int(input('비용은?'))
money = int(input('지불금액은'))
charge = money = cost

# 50000원권 계산

w50k = charge // 50000
charge = charge % 50000
