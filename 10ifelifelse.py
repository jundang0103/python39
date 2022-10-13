# 다중 if문
# if~else만으로 다양한 조건을 판단하기 어려움
# ==> 물론 여러개의 if문을 사용해서 처리 가능함
# 다양한 조건에 따라 판단하기 위해서는
# if ~ elif ~ else 구문을 사용해야 함
import datetime

# if 조건식1:
#    조건식1이 참일때 실행할 문장
# elif 조건식2:
#    조건식2이 참일때 실행할 문장
# ...
# else:
#    거짓일때 실행할 문장

# 결과 조건 : 점수 0 ~ 50  ==> 노력하세요
#               51 ~ 80  ==> 잘했다 !
#               81 ~ 100 ==> 최고야 !

jumsu = 55

if jumsu >= 100 : print('최고')
if jumsu >= 80 : print('잘했다 !')
if jumsu >= 50 : print('노력해')
# ==> 결과가 올바르지 않게 나옴
if 0 <= jumsu <= 50 : print('노력하세요')
else :
    if 51<= jumsu <= 80 : print('잘했다 !')
    else :
         if 81<= jumsu <= 100 : print('최고야 !')
# 들여쓰기를 조건에 따라 작성해야 함 0 가독성 떨어짐

if jumsu <= 50:
    print("노력하세요")
elif jumsu <= 80 :
    print('잘함')
elif jumsu <= 100 :
    print('최고야')
# 조건문장 작성시 들여씌기를 일정하게 사용 - 가독성 좋음

if jumsu >= 0 : print('노력')
if jumsu >= 50 : print('잘함')
if jumsu >= 80 : print('최고')

# 성적처리 프로그램 v3
# 이름, 국어, 영어, 수학을 입력받아
# 총점, 평균, 학점을 게산하고 출력함
# 학점처리 조건은 수우미양가로 함

print('==========성적처리 프로그램 v3============')

kor = int(input('점수를 입력하세요'))
eng = int(input('점수를 입력하세요'))
math = int(input('점수를 입력하세요'))
sum = kor + eng + math
avg = sum / 3
grade = avg

if avg >= 80 :
    print('수')
elif avg >=60 :
    print('우')
elif avg >=50 :
    print('미')
elif avg >=40 :
    print('양')
elif avg >= 30:
    print('가')

print(f'''
당신의 총점은 {sum:d} 이며 평균은 {avg:2f} 이고 등급은 
''')

name = input('이름은?')
kor = int(input('국어점수 :'))
eng = int(input('영어점수 :'))
math = int(input('수학점수 :'))

tot = kor + eng + math
avg1 = tot / 3

grd = '가'
if avg >= 90 : grd ='수'
elif avg >= 80: grd ='우'
elif avg >= 70: grd ='미'
elif avg >= 60: grd ='양'

print(f'이름,{name} 국어:{kor} 영어:{eng} 수학:{math}')
print(f'총점,{tot} 평균: {avg1}학점:{grd}')

# ex) p77. 항공사 짐 무게 측정
kg = int(input('짐의 무게는 얼마에요?'))
if kg >= 10 :
    print('수수료는 10,000원입니다')
else:
    print('수수료는 없어용')

    # =======================
cargo = int(input('짐의 무게는 얼마입니까? (단위kg)'))
result = '수수료 없어용 '

if cargo >= 10 :
    print('수수료가 10,000원이에용')

print(f'짐의 무게는 {cargo:d}kg이고요 {result}')

# ex) p77 항공사 짐 무게에 따른 수수료 계산
# 수수료는 10의 배수 단위고 10,000씩 증가...
kg = int(input('짐의 무게는 얼마에요?'))
tax = kg // 10
if kg < 10 :
    print('수수료는 없어용')
elif kg >= 10 :
    tax1= tax * 10000
    print(f'수수료는 {tax1:d}입니다 ')

    #==================
cargo = int(input('짐의 무게는 얼마입니까? (단위kg)'))
result = '수수료 없어용 '
pat = 0

if cargo >= 10:
    pay = (cargo // 10) * 10000
    result = f'수수료는 {pay}이에용'

# 나이에 따른 학생 분류 후 결과 추력
# 8 ~: 초등학생
# 14 ~ : 중학생
# 17 ~ : 고등학생
# 20 ~ : 대학생
# 26 ~ : 학생이 아닙니다
import datetime
thisYear = datetime.datetime.now().year
birth = int(input('출생연도는 ?'))
age = thisYear - birth + 1

if age >= 26: print('성인')
elif age >= 20: print('대학생')
elif age >= 17: print('고등학생')
elif age >= 14: print('중학생')
elif age >= 8: print('초등학생')
else: print('kids..')


byear = int(input('언제 태어났니 !'))
year = 2022
age = year -byear + 1
result = '학생이 아니야 너 '

if age >= 26 : result = '학생이 아니라구요'
elif age >= 20: result = '대학생이세요'
elif age >= 17: result = '고딩이래요'
elif age >= 14: result = '중딩이래요'
elif age <= 8: result = '잼민이래요'
