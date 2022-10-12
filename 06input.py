# input 함수
# 변수명  = input (입력메세지)

# 성적처리 프로그램 v2
# 이름, 국어, 영어, 수학을 입력받아
# 퐁점, 평균을 계산하고 출력함
# input함수로 입력받은 내용은 기본적으로 문자로 취급 !

name = input('이름은?')
kor = int(input('국어점수 입력 : ')) # 산술식에 사용해야 함으로 형변환 필요
eng = int(input('영어점수 입력 : '))
mat = int(input('수학점수 입력 : '))

tot = kor + eng + mat
avg = tot/3

print(f'이름 : {name:s}')
print(f'국어: {kor:d}, 영어: {eng:d}, 수학: {mat:d}')
print(f'총점: {tot:d}, 평균 {avg:.2f}')


# p57 ex3)

# 조건1 지방, 탄수화물 단백질의 그램을 키보드로 입력받는다
# 조건2 총 칼로리 = 지방 * 9 + 단백질 * 4 + 탄수화물 * 4

ji = int (input ('지방의 그램을 입력하세요'))
dan = int (input('탄수화물의 그램을 입력하세요'))
tan = int (input('단백질의 그램을 입력하세요'))

kacl = (ji*9)+(dan*4)+(tan*4)
print(f' 총칼로리 : {kacl:d} cal')

print(f"""
총칼로리 : {(int(input('지방 : ')) * 9 + int(input('단백질 : ')) * 4 + int(input('탄수화물 : ')) * 4)}cal
""")

# 풀이2 - input 함수 사용
fat = float(input('지방은?'))
carbo = float(input('탄수화물은?'))
protein = float(input('단백질은?'))

total = fat * 9 + carbo * 4 + protein * 4
print(f'총 칼로리 : {total}cal')


# 성적처리 프로그램의 메뉴화면 작성 1
print('성적 처리프로그램 v1')
print('------------------')
print('1. 성적 데이터 추가')
print('2. 성적 데이터 조회')
print('3. 성적 데이터 상세조회')
print('4. 성적 데이터 수정')
print('5. 성적 데이터 삭제')
print('0. 프로그램 종료')
print('------------------')

# 성적처리 프로그램의 메뉴화면 작성 2
main_menu = '성적 처리프로그램 v1 \n'
main_menu += '1. 성적 데이터 추가 \n'
main_menu += '2. 성적 데이터 조회 \n'
main_menu += '3. 성적 데이터 상세조회 \n'
main_menu += '4. 성적 데이터 수정\n'
main_menu += '5, 성적 데이터 삭제\n'
main_menu += '0. 프로그램 종료 \n'
main_menu += '------------------'

print(main_menu)

# 성적처리 프로그램의 메뉴화면 작성3

main_menu = f'''
성적 처리프로그램 v1
====================
1. 성적 데이터 추가
2. 성적 데이터 조회
3. 성적 데이터 상세조회
4. 성적 데이터 수정
5. 성적 데이터 삭제
0. 프로그램 종료
===================='''
print(main_menu)
input('=> 작업을 선택하세요 :')