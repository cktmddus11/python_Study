# 크롤링에 필요한 모듈 임포트
import requests
from bs4 import BeautifulSoup
import time
import urllib.request #
from selenium.webdriver import Chrome
import re
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import datetime as dt


# url을 불러오기 위한 사전작업 실행
# selenium 은 간단히 말해서 컴퓨터 = 나 
# 로딩이 끝날 때까지 기다려?
delay = 3
browser = Chrome()
browser.implicitly_wait(delay)

# 유튜브 url로 접속
start_url = 'https://'