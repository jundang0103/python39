# 파일 입출력
# 지금까지 값을 입력받을때는
# 사용자가 직접 키보드로 입력하는 방식을 사용했고
# 값을 출력할때는 모니터 화면에 표시하는 방식을 사용했음

# 하지만, 값을 입력받거나 출력하는 방법은 이게 다가 아님
# 파일을 통해 값을 입력/출력할 수 있고
# 네트워크를 통해 값을 입력/출력할 수도 있음

# 프로그램 실행 중 생성된 데이터들은
# 주로 메모리 내에 존재하는데 프로그램 종료시 같이 소멸됨
# 데이터의 영속성persistence을 부여하기 위해서는
# 데이터를 저장장치에 보관해서
# 데이터가 소멸되지 않도록 하는 것이 중요!

# 파일쓰기 : 데이터를 파일에 기록
# 파일객체변수 = open(경로, 모드)        # py2
# with open(경로, 모드) as 파일객체변수  # py3

# 파일모드 : 파일작업 종류
# w(쓰기), a(추가쓰기), t(텍스트파일 쓰기),
# b(바이너리파일 쓰기)

# 파일쓰기 작업이 끝나면 반드시 close 해줘야 함
# 단, with문을 사용하는 경우 close 생략 가능

# 간단한 인삿말을 파일에 저장
# open(경로/파일명, 작업모드)    # py2
f = open('hello.dat','w') # 쓰기모드로 파일생성
f.write('Hello,world!!') # 지정한 파일에 내용쓰기
f.close()               # 파일 닫음

# with open(경로/파일명, 인코딩, 작업모드)as 별칭    # p3
with open('hello2.dat', 'w', encoding='UTF-8') as f:
    f.write('안농, 세상아')


# 회원정보를 입력받아 member.dat에 저장
# 아이디, 비밀번호, 이름, 이메일,
# 저장형식 : 아이디/비밀번호/이름/이메일 형식으로 파일에 저장
# ex) abc123/987xyz/abc123/abc123@987xyz.co.kr
with open('member.dat','w', encoding="UTF-8") as member:

    id = input('아이디입력')
    pd = input('비밀번호입력')
    name = input('이름입력')
    email = input('이메일입력')
    member.write(id)
    member.write(pd)
    member.write(name)
    member.write(email)

with open('memver.dat','w',encoding='UTF-8') as member:
    while True :
        if input("회원정보를 추가하시겠습니까 (Y/N)").upper() == "Y":
            id = input('아이디입력')
            pd = input('비밀번호입력')
            name = input('이름입력')
            email = input('이메일입력')

            f.write(f' {id} / {pd} / {name} / {email}')
        else:
            f.close()
            break


with open("member.dat", 'w', encoding='UTF-8') as f:
    while True:
        if input('회원정보 추가ㄱㄱ?(y/n) ').upper() == 'Y':
            userid = input('아이디 : ')
            passwd = input('비밀번호 : ')
            name = input('이름 : ')
            email = input('이메일 : ')

            f.write(f'{userid}/{passwd}/{name}/{email}\n')
        else:
            f.close()
            break
# =========================강사님 코드 =======================
userid = input('아이디는 !?')
passwd = input('비번은 !?')
name = input('이름은 !?')
email = input('이메일은 !?')

data = f'{userid} /{passwd} / {name} / {email} \n '
print(data)

with open("member.dat", 'w', encoding='UTF-8') as f:
    f.write(data)

# 파일에 데이터 누적시켜 저장하기
# 파일쓰기모드를 a라고 지정하면
# 이전에 저장한 내용에 새로운 내용을 추가해서 저장함
with open("member.dat", 'a', encoding='UTF-8') as f:
    f.write(data)

# 학생으로부터 이름,국어,영어,수학 점수를 입력받아
# 파일에 저장하세요 (파일명 : sungjuk.dat)
# 단, 점수는 임의로, 파일에 저장하는 형식은
# "이름,국어,영어,수학" 순으로 작성함
# => 혜교,99,98,99 ( csv형식)
name = input("이름입력")
kor = int(input("국어점수입력"))
eng = int(input("영어점수입력"))
mat = int(input("수학점수입력"))

sungjuk = f'{name} {kor} {eng} {mat} \n '
with open("sungjuk.dat",'a', encoding='UTF-8') as f:
    f.write(sungjuk)
