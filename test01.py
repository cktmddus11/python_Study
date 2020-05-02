#데이터베이스(SQLite3) 모듈 연결
import sqlite3

#SQLite3 데이터베이스(명 : test.db) 연결
conn = sqlite3.connect("test.db")

#connect로부터 cursor 생성
cur = conn.cursor()

#SQL 쿼리문 실행
cur.execute("select *from customer")

#데이터베이스의 모든 레코드
rows = cur.fetchall()
#모든 데이터를 반복하여 출력
for row in rows:
    print(row)
    
#데이터베이스 연결 종료
conn.close()
