# 함수를 이용한 성적처리 프로그램
# 함수 정의부
def displayMenu():
    main_menu = f'''
    성적 처리프로그램 v4
    ====================
    1. 성적 데이터 추가
    2. 성적 데이터 조회
    3. 성적 데이터 상세조회
    4. 성적 데이터 수정
    5. 성적 데이터 삭제
    0. 프로그램 종료
    ===================='''
    print(main_menu)


def inputSungJuk():

    name = input("이름은?")
    kor = int(input("국어는??"))
    eng = int(input("영어는??"))
    mat = int(input("수학은??"))
    sj = {'name':name, 'kor':kor, 'eng':eng, 'mat':mat}

    return  sj
def addSungJuk():
    # 성적 데이터 입력 받기
    sj = inputSungJuk()

    
    # 입력받은 성적데이터 초기화
    tot, avg, grd = computeSungJuk(sj)

    sj['tot'] = tot
    sj['avg'] = avg
    sj['grd'] = grd


    sjs.append(sj)
    input('성적 데이터 추가 완료 !')

def readSungJuk():
    hdr = '이름 국어 영어 수학 평균 학점\n'
    hdr += '========================='
    print(hdr)

    for sj in sjs:
        print(f'{sj["name"]} {sj["kor"]} {sj["eng"]} {sj["mat"]} {sj["avg"]} {sj["grd"]}')
        input('성적 데이터 조회 완료 !')


def readOneSungJuk():
    name = input('조회할 학생의 이름은?')
    sj = None
    for item in sjs:
        if item['name'] == name: sj = item
        hdr = '이름 국어 영어 수학 총점 평균 학점 \n'
        hdr += '----------------------------\n'
        print(hdr)
        for k in sj.keys():  # sjs에서 입력한 이름과 일치하는 항목을 찾음
            print(sj.get(k), end=' ')

    input('\n성적 데이터 상세조회 완료 !')


def modifySungJuk():
    name = input("수정할 학생 이름은 ? ")

    sj = None
    for i,item in sjs:  # 입력한 이름과 일치하는 항목을 sjs에서 찾음
        if (sjs[i])['name'] == name: idx = i
        break

    # 새로운 값을 입력받음
    kor = int(input(f'새로운 국어 점수는? ({sjs[idx]["kor"]}'))
    eng = int(input(f'새로운 영어 점수는? ({sjs[idx]["eng"]}'))
    mat = int(input(f'새로운 수학 점수는? ({sjs[idx]["mat"]}'))

    #다시 성적 처리
    tot, avg ,grd = 0, 0, '가'
    computeSungJuk(kor,eng,mat,tot,avg,grd)
    sj['tot'] = tot
    sj['avg'] = avg
    sj['grd'] = grd

    # 값 다시 저장
    sj = {'name': name, 'kor': kor, 'eng': eng, 'mat': mat, 'tot': tot, 'avg': avg, 'grd': grd}
    tot, avg, grd =computeSungJuk(sj)

    # 기존 위치에 다시 저장
    sjs[idx] = sj
    print('성적 데이터 수정 완료 !')

def removeSungJuk():
    name = input("삭제할 데이터의 학생 이름은")

    idx = None
    for i in range(len(sjs)):  # 삭제할 데이터의 인덱스 조사
        item = sjs[i]
        if item['name'] == name: idx = i
        sjs.pop(idx)

    input('성적 데이터 삭제 완료 !')

def computeSungJuk(sj):
    tot = sj['kor'] + sj['eng'] + sj['mat']

    avg = tot / 3
    grd = '가'
    if avg >= 90:
        grd = '수'
    elif avg >= 80:
        grd = '우'
    elif avg >= 70:
        grd = '미'
    elif avg >= 60:
        grd = '양'

    return tot,avg,grd

# 성적 데이터 저장할 변수 선언
sjs = []

# 프로그램 주 실행부

while True:
    # 메뉴 표시 및 값 입력
    # 메뉴입력받음
    displayMenu()
    menu = input('==> 메뉴를 선택 하세요')

    if menu == '1': addSungJuk()

    elif menu =='2': readSungJuk()

    elif menu =='3': readOneSungJuk()

    elif menu =='4': modifySungJuk()

    elif menu =='5': removeSungJuk()

    elif menu =='0': break

    else:
        print('잘못된 번호를 입력하셨습니다.')

