# 33 - 신용카드 판별
card = input('신용카드 번호는 ?')
result = ''

if card[:2] == '35' :
    nums = card[2:]    # 나머지 카드 번호 추출
    if nums == '6317':  result = 'NH농협 JCB카드'
    elif nums == '6901' : result = '신한 JCB카드'
    elif nums == '6912' : result = 'KB국민 JCB카드'
    else: result ='잘못된 카드 번호야 !'
elif card[:1] == '4' :
     nums = card[1:] # 나머지 카드 번호 추출
     if nums == '04825': result ='비씨 Visa카드'
     if nums == '08678': result ='신한 Visa카드'
     if nums == '07973': result ='KB국민 Visa카드'
     else:
         result = '잘못된 카드 번호야 !'
elif card[:1] == '5' :
    nums = card[1:]  # 나머지 카드 번호 추출
    if nums == '15594': result = '신한 Master카드'
    if nums == '24353': result = '외한 Master카드'
    if nums == '40926': result = 'KB국민 Master카드'
    else:
        result = '잘못된 카드 번호야 !'
print(result)


# 35 - 시간때를 의미하는 영단어 판별
daytime = input('시간때를 의미하는 영단어는?')
result = '잘못입력하셨습니다 !'

if daytime == 'morning hours' : result = '아침시간 (7-12)'
# elif daytime == 'midday' or daytime =='noon' : result = '점심시간'
elif daytime in ( 'midday' ,'noon') : result = '점심시간 (12-1)'
elif daytime == 'afternoon hours' : result = '오후(1~6)'
elif daytime == 'night hours' : result = '저녁시간(6~9)'


# switch ~ case 와 비슷하게 작성해보기
# 파이썬은 지금까지(~v3.9) swtich ~ case 구문을 지원하지 않음
# 만일, switch ~ case 구문을 구현하려면 dict를 이용해야 함
# 한편, v3.10 이상부터는 match case 라는 구문으로 구현가능

# dict 자료구조
#  키와 값 형태로 자료를 저장하는 형식
# 연관(키-값) 배열 자료형의 한 종류임
# 객체명 ={키 : 값} => 객체명.get(키), 객체명[키]

cards = {'356317' : 'NH농협JCB카드',
        '404825' :'비씨Visa카드', '515594': '신한Master카드'}
cards.get('404825')

datetimes ={'midday':'점심시간','midnight':'자정시간','small hours':'새벽'}
datetimes.get('midnight')

# 성적처리 프로그램 v3b
# 이름, 국어, 영어, 수학을 입력받아
# 총점, 평균, 학점을 게산하고 출력함
# 학점처리 조건은 수우미양가로 하되
# 단, 학점은 dict를 이용해서 처리함

print('''\
성적 처리프로그램 v3b
-------------------''')
name = input('이름 : ')
kor = int(input('국어 : '))
eng = int(input('영어 : '))
mat = int(input('수학 : '))

tot = kor + eng + mat
avg = tot/3
grds = {
    10 : '수',
     9 : '수',
     8 : '우',
     7 : '미',
     6 : '양',
     5 : '가',
     4 : '가',
     3 : '가',
     2 : '가',
     1 : '가',
     0 : '가'
}
grade = grds.get(avg//10)
print(f'''\
이름:{name:s}\n국어:{kor:3d}점, 영어:{eng:3d}점, 수학:{mat:3d}점
총점:{tot:3d}점, 평균:{avg:.1f}점, 학점은 {grade:s}입니다.''')

# 3항 연산자 - if 단축문 : 컨프리헨션
# 참일때 값 if 조건식 else 거짓일때 값

print( '참' if True else '거짓')
print( '참' if False else '거짓')

# ex) 윤년여부를 출력하는 프로그램을 작성하세요
# 단, 3항 연산자를 이용해서 구현함

year =int(input("몇년임"))

isLeapYear = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
result ='윤년입니다' if isLeapYear else '윤년이 아닙니다'
print(year, result)


# ex) 년도와 월을 입력받아
# 윤년여부와 입력한 달의 마지막 날을 출력하는 프로그램을 작성하세요
# 30: 4, 6 , 9 , 11
# 31: 1, 3 , 5, 8, 10, 12
# 28 : 2 (윤년이 아닐때)
# 29: 2 (윤년일때)
