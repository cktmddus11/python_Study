#dbTest06.py
from flask import Flask
#urllib 모듈을 읽어 들인다.
from urllib import request
#beautifulsoup4 모듈을 읽어 들인다. 
from bs4 import BeautifulSoup

#웹 서버 실행
app = Flask(__name__)
@app.route("/")
def hello():
      target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
      soup = BeautifulSoup(target, "html.parser")
      output = ""

      for location in soup.select("location"):
            output += "<h3>{} </h3>".format(location.select_one("city").string)
            output += "날씨:{} <br />".format(location.select_one("wf").string)
            output += "최저/최고 기온:{}/{}"\
                      .format(\
                            location.select_one("tmn").string, \
                            location.select_one("tmx").string\
                            )
            output += "<hr />"
      return output

if __name__== "__main__":
    app.run()     