from SungJukVO import SungJukVO
from SungJukv8DAO import SungJukv8DAO as dao


class SungJukv8Lib:

    @staticmethod
    def display_menu(self):
        main_menu = (
            "성적 처리프로그램 v7\n"
            "-------------------\n"
            "1. 성적 데이터 추가\n"
            "2. 성적 데이터 조회\n"
            "3. 성적 데이터 상세조회\n"
            "4. 성적 데이터 수정\n"
            "5. 성적 데이터 삭제\n"
            "0. 프로그램 종료\n"
            "-------------------\n")
        print(main_menu)
        return input('=> 메뉴를 선택하세요 : ')

    @staticmethod
    def add_sungjuk(self):
        # 성적 데이터 입력받기
        sj = self.__input_sungjuk()

        # 성적처리
        tot, avg, grd = self.compute_sungjuk(sj)

        # 처리된 성적데이터를 sungjuk 테이블에 저장
        cnt = dao.insert_sungjuk(self, sj)

        print(cnt, '개의 성적 데이터가 추가됨!')

    @staticmethod
    def read_sungjuk(self):
        hdr = ("이름 국어 영어 수학\n"
               "--------------------")
        print(hdr)

        # 성적테이블에서 이름/국어/영어/수학 만 select해서 출력
        result, cnt = dao.select_sungjuk()

        # 조회된 데이터 출력
        print(result)
        print(cnt, '개의 성적 데이터가 조회됨!')

    @staticmethod
    def read_one_sungjuk(self):
        name = input('상세조회할 이름 : ')

        hdr = ("이름 국어 영어 수학 총점 평균 학점\n"
               "--------------------------------")
        print(hdr)

        # 입력한 학생이름으로 성적테이블을 조회해서 조회된 결과를 출력
        row = dao.selectone_sungjuk(name)

        result = f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]:.0f} {row[6]}\n'

        # 조회된 데이터 출력
        print(result)
        # print(cur.rowcount, '개의 성적 데이터가 조회됨!')

        # input('성적 데이터 상제조회 완료!')

    @staticmethod
    def modify_sungjuk(self, sjdao):
        name = input('수정할 이름 : ')

        # 수정할 학생이름으로 기존데이터 조회
        row, cnt = dao.selectone_sungjuk(name)

        if cnt < 1:
            print('그런 학생 음슴;')
        else:
            if input('수정하실..?(y/n) ').upper() == 'Y':
                # 수정할 성적 데이터 입력받기
                sj = sjdao.selectone_sungjuk(name)
                # 번호/이름/국어/영어/수학/총점/평균/학점/등록일

                # 새로운(기존) 값을 입력받음
                kor = int(input(f'새로운 국어(기존점수 ({sj[2]}) : '))
                eng = int(input(f'새로운 영어(기존점수 ({sj[3]}): '))
                mat = int(input(f'새로운 수학(기존점수 ({sj[4]}): '))

                # 다시 성적처리
                sj =SungJukVO(name,kor,eng,mat)
                self.__compute_sungjuk(sj)

                if cnt > 0:
                    print('수정성공')
                else:
                    print('수정실패')

    @staticmethod
    def remove_sungjuk(self):
        name = input('삭제할 이름 : ')

        # 삭제할 학생이름 입력받아 성적테이블에서 학생 데이터 삭제
        cnt = dao.delete_sungjuk(name)

    def __compute_sungjuk(self,sj):
        sj.tot = sj.kor + sj.eng + sj.mat
        sj.avg = sj.tot / 3
        grd = '가'
        if sj.avg >= 90:
            grd = '수'
        elif sj.avg >= 80:
            grd = '우'
        elif sj.avg >= 70:
            grd = '미'
        elif sj.avg >= 60:
            grd = '양'


    def __input_sungjuk(self):
        name = input('이름 : ')
        kor = int(input('국어 : '))
        eng = int(input('영어 : '))
        mat = int(input('수학 : '))

        return SungJukVO(name, kor, eng, mat)