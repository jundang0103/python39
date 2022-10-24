
# 회원가입을 처리하는 클래스 생성
# MemberVO :
#     userid, passwd, name, email, milege, grade
# MemberService :
#  registerMember  : 회원 정보 입력
#  processMemberGrade : 마일리지에 따라 회원 등급 결정
#      vip : 마일리지 - 10000이상
#      gold : 마일리지 - 7000이상
#      silver : 마일리지 - 4000이상
#      bronze : 마일리지 - 1000이상
#      member : 그외


class MemberVO:
    def __init__(self, userid, passwd, name, email, mileage, grade):
        self.__userid = userid
        self.__passwd = passwd
        self.__name = name
        self.__email = email
        self.__milege = mileage
        self.__grade = 'member'

    def __str__(self):
        result =f"{self.__userid},{self.__passwd},{self.__name}," \
                f"{self.__email},{self.mileage},{self.__grade}"
        return result

    @property

    def mileage(self):
        return self.__milege

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade):
        self.__grade = grade


class MemberService:

    @staticmethod
    def registerMember():
        uid = input("아이디는?")
        pwd = input("비번은?")
        name = input("이름은?")
        email = input("이메일은?")
        mileage = int(input("마일리지는?"))

        return MemberVO(uid, pwd, name, email, mileage)

    @staticmethod
    def processMemberGrade(mvo):
        if mvo.mileage >= 10000: mvo.grade = "vip"
        elif mvo.mileage >= 7000: mvo.grade = "gold"
        elif mvo.mileage >= 4000: mvo.grade = "silver"
        elif mvo.mileage >= 1000: mvo.grade = "bronze"

# 코드 실행
mb = MemberService.resgisterMember()
MemberService.processMemberGrade(mb)
print(mb) # ==> 결과 출력