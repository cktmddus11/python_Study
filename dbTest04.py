#dbTest04.py

#flask패키지에서 Flask 모듈을 임포트
from flask import Flask
#flask패키지에서 request 객체를 사용할 수 있도록 임포트
from flask import request
#json 라이브러리 임포트
import json
#sqlite3 라이브러리 임포트
import sqlite3

#Flask(서버) App 생성
app = Flask(__name__)
#디버그 모드를 실행(활성화)하기 위해서 선언
app.debug = True
#데이터베이스 연결을 위한 함수 선언
def get_db_con() -> sqlite3.connect:
    return sqlite3.connect("test.db")

#URL 경로
@app.route("/") #라우팅 다음에는 항상 라우팅 주소에 대한 함수 선언해야함
#test.db 안에 있는 모든 데이터를 가져오기 위한 함수 선언
def hello():
    with get_db_con() as con: #with 의 함수 리턴값 as 다음값으로 리턴값 받음?
        cur = con.cursor()
        # select 쿼리문을 저장하기 위한 변수 선언
        q = "select *from customer"
        result = cur.execute(q)
        #결과는 JSON 문자열 만들어 줌
        result_json = jsonize(result)
        return result_json

#데이터베이스의 result를 받아서 JSON 문자열로 생성하는 함수 선언
def jsonize(result):
    result_json = json.dumps(list(result.fetchall()), 
        ensure_ascii=False).encode("utf-8")
    return result_json

if __name__ == "__main__":
    #flask application 을 실행
    app.run()