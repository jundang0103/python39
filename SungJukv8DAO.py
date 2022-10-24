from awsdlbinfo import awsdlbinfo as db


class SungJukv8DAO:
    def insert_sungjuk(self, sj):
        conn, cur = db.open_conn()

        sql = "insert into sungjuk(name,kor,eng,mat,tot,avg,grd) values (%s,%s,%s,%s,%s,%s,%s)"

        params = [sj.name, sj.kr, sj.eng, sj.mat, sj.tot,sj.tot, sj.avg, sj.grd]
        cur.execute(sql, params)
        conn.commit()
        cnt = cur.rowcount

        db.close_conn(conn, cur)

        return cnt

    def select_sungjuk(self):
        conn, cur = db.openConn()

        sql = "select name,kor,eng,mat from sungjuk order by sjno"
        cur.execute(sql)

        # 조회된 데이터 출력
        rows = cur.fetchall()
        result = ''
        for row in rows:
            result += f'{row[0]} {row[1]} {row[2]} {row[3]}\n'
        cnt = cur.rowcount

        db.closeConn(conn, cur)

        return result, cnt

    def selectone_sungjuk(self, name):
        conn, cur = db.openConn()

        sql = "select name,kor,eng,mat,tot,avg,grd from sungjuk where name=%s"
        params = (name,)
        cur.execute(sql, params)

        # 조회된 데이터 출력
        row = cur.fetchone()
        cnt = cur.rowcount
        # result = f'{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]:.0f} {row[6]}\n'

        db.closeConn(conn, cur)

        return row, cnt


    def update_sungjuk(self, sj):
        conn, cur = db.openConn()

        # sql = "update sungjuk set kor=%(kr)s,eng=%(en)s,mat=%(mt)s," \
        #       "tot=%(tt)s,avg=%(av)s,grd=%(gd)s, regdate=current_timestamp where name=%(nm)s"

        # params = (kor, eng, mat, tot, avg, grd, name)
        #params = dict(nm=name, kr=kor, en=eng, mt=mat, tt=tot, av=avg, gd=grd)
        sql = "update sungjuk set kor=%s,eng=%s,mat=%s," \
              "tot=%s,avg=%s,grd=%s, regdate=current_timestamp where name=%s"
        cur.execute(sql, sj)
        conn.commit()
        cnt = cur.rowcount

        db.closeConn(conn, cur)

        return cnt


    def delete_sungjuk(sele, name):
        conn, cur = db.openConn()

        sql = "delete from sungjuk where name=%s"
        params = (name,)
        cur.execute(sql, params)
        conn.commit()
        cnt = cur.rowcount

        db.closeConn(conn, cur)

        return cnt