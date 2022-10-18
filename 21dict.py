# dict
# 비순차 자료구조
# 키를 통해 값을 찾는 연관배열 객체
# 선언방법은 { 키:값 } 형태로 정의하고 사용
# 다양한 자료형으로 구성된 데이터를
# 하나의 변수로 접근할 수 있음

# dict 선언
member = { 'userid': 'abc123','passwd':'987xyz'}

# dict 값 조회 : 객체명['키명'], 객체명.키명
print(member['userid'],member['passwd'])

# dict 모든 키 조회 : 객체명.keys()
# for ~ in 반복문으로 조회 가능
print(member.keys())

for key in member.keys():
    print(key,end=' ')

# dict 모든 값 조회 : 객체명.keys()
 # for ~ in 반복문으로 조회 가능함

print(member.values())
for val in member.values():
     print(val,end=' ')

# dict 모든 키, 값 조회 1 : 객체명.items()
print(member.items())

for k, v in member.items():
    print(f'({k},{v})',end=' ')

# dict 모든 키, 값 조회 2 : 키 이용 (추천)
for k in member.keys():
    print(member[k], end='')

# dict 모든 키, 값 조회 2: 객체명.get(키) 이용
for k in member.keys():
    print(member.get(k),end=' ')


# dict 동적 생성 1
user = {}  # 사용자 - 이름, 나이, 이메일로 구성

# 객체명[새로운키] = 새로운값
user['name'] = '홍길동'
user['age'] = 15
user['email'] = 'abc123@987xyz.com'

# dict 동적 생성 2 : dict( 키 = 값 , ..)
user2 = dict(name='홍길동', age=35, email='abc123@987xyz.co.kr')

print(user2)

# dict 동적 생성 3 : list 이용 - dict ([ [키, 값], ...])
user3 = [ ['name'], ['홍길동'], ['age',35], ['email', 'xyz@abc.co.kr']]

print(dict(user3))

# dict 수정하기 : 객체명[기존키] = 새로운값
user['age'] = 30
user['email'] = '123@987.co.kr'

# dict 삭제하기 : del 객체명[기존키]
del user['age']

# 객체명.get(키) Vs 객체명[키]
user['regdate'] # 존재하지 않는 키 호출시 - 오류표시
# 오류발생시 예외처리 코드로 적절히 대처

user.get('regdate') # 존재하지 않는 키 호출시 - 오류표시 x
# 반환값이 None인지 여부에 따라 오류처리 대처


# ex1) dict 자료구조를 이용해서 학생 1명분의 데이터를 입력받아 처리
# 저장형식 : { 'name':??, 'kor':??, 'eng':??, 'mat':??,
#             'tot':??, 'avg':??, 'grd':??  }

student = {}
student['name'] = input("이름입력")
student['kor'] = int(input("국어 점수입력"))
student['eng'] = int(input("영어 점수입력"))
student['mat'] = int(input("수학 점수입력"))
student['tot'] = student.get('kor')+student.get('eng')+student.get('mat')
student['avg'] = student.get('tot') / 3
if student['avg'] >= 90 :
    student['grd'] = '수'
elif student['avg'] >= 80 :
    student['grd'] = '우'
elif student['avg'] >= 70 :
    student['grd'] = '미'
elif student['avg'] >= 60 :
    student['grd'] = '양'
else : student['grd'] = '가'

print(student)



# ex2) dict 자료구조를 이용해서 학생 3명분의 데이터를 입력받아 처리
# 저장형식 : { 'name':??, 'kor':??, 'eng':??, 'mat':??,
#             'tot':??, 'avg':??, 'grd':??  }
students = []
for _ in range(3) :
    student = {}
    student['name'] = input("이름입력")
    student['kor'] = int(input("국어 점수입력"))
    student['eng'] = int(input("영어 점수입력"))
    student['mat'] = int(input("수학 점수입력"))
    student['tot'] = student.get('kor')+student.get('eng')+student.get('mat')
    student['avg'] = student.get('tot') / 3
    if student['avg'] >= 90 :
        student['grd'] = '수'
    elif student['avg'] >= 80 :
        student['grd'] = '우'
    elif student['avg'] >= 70 :
        student['grd'] = '미'
    elif student['avg'] >= 60 :
        student['grd'] = '양'
    else : student['grd'] = '가'

    students.append(student)
print(students)

# dict 형식 데이터 출력시 예쁘게 표시 : pretty print
from  pprint import  pprint as pp

pp(students)


# =================================================================== Study 할 것 !
# dict
# 비순차 자료구조
# 키를 통해 값을 찾는 연관배열 객체
# 선언방법은 { 키:값 } 형태로 정의하고 사용
# 다양한 자료형으로 구성된 데이터를
# 하나의 변수로 접근할 수 있음

# dict 선언
member = {'userid': 'abc123', 'passwd': '987zxc'}

# dict 조회: 객체명['키명'], 객체명.키명
print(member['userid'])

# dict 모든 키 조회: 객체명.keys() => list 형 반납
print(member.keys())

print('------------------- 키조회')
for member_key in member.keys():
    print(member_key)
print('-------------------')
print('------------------- 값조회')
for member_value in member.values():
    print(member_value)
print('-------------------')
print('------------------- 키로 값 조회')
for member_key in member.keys():
    print(member[member_key])
print('-------------------')

print('------------------- 키로 값 조회 .get() 메소드 활용')
for member_key in member.keys():
    print(member.get(member_key))
print('-------------------')

print('------------------- 키, 값 조회')
for key, value in member.items():
    print(key, ' : ', value)
print('-------------------')

# items() 메소드는 2차원 tuple에 1번방, 2번방은 k, v 인자로 전달 받아 처리
# 그럼 내가 중복 tuple를 직접 선언해도 처리가 가능한가?
# 질문에서 시작한 코딩
print('------------------- 키, 값 조회')
for k, v in (('test', 'ttt'), ('안녕', '바보야')):
    print(k, ' : ', v)
print('-------------------')

# 직접 선언해서 처리는 가능 하네? 그럼 3개 전달 받아서 처리는 가능한가?
# 질문에서 시작한 코딩
# 에러나네? 이렇게 사용은 불가
# print('------------------- 키, 값 조회')
# for k, v, c in (('test', 'ttt'), ('안녕', '바보야'), ('멋을보니?', '허허허')):
#     print(k, ' : ', v, ' : ', c)
# print('-------------------')

# 직접 선언해서 처리는 가능 하네? 그럼 3개가 선언 되어 있으나 2개를 전달 받아서 처리는 가능한가?
# 질문에서 시작한 코딩
print('————————— 키, 값 조회')
for k, v in (('test', 'ttt'), ('안녕', '바보야'), ('멋을보니?', '허허허')):
    print(k, ' : ', v)
print('—————————')