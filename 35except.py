# 예외처리
# 프로그램을 만들다 보면 수많은 에러가 발생함
# 코드를 잘못 작성하거나, 실행상의 문제로 인해
# 에러가 발생하면 프로그램 실행이 중단되기도 함
import sys

# 하지만, 프로그램이 중단되는 것을 피하기 위해
# 이러한 에러는 무시하고 넘어가줬으면 하는때도 있음
# 에러에 따른 적절한 처리를 하고 싶을때도 있을 것임

# 파이썬에서는 try-except 구문으로
# 예외처리를 할 수 있음

# error와 except 차이 비교
# 에러 : 프로그램 실행 중 오작동이나 비정상적 종료를
# 유발하게 하는 원인

# 컴파일 오류 : 주로 문법적 오류를 의미 - 개발자가 조치가능함
# 논리 오류 : 실행 가능 하지만 예상한 결과가 안나오는 오류 - 개발자가 조치가능함
# 시스템 오류 : 메모리 초과, 서버접속 불가등등의 오류 - 조치 불가함
# 실행 오류 : 프로그램 실행 중 발생하는 예외적인 오류
#    ex : 어떤 값을 0으로 나누는 경우, 리스트의 인덱스를 잘못 호출하는 경우 둥둥
# 잘못된 코드들의 사용

# 예외 : 개발자가 완전히 조치할 수 없지만
# 어느정도 수습할 수 있는 수준의 덜 심각한 오류
# 예외처리를 통해 프로그램의 비정상 종료를 막을 수 있음

# 오류발생 1
print('-프로그램 시작-')
print(10/5)
print('-프로그램 끝-')  # 정상종료

# 오류발생 2
print('-프로그램 시작-')
print(10/0)
print('-프로그램 끝-')  # 오류

# 오류발생 3
print('-프로그램 시작-')
nums = [1,2,3]
print(nums[100])
print('-프로그램 끝-')  # 오류

# 발생한 오류를 예외처리하기
# try :
#    오류가 발생한 코드
# except :
#   오류발생시 처리할 코드

# 예외처리 1
print('----프로그램 시 작 ====')
try:
    print(10/0)  # 오류가 발생하더라도
except:
    print("오류발생")
print("프로그램 끝") # 중단되지 않고 끝까지 실행


# 예외처리 2
try:
    print('----프로그램 시 작 ====')
    print(10/0)  # 오류가 발생하면 except로 jump
    print("프로그램 끝") # 따라서, 이 코드는 실행되지 않음
except:
    print("오류발생")

# 예외처리 3
    print('----프로그램 시 작 ====')
    nums =[1,2,3,]
try:
    print(nums[100])
except:
    print("오류발생")
print("=====프로그램 끝=======")  # 중단되지 않고 끝까지 실행

# 발생한 오류를 특정지어 예외처리하기
# try:
#   오류가 발생할만한 코드
# except 발생한 오류유형:
#   오류유형별 처리코드

# 오류발생4
# 다양하게 발생하는 예외 상황에 대한 적절한 코드 작성
# 아래 코드 실행시 발생하는 오류수는 3가지
# 1. 리스트 인덱스 초과
# 2. 0으로 나누려고 할 때
# 3. 문자 입력시

# 예외처리 4 - 예외처리가 너무 포괄적임
nums = [1, 10, 20 ,50]

try:
    idx = int(input('nums에서 사용할 값의 index는?'))
    divr = int(input('앞에서 선택한 값을 나눌 정수는?'))
    print(nums[idx] / divr)
except:
    print('오류 발 생')


# 예외처리 5 - 예외처리를 유형별로 세분화함
nums = [1, 10, 20 ,50]

try:
    idx = int(input('nums에서 사용할 값의 index는?'))
    divr = int(input('앞에서 선택한 값을 나눌 정수는?'))
    print(nums[idx] / divr)
except IndexError:
    print('리스트의 인덱스가 너무 커요 !')
except ZeroDivisionError:
    print('0으로 뭘 나눌라고 어이없어')
except ValueError:
    print('숫자만 입력하라고')

# 파이썬에서 제공하는 예외처리 모듈
import builtins

dir(builtins)

# 예외상황 확인방법
nums = [1, 10, 20, 50]

try:
    idx  = int(input('nums에서 사용할 값의 index : '))
    divr = int(input('앞에서 선택한 값을 나눌 정수 : '))
    print(nums[idx]/divr)
except Exception as e:
    print(f'{type(e)} : {e}')
    
# 예외의 에러 메세지 받아오기
# try:
#   오류가 발생할만한 코드
# except 예외명 as 별칭 :
#   print(별칭)

# 예외처리 6 - 에러 메세지 상세 출력
nums = [1, 10, 20, 50]

try:
    idx  = int(input('nums에서 사용할 값의 index : '))
    divr = int(input('앞에서 선택한 값을 나눌 정수 : '))
    print(nums[idx]/divr)
except Exception as e:
    print(f'{type(e)} : {e}')
except IndexError as ie:
    print('인덱스 초과요',ie)
except ZeroDivisionError as zde:
    print('0으로 못나눔',zde)
except ValueError as ve:
    print('숫자만 입력 plz',ve)

# 예외처리 7 - 에러 메세지 상세 출력
import  sys
nums = [1, 10, 20, 50]

try:
    idx  = int(input('nums에서 사용할 값의 index : '))
    divr = int(input('앞에서 선택한 값을 나눌 정수 : '))
    print(nums[idx]/divr)
except Exception:
    extype, exval,traceback = sys.exc_info()
    # 현재 발생한 예외 정보를 tuple로 반환
    print(extype.__name__) # 예외 이름
    print(traceback.tb_frame.f_code.co_filename)
    print(traceback.tb_lineno)  # 예외발생 위치
    print(exval.message)        # 예외 메세지

# 예외발생과 상관없이 항상 코드 실행 : finally
# 주로 자원반납과 관련된 코드들에 사용
# try
#    코드
# except:
#   예외처리
# finally:
#   항상실행될코드

# 예외처리 8
try:
    print('----프로그램 시 작 ====')
    # print(10/0)
    print(10/10 )
except:
    print("오류발생")
finally:
    print("===========프ㄹ그램끝")