# print 함수

# 성적처리 프로그램 v1
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균을 계산하고 출력함

name = '홍홍홍'
kor = 99
eng = 98
mat = 99

tot = kor + eng + mat
avg = tot / 3

#출력 2
print('이름 = ',name)
print('국어 = ',kor, '영어 =', eng, '수학 = ', mat)
print(tot, avg)

# 출력 3 출력서식 사용
# print(출력서식 % 변수들...)
# 출력서식 문자 : %d, %f, %s
print('이름 : %s' % name )
print('국어 : {0:d}, 영어 : {1:03d}, 수학 : {2:03d} ' .format(kor, eng, mat)) # 인덱스 생략 가능
print('총점 : {0:d}, 평균 : {1:.1f} ({1:f})'.format(tot, avg)) # 특정변수 반복출력 가능
print('총점 : {0:d}, 평균 : {1:.1f} ({1:f})'.format(avg, tot)) # 변수의 출력순서 재조정
print('평균 = %.2f' %avg)

# 출력 4 - 인덱스 , 출력서식 사용 .format함수 사용
#print({인덱스:출력서식}.format(변수들..))
print('이름 : {0:s}'.format(name))

# 출력 5 - 문자열 템플릿(f-string) : .format함수 사용 py 3.6이후 지원 (추천)
# print (f'{ 변수명:출력서식}')
print(f'이름 : {name:s}')
print(f'국어 : {kor:d} 영어 : {eng:d} 수학 : {mat:d}')
print(f'총점 : {tot:d} 평균 : {avg:.1f}')

# % 서식
print('===== % 서식 =====')
print("7x1=%d" %7*1)
print("7x2=%d" %7*2)
print("7x3=%d" %7*3)
print("7x4=%d" %7*4)
print("7x5=%d" %7*5)
print("7x6=%d" %7*6)
print("7x7=%d" %7*7)
print("7x8=%d" %7*8)
print("7x9=%d" %7*9)

# ,format
print('===== .format 서식 =====')
print('7x1 : {0:d}'.format(7*1))
print('7x2 : {0:d}'.format(7*2))
print('7x3 : {0:d}'.format(7*3))
print('7x4 : {0:d}'.format(7*4))
print('7x5 : {0:d}'.format(7*5))
print('7x6 : {0:d}'.format(7*6))
print('7x7 : {0:d}'.format(7*7))
print('7x8 : {0:d}'.format(7*8))
print('7x9 : {0:d}'.format(7*9))

# f-string
print('===== f-string 서식 =====')
print(f'7x1 = {7*1:d} : 7x2 = {7*2:d} ')
print(f'7x2= {7*2:d}')
print(f'7x3= {7*3:d}')
print(f'7x4= {7*4:d}')
print(f'7x5= {7*5:d}')
print(f'7x6= {7*6:d}')
print(f'7x7= {7*7:d}')
print(f'7x8= {7*8:d}')
print(f'7x9= {7*9:d}')


ggu = 7
i = 1
print(f'{ggu:d} * {i:d} = {ggu*i:2d}'); i+=1
print(f'{ggu:d} * {i:d} = {ggu*i:2d}'); i+=1
print(f'{ggu:d} * {i:d} = {ggu*i:2d}'); i+=1
print(f'{ggu:d} * {i:d} = {ggu*i:2d}'); i+=1
print(f'{ggu:d} * {i:d} = {ggu*i:2d}'); i+=1
print(f'{ggu:d} * {i:d} = {ggu*i:2d}'); i+=1
print(f'{ggu:d} * {i:d} = {ggu*i:2d}'); i+=1
print(f'{ggu:d} * {i:d} = {ggu*i:2d}'); i+=1
print(f'{ggu:d} * {i:d} = {ggu*i:2d}'); i+=1