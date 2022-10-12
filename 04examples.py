# 1
# 프로그래밍 언어 실습시 글꼴은
# 고정폭 글꼴을 사용할 것을 추천

print("""\
☆   ☆     ☆☆       ☆☆☆☆       ☆☆☆☆      ☆    ☆      /////
☆   ☆    ☆   ☆     ☆     ☆     ☆     ☆     ☆    ☆     | o o |
☆☆☆☆   ☆     ☆    ☆☆☆☆☆     ☆☆☆☆        ☆ ☆     (|  ∧  |)
☆   ☆   ☆☆☆☆☆☆  ☆       ☆    ☆     ☆       ☆       | [_] |
☆   ☆   ☆       ☆  ☆        ☆   ☆      ☆      ☆        -----""")

print("""\ 
               +---+
               |   |
          +---++---+
          |   ||   |
     +---++---++---+    /\\_/\\     -----
     |   ||   ||   |   ( \' \' )   /Hello\\
+---++---++---++---+   (  _  )  < Junior|
|   ||   ||   ||   |    | | |    \\Coder!/
+---++---++---++---+   (__|__)    -----""")

# 3
rate1 = 1
# 1stPlayer = 2         변수명이 숫자로 시작
#myprogram.java = 3   .때문에 불가
long = 4
TimeLimit = 5
numberofWindow = 6
# 4
x, y, z = 1, 2, 3
print (3 * x, 3 * x + y, (x+y) / 7 )
s0, v0, t, g = 4, 5, 6, 9.8
print(s0 + v0 * t (1/2) * 9 * t ** 2)

# 6
x = 2.5
y = 1.5
m = 18
n = 4
#가
print( x+n * y -( x+n)* y)
#나
print( m/n + m% n)
#다
print(5 * x - n/5)
#라
print (1 -(1-(1-(1-(1-n)))))

#7

print(3 + 4.5 * 2 + 27 / 8)
# 논리연산시 경우에 따라 단축식 평가가 적용되기도 함
print(True or False and 3 < 4 or not (5 == 7))

print(True or 3 < 5 and 6 >=2)

#print(not true >'A')
print(not True >bool('A')) # (True > True)

#print(7 % 4 + 3 - 2 / 6 * 'z')
print(7 % 4 + 3 - 2 / 6 * bool('z'))

#print ('D' + 1 +'M' % 2/ 3)
print(bool('D')+ 1 + bool('M') % 2 / 3)

#9
print(True and False and True or True)
print(True or True and True and False)
print((True and False) or (True and not False ) or (False and not False))
print ((2 < 3 ) or ( 5 > 2) and not( 4 == 4) or( 9 != 4))
print( 6 == 9 or 5 < 6 and 8 < 4 or 4 > 3)

#10
print(27 / 13 + 4)
print(27 / 13 + 4.0)
print(42.7 % 3 + 18)

# 논리식과 산술식(값)이 결합된 수식에서는
# 논리식의 결과가 True면 값이 출력
# 논리식의 결과가 False면 False가 출력
print((3 < 4 ) and 5 / 8)

print(23 / 5 + 23 / 5.0)

# print( 2.0 + 'a')   # 문자와 정수/ 실수간 산술연산 불가
print(2 + 'a')
print('a' + 'b')
# print('a'/ 'b')  # 문자간 산술연산 불가

print('a' and not 'b')
print('a' and 'b')

# print((float) 'a' / 'b')  # 문자는 실수로의 형변환 불과

#11

name = input("이름입력 :")              # name = '홍길동'
weight = input("몸무게입력:")           # weight = 55.5
age = input("나이입력: ")               # age = 35
print(name, weight, age)


#12


# K나이 - 세는나이(출생시 1살, 해가 바뀌면 + 1)
#        만나이(출생시 0살, 생일이 지나면 + 1)
#        연나이(현재연도 - 출생연도)
birthYear = 1990
currentYear = 2022
isPassBirth = True

age = currentYear - birthYear

print('연나이 = ', age)
print('세는나이', 1 + age)

#파이썬 if 단축식 : 참일때 값 if 조건식 else 거짓일때 값
print('만나이', (age + 1) if isPassBirth else age)

# 13
print('7 x 1 = ', (7*1))
print('7 x 2 = ', (7*2))
print('7 x 3 = ', (7*3))
print('7 x 4 = ', (7*4))
print('7 x 5 = ', (7*5))
print('7 x 6 = ', (7*6))
print('7 x 7 = ', (7*7))
print('7 x 8 = ', (7*8))
print('7 x 9 = ', (7*9))