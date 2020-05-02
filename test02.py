#데이터 베이스 (SQLite3) 모듈 연결
import sqlite3

#SQLite3 데이터베이스(명 : test.db) 연결
conn = sqlite3.connect("test.db")

#connect로부터 cursor 생성
cur = conn.cursor()

#DML(Data Manipulation Language)
#insert, update, delete
data = [
    ('워너원', 35, '부산'),
    ('AOA', 33, '경기'),
]
#executemany() : 복수 개의 Row 데이터를 한꺼번에 처리를 지원한 메스드
sql = "insert into customer (name, category, region) values (?, ?, ?)"
cur.executemany(sql, data)

conn.commit()
conn.close()
