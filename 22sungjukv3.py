# 2차원 리스트와 dict 이용한 성적처리 프로그램

# 성적 데이터 저장할 변수 선언
sjs = []


# 프로그램 메뉴 출력을 위한 변수 선언

main_menu = f'''
성적 처리프로그램 v3b
====================
1. 성적 데이터 추가
2. 성적 데이터 조회
3. 성적 데이터 상세조회
4. 성적 데이터 수정
5. 성적 데이터 삭제
0. 프로그램 종료
===================='''

# 프로그램 주 실행부

while True:
    print(main_menu)
    menu = input('=> 작업을 선택하세요 :')

    if menu == '0':
        print('성적 프로그램을 종료 합니다 !')
        break

    elif menu == '1':
        name = input("이름은?")
        kor = int(input("국어는??"))
        eng = int(input("영어는??"))
        mat = int(input("수학은??"))

        # 성적 처리
        tot = kor + eng + mat
        avg = tot / 3
        grd = '가'
        if avg >= 90 : grd = '수'
        elif avg >= 80 : grd = '우'
        elif avg >= 70 : grd = '미'
        elif avg >= 60 : grd = '양'

        sj = { 'name': name, 'kor': kor, 'eng': eng, 'mat': mat,'tot': tot, 'avg': avg, 'grd': grd }


        sjs.append(sj)
        input('성적 데이터 추가 완료 !')


    elif menu == '2': # 이름,국어,영어,수학만 출력
        hdr =  '이름 국어 영어 수학 \n'
        hdr += '================='
        print(hdr)

        for sj in sjs:
                print(f'{sj["name"]} {sj["kor"]} {sj["eng"]}{sj["mat"]}')
                input('성적 데이터 조회 완료 !')

    elif menu == '3': # 이름으로 검색 후 해당 학생의 정보 모두 출력
        name = input('조회할 학생의 이름은?')
        sj = None
        for item in sjs:
            if item['name'] == name: sj = item
            hdr = '이름 국어 영어 수학 총점 평균 학점 \n'
            hdr += '----------------------------\n'
            print(hdr)
            for k in sj.keys(): # sjs에서 입력한 이름과 일치하는 항목을 찾음
                print(sj.get(k), end=' ')

        input('\n성적 데이터 상세조회 완료 !')

    elif menu == '4':
        name = input("수정할 학생 이름은 ? ")


        sj = None
        for item in sjs: # 입력한 이름과 일치하는 항목을 sjs에서 찾음
            if (sjs[i])['name'] == name: idx = i
            break

        # 새로운 값을 입력받음
        kor = int(input(f'새로운 국어 점수는? ({sjs[idx]["kor"]}'))
        eng = int(input(f'새로운 영어 점수는? ({sjs[idx]["eng"]}'))
        mat = int(input(f'새로운 수학 점수는? ({sjs[idx]["mat"]}'))

        # 다시 성적 처리
        tot = kor + eng + mat
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

        # 값 다시 저장
        sj = { 'name':name, 'kor':kor, 'eng':eng, 'mat':mat, 'tot':tot, 'avg':avg, 'grd':grd }


        # 기존 위치에 다시 저장
        sjs[idx] = sj
        print('성적 데이터 수정 완료 !')

    elif menu == '5':
        name = input("삭제할 데이터의 학생 이름은")

        idx = None
        for i in range(len(sjs)): # 삭제할 데이터의 인덱스 조사
            item = sjs[i]
            if item['name'] == name : idx = i
            sjs.pop(idx)

  #      for sjs in sj:
   #         print(f'{sj["name"]}을 정말 삭제합니다')
    #        del sj['name',"kor",'eng','mat']

        input('성적 데이터 삭제 완료 !')

    else:
        print('잘못된 번호를 입력하셨습니다.')