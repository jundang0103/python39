# 함수function
# 주어진 입력값으로 무언가를 수행하고 결과물을 내놓는 객체
# 한번 작성해두면 언제든 재사용 가능
# 논리적인 단위 분할 가능 -> 개발의 분업화
# 코드의 구현을 외부로 부터 숨길수 있음 -> 캡슐화

# 함수 정의
# def 함수이름(매개변수):
#     함수몸체

# 함수 호출
# 함수이름(인수)

# 인사말 출력하는 코드 1
print('Hello, World!!')

# 인사말 출력하는 코드 2 - 3번반복
for _ in range(3):
    print('Hello, World!!')

# 인사말을 출력하는 코드 3 ==> 3번 반복하는 코드를 3번 반복한다면?
# 복붙으로 해결 할 수 있지만,
# 수정사항이 생기면 유지보수가 쉽지 않음
#for _ in range(3):
#   print('Hello, World!!')
#for _ in range(3):
#    print('Hello, World!!')
#for _ in range(3):
#    print('Hello, World!!')
#for _ in range(3):
    for _ in range(3) :
       print("Hello, World !!")

# 인사말을 출력하는 코드 4 ==> 함수
def sayHello():     # 함수 정의
    for _ in range(3) :
       print("Hello, World !!")

sayHello()  # 함수 호출
sayHello()
sayHello()

#-------------------------------------------------
# 매개변수parameter vs 인수argument
# 매개변수 : 함수 정의시 입력으로 전달된 값을 받는 변수
# 인수 : 함수 호출시 실제 입력으로 전달하는 값
def sayHello(msg):
    for _ in range(3) :
       print(f'Hello, {msg}!!')

sayHello('python')
# python : 함수 호출시 함수내부로 전달하는 실제값

sayHello('Java')

# ex) 두수를 입력받아 add 라는 함수로 호출해서 결과 출력
# 단, add라는 함수는 두 입력값을 더한 후 결과 출력함
def add(a,b):
    print(a+b)
add(1,2)


# ==================================
def addNums():
    a = int(input('첫번째 슷자는?'))
    b = int(input('두번째 슷자는?'))
    print(f'{a}+{b}={a+b}')

addNums()

#======================================
def addNums(a,b):
    print(f'{a}+{b}={a+b}')
a = int(input('첫번째 슷자는?'))
b = int(input('두번째 슷자는?'))

addNums(a,b)

# 함수 다중정의 - overloading
# 동일한 이름의 함수를 매개변수에 따라 다른 기능으로
# 동작하도록 작성하는 것을 의미
# 파이썬에서는 공식적으로 지원하는 기능은 아님 - 구현가능
# 다중정의를 너무 남발하면 코드가 복잡해짐

# ex) 잔돈계산하는 프로그램을 함수로 작성
# 함수명 : computeCharge(비용, 지불)
def computeCharge(cost,money):
    charge = money - cost
    back0 = cost - money
    back = back0
    print(f'비용은{cost}이고, 받은금액은 {money}이며,\n 잔액은{charge}입니다.')

    num50000 = back // 50000;
    back = back % 50000
    num10000 = back // 10000;
    back = back % 10000
    num5000 = back // 5000;
    back = back % 5000
    num1000 = back // 1000;
    back = back % 1000
    num500 = back // 500;
    back = back % 500
    num100 = back // 100;
    back = back % 100
    num50 = back // 50;
    back = back % 50
    num10 = back // 10;
    back = back % 10

    print(f'''\
    지불비용은 {cost:,d}원이고,\n
    받은금액은 {money:,d}원이고,\n
    잔액은 {back0:,d}원입니다.\n
    50,000원권은 {num50000}장, 10,000원권은 {num10000}장,
    5,000원권은 {num5000}장, 1,000원권은 {num1000}장,
    500원은 {num500}개, 100원은 {num100}개,
    50원은 {num50}개, 10원은 {num10}개입니다.''')

cost = int(input("지불비용"))
money = int(input("받은금액"))

computeCharge(cost,money)
#=======================================================
# ex) 잔돈계산하는 프로그램을 함수로 작성
# 함수명 : computeCharge(비용, 지불)
def computeCharge(price, inMoney):
    difference = inMoney - price
    balance = 0

    print(
        f"""
    지불 금액은 {price}원 이고,
    받은 금액은 {inMoney}원 이고,
    잔액은 {difference}원 입니다.
    """)

    for cash in [50000, 10000, 5000, 1000, 500, 100, 50, 10]:
        charge = (difference - balance) // cash
        balance += charge * cash
        print(f"{cash}원권은 {charge}장")

computeCharge(17500, 100000)

# =============================================
# ex) 33 - 신용카드 판별하는 프로그램을 함수로 작성
# 함수명 checkCredit(코드)
# dict 자료구조를 이용해서 작성
def checkCredit(code):
    cards= {'356317' : 'NH농협JCB카드',
            '404825' :'비씨Visa카드',
            '515594': '신한Master카드',
            '404825':'비씨 Visa카드',
            '438676':'신한Master카드',
            '457973': 'KB 국민 Visa카드',
            '515594':'신한 Master카드',
            '524353':'외한 Master카드',
            '540926':'KB국민 Master카드'}
    cardname = cards.get(code)
    if cardname == None: print('카드번호를 잘못 입력했습니다.')
    else : print(cardname)

code = input('조회할 카드 번호는?')
checkCredit(code)